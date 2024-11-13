# NOTE: This file is for /cowsay command (Cowsay)
from telegram import Update
from telegram.ext import ContextTypes


async def Cowsay(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = " ".join(context.args)  # type: ignore
    if text == "":
        await update.message.reply_text("Please provide a message to say.")
        return

    cow = r"""
           \
             \   ^__^
              \  (oo)\_________
                 (__)\                  )\/\
                        ||------w  |
                        ||         ||
    """

    # result = "\n".join([top] + middle + [bottom])  # join the top, middle and bottom

    await update.message.reply_text(f"{text}{cow}")
