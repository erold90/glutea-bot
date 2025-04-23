import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler

from handlers.start import start
from handlers.english import english
from handlers.francais import francais
from handlers.italiano import italiano
from handlers.espanol import espanol
from handlers.russian import russian

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("english", english))
    app.add_handler(CommandHandler("francais", francais))
    app.add_handler(CommandHandler("italiano", italiano))
    app.add_handler(CommandHandler("espanol", espanol))
    app.add_handler(CommandHandler("russian", russian))

    print("Bot is running...")
    app.run_polling()
