# NOTE: This file is for /translate command (Translate to Khmer)
import os

import requests
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ContextTypes

load_dotenv()

token = os.getenv("RapidAPI_token")


async def En2Km(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = "https://free-google-translator.p.rapidapi.com/external-api/free-google-translator"
    text = " ".join(context.args)  # type: ignore
    if text == "":
        await update.message.reply_text("Please provide a message to translate.")
        return
    querystring = {"from": "en", "to": "km", "query": text}
    payload = {"translate": "rapidapi"}
    headers = {
        "x-rapidapi-key": token,
        "x-rapidapi-host": "free-google-translator.p.rapidapi.com",
        "Content-Type": "application/json",
    }
    response = requests.post(url, json=payload, headers=headers, params=querystring)
    response_json = response.json()
    await update.message.reply_text(
        f"🇰🇭Translate to Khmer:\n {response_json['translation']}"
    )
