from telegram import Bot
from config.settings import CHAT_ID,BOT_TOKEN

# send signal to telegram
async def send_signal_to_telegram(signal):
    message = f"""
        BANKNIFTY SIGNAL - BUY
        Option: {signal['option']}
        Entry: {signal['entry']}
        Target: {signal['target']}
        Stoploss: {signal['stoploss']}
        Qty: 1
    """
    bot = Bot(token=BOT_TOKEN)
    bot.send_message(chat_id=CHAT_ID,text=message)