from telegram import Update
from telegram.ext import ContextTypes

async def english(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to Glutea!\nHere you’ll find smart workouts, challenges and personalized fitness tools.\nLet’s get started!"
    )
