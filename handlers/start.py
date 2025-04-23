from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "👋 Welcome to Glutea – your smart fitness assistant\n"
        "🇫🇷 Bienvenue sur Glutea – votre coach fitness intelligent\n"
        "🇮🇹 Benvenuto su Glutea – il tuo assistente fitness intelligente\n"
        "🇪🇸 Bienvenido a Glutea – tu asistente de fitness inteligente\n"
        "🇷🇺 Добро пожаловать в Glutea – ваш умный фитнес-ассистент\n\n"
        "Please select your language:"
    )

    keyboard = [
        [
            InlineKeyboardButton("English 🇬🇧", callback_data="english"),
            InlineKeyboardButton("Français 🇫🇷", callback_data="francais")
        ],
        [
            InlineKeyboardButton("Italiano 🇮🇹", callback_data="italiano"),
            InlineKeyboardButton("Español 🇪🇸", callback_data="espanol"),
            InlineKeyboardButton("Русский 🇷🇺", callback_data="russian")
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(text, reply_markup=reply_markup)
