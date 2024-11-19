from telegram import Update
from telegram.ext import ContextTypes


async def Help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_chat_action("typing")
    await update.message.reply_text(
        "/chat - Chat with AI!\n/img - Generate AI Image!\n/km - Translate English to Khmer!\n/qrcode - Generate qrcode!\n/meme - Get random meme!\n/help - Show all commands!\n/cowsay - cow will say...!\n/caps - Capitalize your message!\n/myinfo - Show your account informations!"
    )
