import logging
import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (ApplicationBuilder, CommandHandler, ContextTypes,
                          MessageHandler, filters)

from functions.AI import AskAI
from functions.AI_Image import GenerateImage
from functions.API_Limit import GetAPILimits
from functions.Caps import Caps
from functions.Cowsay import Cowsay
from functions.GenQrcode import GenQrcode
from functions.GetMeme import GetMeme
from functions.Help import Help
from functions.MyInfo import MyInfo
from functions.Translate import En2Km

load_dotenv()
prod_api = os.getenv(
    "Production_token", ""
)  # provide "" as default if Production_token not found
dev_api = os.getenv(
    "Development_token", ""
)  # provide "" as default if Development_token not found

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


async def Start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_chat_action("typing")
    await update.message.reply_text(
        f"👋Hello {update.effective_user.first_name}, please use /help to see all available commands!"
    )


app = ApplicationBuilder().token(dev_api).build()

app.add_handler(CommandHandler(("start").lower(), Start))
app.add_handler(CommandHandler(("hello").lower(), Start))
app.add_handler(CommandHandler(("hi").lower(), Start))
app.add_handler(CommandHandler(("caps").lower(), Caps))
app.add_handler(CommandHandler(("myinfo").lower(), MyInfo))
app.add_handler(CommandHandler(("info").lower(), MyInfo))
app.add_handler(CommandHandler(("help").lower(), Help))
app.add_handler(CommandHandler(("km").lower(), En2Km))
app.add_handler(CommandHandler(("meme").lower(), GetMeme))
app.add_handler(CommandHandler(("limit").lower(), GetAPILimits))
app.add_handler(CommandHandler(("qrcode").lower(), GenQrcode))
app.add_handler(CommandHandler(("chat").lower(), AskAI))
app.add_handler(CommandHandler(("img").lower(), GenerateImage))
app.add_handler(CommandHandler(("cowsay").lower(), Cowsay))

# Handle unknown commands
app.add_handler(MessageHandler(filters.COMMAND, Start))

app.run_polling()
