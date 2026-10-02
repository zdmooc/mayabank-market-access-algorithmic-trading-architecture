from dataclasses import dataclass
from .model import Order

@dataclass(frozen=True)
class RiskDecision:
    accepted:bool
    reason:str="ACCEPT"

@dataclass
class RiskPolicy:
    max_qty:int=100_000
    max_notional:float=5_000_000.0
    price_floor:float=0.01
    price_ceiling:float=1_000_000.0
    max_market_data_age_ms:float=1_000.0
    allowed_instruments:set[str]|None=None
    route_enabled:bool=True

    def check(self,order:Order,market_data_age_ms:float=0.0):
        if self.allowed_instruments is not None and order.instrument not in self.allowed_instruments:
            return RiskDecision(False,"INSTRUMENT_NOT_ALLOWED")
        if not self.route_enabled: return RiskDecision(False,"ROUTE_DISABLED")
        if order.qty>self.max_qty: return RiskDecision(False,"MAX_QTY")
        if order.qty*order.limit_price>self.max_notional: return RiskDecision(False,"MAX_NOTIONAL")
        if not (self.price_floor<=order.limit_price<=self.price_ceiling): return RiskDecision(False,"PRICE_COLLAR")
        if market_data_age_ms>self.max_market_data_age_ms: return RiskDecision(False,"STALE_MARKET_DATA")
        return RiskDecision(True)
