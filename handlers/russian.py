from telegram import Update
from telegram.ext import ContextTypes

async def russian(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Добро пожаловать в Glutea!\nЗдесь вы найдёте умные тренировки, челленджи и персонализированные фитнес-инструменты.\nНачнём!"
    )
