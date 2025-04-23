from telegram import Update
from telegram.ext import ContextTypes

async def italiano(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Benvenuto su Glutea!\nQui troverai allenamenti intelligenti, sfide e strumenti fitness personalizzati.\nIniziamo!"
    )
