# import requests 
# import pandas as pd 
# from telegram import Bot 
from config.settings import CHAT_ID, BOT_TOKEN ,BANKNIFTY_SYMBOL,PCR_BULLISH_THRESHOLD
# from services.nse_fetcher import fetch_option_chain 
# from logic.signal_generator import generate_signal 
# from services.telegram_bot import send_signal_to_telegram 
# import schedule 
# import time 
# from nsepython import *

# def main(): 
#    try:  
#        data = fetch_option_chain() 
#        print("Fetched data")
#        signal = generate_signal(data) 
#        print("Signal generated ",signal)
#        print("data ", data) 
#        send_signal_to_telegram(signal) 
#    except Exception as e: 
#        print(f"Error: {e}") 

# schedule.every(2).minutes.do(main)  # Run the script every 15 minutes 

# while True: 
#    schedule.run_pending() 
#    time.sleep(1) 
 
 
import requests 
import asyncio 
from telegram import Bot  
from services.nse_fetcher import fetch_option_chain 
from logic.signal_generator import generate_signal 
from services.telegram_bot import send_signal_to_telegram 

def fetch_option_chain(symbol="BANKNIFTY"): 
    url = f"https://www.nseindia.com/api/option-chain-v3?type=Indices&symbol={symbol}" 
    headers = { 
       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36', 
       'Authorization': 'Bearer YOUR_API_KEY' 
    } 
    try: 
       response = requests.get(url, headers=headers) 
       response.raise_for_status() 
       return response.json() 
    except requests.exceptions.RequestException as e: 
       print(f"Error: {e}") 
       return None 

async def send_signal_to_telegram(signal): 
   if signal: 
       message = f""" 
           BANKNIFTY SIGNAL - BUY 
           Option: {signal['option']} 
           Entry: {signal['entry']} 
           Target: {signal['target']} 
           Stoploss: {signal['stoploss']} 
           Qty: 1 
       """ 
       bot = Bot(token=BOT_TOKEN) 
       await bot.send_message(chat_id=CHAT_ID, text=message) 

def generate_signal(data): 
   # Analyze the data and generate a signal 
   # For example: 
   if data: 
       signal = { 
           "option": "48800 CE", 
           "entry": "Rs. 185-195", 
           "target": "Rs. 230", 
           "stoploss": "Rs. 160" 
       } 
   else: 
       signal = None 
   return signal 

async def main(): 
   data = fetch_option_chain() 
   signal = generate_signal(data) 
   print("data ", data) 
   await send_signal_to_telegram(signal) 
   print("signal sent to the telegram ", data) 

if __name__ == "__main__": 
   asyncio.run(main()) 
