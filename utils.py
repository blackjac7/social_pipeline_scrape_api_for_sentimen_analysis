import pandas as pd

def combine_sources(data_dict):
    rows = []
    for src, recs in data_dict.items():
        for r in recs:
            r["source"] = src
            rows.append(r)
    return pd.DataFrame(rows)

def save_json(obj, filename):
    if isinstance(obj, pd.DataFrame):
        obj.to_json(filename, orient="records", lines=True)
    else:
        pd.DataFrame([obj]).to_json(filename, orient="records")
    print(f"✅ Saved to {filename}")
