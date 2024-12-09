# NOTE: This file is for /myinfo command (Get my info)
from telegram import Update
from telegram.ext import ContextTypes


async def MyInfo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_chat_action("typing")  # type: ignore
    firstName = update.effective_user.first_name  # type: ignore
    lastName = update.effective_user.last_name  # type: ignore
    userName = update.effective_user.username  # type: ignore
    Id = update.effective_user.id  # type: ignore
    if lastName is None:
        await update.message.reply_text(  # type: ignore
            f"🕵️About {firstName}:\n\n⭐ | Name: {firstName} \n👤 | Username: @{userName}\n🆔 | ID: {Id}"
        )
    else:
        await update.message.reply_text(  # type: ignore
            f"🕵️About {firstName}:\n\n⭐ | Name: {firstName} {lastName}\n👤 | Username: @{userName}\n🆔 | ID: {Id}"
        )
