# NOTE: This file is for /meme command (Get meme)
import os

import requests
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ContextTypes

load_dotenv()

token = os.getenv("RapidAPI_token")


async def GetMeme(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_chat_action("upload_photo")
    url = "https://programming-memes-images.p.rapidapi.com/v1/memes"
    headers = {
        "x-rapidapi-key": token,
        "x-rapidapi-host": "programming-memes-images.p.rapidapi.com",
    }
    response = requests.get(url, headers=headers).json()
    await update.message.reply_photo(response[0]["image"])
