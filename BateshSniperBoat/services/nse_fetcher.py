import requests

def fetch_option_chain(symbol="BANKNIFTY"):
    url = f"https://www.nseindia.com/api/option-chain-indices?symbol={symbol}"
    url = f"https://www.nseindia.com/api/option-chain-v3?type=Indices&symbol={symbol}"
    headers = {"User-Agent":"Mozilla/5.0"}
    session = requests.Session() 
    try:
        response = session.get(url,headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"[Error] Failed to fetch data : {e}")
        return None