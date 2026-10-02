from dataclasses import dataclass
from enum import Enum

class Side(str, Enum):
    BUY="BUY"
    SELL="SELL"

class OrderStatus(str, Enum):
    PENDING_NEW="PENDING_NEW"
    NEW="NEW"
    PARTIALLY_FILLED="PARTIALLY_FILLED"
    FILLED="FILLED"
    PENDING_CANCEL="PENDING_CANCEL"
    CANCELED="CANCELED"
    REJECTED="REJECTED"
    RECONCILIATION_REQUIRED="RECONCILIATION_REQUIRED"

@dataclass
class Order:
    order_id:str
    instrument:str
    side:Side
    qty:int
    limit_price:float
    trader:str="TRADER-1"
    algo:str="MANUAL"
    venue:str="SIM-VENUE"
    cum_qty:int=0
    status:OrderStatus=OrderStatus.PENDING_NEW
    reject_reason:str|None=None

    @property
    def leaves_qty(self): return max(0,self.qty-self.cum_qty)

    @property
    def active(self): return self.status not in {OrderStatus.FILLED,OrderStatus.CANCELED,OrderStatus.REJECTED}

    def acknowledge(self):
        if self.status!=OrderStatus.PENDING_NEW: raise ValueError("invalid ack")
        self.status=OrderStatus.NEW

    def reject(self,reason):
        self.reject_reason=reason
        self.status=OrderStatus.REJECTED

    def fill(self,qty):
        if qty<=0 or qty>self.leaves_qty or not self.active: raise ValueError("invalid fill")
        self.cum_qty+=qty
        self.status=OrderStatus.FILLED if self.leaves_qty==0 else OrderStatus.PARTIALLY_FILLED

    def request_cancel(self):
        if self.status not in {OrderStatus.NEW,OrderStatus.PARTIALLY_FILLED}: raise ValueError("invalid cancel")
        self.status=OrderStatus.PENDING_CANCEL

    def cancel_confirmed(self):
        if self.status!=OrderStatus.PENDING_CANCEL: raise ValueError("invalid cancel confirmation")
        self.status=OrderStatus.CANCELED
