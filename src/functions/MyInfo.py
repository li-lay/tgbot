# NOTE: This file is for /myinfo command (Get my info)
from telegram import Update
from telegram.ext import ContextTypes


async def MyInfo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_chat_action("typing")
    firstName = update.effective_user.first_name
    lastName = update.effective_user.last_name
    userName = update.effective_user.username
    Id = update.effective_user.id
    if lastName is None:
        await update.message.reply_text(
            f"🕵️About {firstName}:\n\n⭐ | Name: {firstName} \n👤 | Username: @{userName}\n🆔 | ID: {Id}"
        )
    else:
        await update.message.reply_text(
            f"🕵️About {firstName}:\n\n⭐ | Name: {firstName} {lastName}\n👤 | Username: @{userName}\n🆔 | ID: {Id}"
        )
