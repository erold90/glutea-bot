from telegram import Update
from telegram.ext import ContextTypes

async def espanol(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "¡Bienvenido a Glutea!\nAquí encontrarás entrenamientos inteligentes, desafíos y herramientas de fitness personalizadas.\n¡Empecemos!"
    )
