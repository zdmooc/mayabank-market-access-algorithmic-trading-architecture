from dataclasses import dataclass,field
from .fix_session import FixLikeSession
from .model import Order,OrderStatus
from .risk import RiskPolicy

@dataclass
class MarketAccessEngine:
    risk_policy:RiskPolicy
    session:FixLikeSession=field(default_factory=FixLikeSession)
    orders:dict[str,Order]=field(default_factory=dict)
    drop_copy:list[dict]=field(default_factory=list)

    def start(self): self.session.connect()

    def submit(self,order,market_data_age_ms=0.0):
        self.orders[order.order_id]=order
        d=self.risk_policy.check(order,market_data_age_ms)
        if not d.accepted:
            order.reject(d.reason)
            self.drop_copy.append({"order_id":order.order_id,"event":"RISK_REJECT","reason":d.reason})
            return order
        self.session.send(f"NEW:{order.order_id}:{order.instrument}:{order.qty}:{order.limit_price}")
        order.acknowledge()
        self.drop_copy.append({"order_id":order.order_id,"event":"NEW"})
        return order

    def fill(self,order_id,qty):
        o=self.orders[order_id]
        o.fill(qty)
        self.drop_copy.append({"order_id":order_id,"event":"FILL","qty":qty,"cum_qty":o.cum_qty,"leaves_qty":o.leaves_qty})
        return o

    def request_cancel(self,order_id):
        o=self.orders[order_id]
        o.request_cancel()
        self.session.send(f"CANCEL:{order_id}")
        self.drop_copy.append({"order_id":order_id,"event":"CANCEL_REQUEST"})
        return o

    def fill_wins_cancel_race(self,order_id,qty):
        o=self.orders[order_id]
        if o.status!=OrderStatus.PENDING_CANCEL: raise ValueError("not pending cancel")
        o.status=OrderStatus.NEW if o.cum_qty==0 else OrderStatus.PARTIALLY_FILLED
        o.fill(qty)
        self.drop_copy.append({"order_id":order_id,"event":"FILL_DURING_CANCEL","qty":qty})
        return o

    def kill(self,*,trader=None,algo=None,venue=None):
        ids=[]
        for o in self.orders.values():
            if not o.active: continue
            if trader is not None and o.trader!=trader: continue
            if algo is not None and o.algo!=algo: continue
            if venue is not None and o.venue!=venue: continue
            if o.status in {OrderStatus.NEW,OrderStatus.PARTIALLY_FILLED}:
                o.request_cancel(); ids.append(o.order_id)
                self.drop_copy.append({"order_id":o.order_id,"event":"KILL_CANCEL_REQUEST"})
        return ids
