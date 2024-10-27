import logging
import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from functions.AI import AskAI
from functions.AI_Image import GenerateImage
from functions.API_Limit import GetAPILimits
from functions.Caps import Caps
from functions.GenQrcode import GenQrcode
from functions.GetMeme import GetMeme
from functions.Hello import Hello
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
    await update.message.reply_text(
        f"👋Hello {update.effective_user.first_name}, please use /help to see all available commands!"
    )


app = ApplicationBuilder().token(dev_api).build()

app.add_handler(CommandHandler(("start").lower(), Start))
app.add_handler(CommandHandler(("hello").lower(), Hello))
app.add_handler(CommandHandler(("hi").lower(), Hello))
app.add_handler(CommandHandler(("caps").lower(), Caps))
app.add_handler(CommandHandler(("myinfo").lower(), MyInfo))
app.add_handler(CommandHandler(("info").lower(), MyInfo))
app.add_handler(CommandHandler(("help").lower(), Help))
app.add_handler(CommandHandler(("translate").lower(), En2Km))
app.add_handler(CommandHandler(("meme").lower(), GetMeme))
app.add_handler(CommandHandler(("limit").lower(), GetAPILimits))
app.add_handler(CommandHandler(("qrcode").lower(), GenQrcode))
app.add_handler(CommandHandler(("chat").lower(), AskAI))
app.add_handler(CommandHandler(("imagine").lower(), GenerateImage))

app.run_polling()
