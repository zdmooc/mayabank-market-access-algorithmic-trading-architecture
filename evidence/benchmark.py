import json,statistics,time
from market_access_lab.model import Order,Side
from market_access_lab.risk import RiskPolicy

def pct(v,p):
    s=sorted(v); r=(len(s)-1)*p; lo=int(r); hi=min(lo+1,len(s)-1); f=r-lo
    return s[lo]*(1-f)+s[hi]*f

def main():
    policy=RiskPolicy(allowed_instruments={"MAYA"}); samples=[]
    for i in range(5000):
        o=Order(f"B{i}","MAYA",Side.BUY,100,100.0)
        a=time.perf_counter_ns(); d=policy.check(o); b=time.perf_counter_ns()
        if not d.accepted: raise RuntimeError("unexpected reject")
        samples.append((b-a)/1000.0)
    print(json.dumps({"sample_count":len(samples),"unit":"microseconds",
      "p50":round(pct(samples,.5),3),"p95":round(pct(samples,.95),3),
      "p99":round(pct(samples,.99),3),"p999":round(pct(samples,.999),3),
      "max":round(max(samples),3),"mean":round(statistics.mean(samples),3),
      "claim":"PERFORMANCE_MEASURED_SYNTHETIC_ONLY"},indent=2))

if __name__=="__main__": main()
