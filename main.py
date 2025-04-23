import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler
from handlers.start import start

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    app.run_polling()
