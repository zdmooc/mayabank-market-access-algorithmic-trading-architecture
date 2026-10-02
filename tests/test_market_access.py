import unittest
from market_access_lab.engine import MarketAccessEngine
from market_access_lab.fix_session import FixLikeSession
from market_access_lab.model import Order,OrderStatus,Side
from market_access_lab.risk import RiskPolicy

class Tests(unittest.TestCase):
    def engine(self):
        e=MarketAccessEngine(RiskPolicy(max_qty=100_000,max_notional=5_000_000,
            max_market_data_age_ms=100,allowed_instruments={"MAYA"})); e.start(); return e

    def test_happy_path_and_invariant(self):
        e=self.engine(); o=Order("A","MAYA",Side.BUY,10_000,100)
        e.submit(o); e.fill("A",2_000)
        self.assertEqual(o.status,OrderStatus.PARTIALLY_FILLED)
        self.assertEqual(o.cum_qty+o.leaves_qty,o.qty)
        e.fill("A",8_000); self.assertEqual(o.status,OrderStatus.FILLED)

    def test_risk_reject(self):
        e=self.engine(); o=Order("B","MAYA",Side.BUY,100_001,10); e.submit(o)
        self.assertEqual(o.reject_reason,"MAX_QTY")

    def test_stale_market_data(self):
        e=self.engine(); o=Order("C","MAYA",Side.BUY,100,10); e.submit(o,101)
        self.assertEqual(o.reject_reason,"STALE_MARKET_DATA")

    def test_cancel_fill_race(self):
        e=self.engine(); o=Order("D","MAYA",Side.BUY,100,10); e.submit(o); e.request_cancel("D")
        e.fill_wins_cancel_race("D",100); self.assertEqual(o.status,OrderStatus.FILLED)

    def test_sequence_gap_duplicate_and_reconnect(self):
        s=FixLikeSession(); s.connect()
        self.assertEqual(s.receive(1,"X")["status"],"ACCEPTED")
        g=s.receive(4,"X"); self.assertEqual((g["resend_begin"],g["resend_end"]),(2,3))
        self.assertEqual(s.receive(1,"X")["status"],"DUPLICATE_OR_REPLAY")
        self.assertEqual(s.send("ONE")["seq"],1); s.disconnect(); s.connect()
        self.assertEqual(s.send("TWO")["seq"],2)

    def test_replay(self):
        s=FixLikeSession(); s.connect(); s.send("ONE"); s.send("TWO")
        self.assertEqual([x["seq"] for x in s.replay(1,2)],[1,2])

    def test_selective_kill(self):
        e=self.engine()
        a=Order("K1","MAYA",Side.BUY,10,10,trader="T1"); b=Order("K2","MAYA",Side.BUY,10,10,trader="T2")
        e.submit(a); e.submit(b)
        self.assertEqual(e.kill(trader="T1"),["K1"])
        self.assertEqual(a.status,OrderStatus.PENDING_CANCEL); self.assertEqual(b.status,OrderStatus.NEW)

if __name__=="__main__": unittest.main()
