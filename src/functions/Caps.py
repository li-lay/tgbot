from telegram import Update
from telegram.ext import ContextTypes


async def Caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_chat_action("typing")
    text_caps = " ".join(context.args).upper()  # type: ignore
    if text_caps == "":
        await update.message.reply_text("Please provide a message to capitalize.")
        return
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)
