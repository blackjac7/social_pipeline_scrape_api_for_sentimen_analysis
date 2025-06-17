import requests

def fetch_country_data(name="indonesia"):
    url = f"https://restcountries.com/v3.1/name/{name}"
    resp = requests.get(url); resp.raise_for_status()
    data = resp.json()[0]
    return {
        "name": data["name"]["common"],
        "population": data["population"],
        "area": data["area"],
        "languages": list(data["languages"].values()),
        "currencies": data["currencies"],
        "gini": data.get("gini", {}),
        "region": data["region"],
        "subregion": data["subregion"],
        "latlng": data["latlng"],
    }