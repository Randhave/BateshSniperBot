import requests 
import pandas as pd 
from telegram import Bot 
from config.settings import CHAT_ID, BOT_TOKEN ,BANKNIFTY_SYMBOL,PCR_BULLISH_THRESHOLD
from services.nse_fetcher import fetch_option_chain 
from logic.signal_generator import generate_signal 
from services.telegram_bot import send_signal_to_telegram 
import schedule 
import time 

def main(): 
   try:  
       data = fetch_option_chain() 
       print("Fetched data")
       signal = generate_signal(data) 
       print("Signal generated ",signal)
       print("data ", data) 
       send_signal_to_telegram(signal) 
   except Exception as e: 
       print(f"Error: {e}") 

schedule.every(5).minutes.do(main)  # Run the script every 15 minutes 

while True: 
   schedule.run_pending() 
   time.sleep(1) 
