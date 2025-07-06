import requests
from nsepython import *
import certifi

def fetch_option_chain(symbol="BANKNIFTY"): 
   url = f"https://www.nseindia.com/api/option-chain-v3?type=Indices&symbol={symbol}" 
   headers = { 
       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36' 
   } 
   try: 
       response = requests.get(url, headers=headers, verify=certifi.where()) 
       response.raise_for_status() 
       return response.json() 
   except requests.exceptions.RequestException as e: 
       print(f"Error: {e}") 
       return None 