from .engine import MarketAccessEngine
from .model import Order,Side
from .risk import RiskPolicy

def main():
    e=MarketAccessEngine(RiskPolicy(allowed_instruments={"MAYA"})); e.start()
    o=Order("ORD-1","MAYA",Side.BUY,10_000,100.0,trader="DJ-TRADER",algo="TWAP")
    e.submit(o); e.fill("ORD-1",2_000); e.fill("ORD-1",5_000); e.fill("ORD-1",3_000)
    r=Order("ORD-2","MAYA",Side.BUY,200_000,100.0); e.submit(r)
    print("ORD-1",o.status.value,o.cum_qty,o.leaves_qty)
    print("ORD-2",r.status.value,r.reject_reason)
    print("DROP_COPY_EVENTS",len(e.drop_copy))

if __name__=="__main__": main()
