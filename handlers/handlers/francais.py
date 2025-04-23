from telegram import Update
from telegram.ext import ContextTypes

async def francais(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Bienvenue sur Glutea !\nVous trouverez ici des entraînements intelligents, des défis et des outils personnalisés pour votre remise en forme.\nC’est parti !"
    )
