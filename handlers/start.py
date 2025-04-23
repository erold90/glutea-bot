from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "👋 Welcome to Glutea – your smart fitness assistant\n"
        "🇫🇷 Bienvenue sur Glutea – votre coach fitness intelligent\n"
        "🇮🇹 Benvenuto su Glutea – il tuo assistente fitness intelligente\n"
        "🇪🇸 Bienvenido a Glutea – tu asistente de fitness inteligente\n"
        "🇷🇺 Добро пожаловать в Glutea – ваш умный фитнес-ассистент\n"
        "\nPlease select your language:"
    )
    keyboard = [["English 🇬🇧", "Français 🇫🇷"], ["Italiano 🇮🇹", "Español 🇪🇸", "Русский 🇷🇺"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(text, reply_markup=reply_markup)
