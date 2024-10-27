from telegram import Update
from telegram.ext import ContextTypes


async def Help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Use / to see all commands!")
