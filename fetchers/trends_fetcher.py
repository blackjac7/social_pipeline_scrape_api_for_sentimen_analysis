from pytrends.request import TrendReq
import time

def fetch_trends(keyword, timeframe="2019-01-01 2019-12-31", geo="ID"):
    pt = TrendReq(hl="id-ID", tz=420)
    pt.build_payload([keyword], timeframe=timeframe, geo=geo)
    df = pt.interest_over_time()
    if not df.empty:
        df = df.reset_index()[["date", keyword]]
        df.columns = ["date", "trend"]
    return df