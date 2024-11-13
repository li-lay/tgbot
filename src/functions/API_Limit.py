# NOTE: This file is for /limit command (Check API limits)
import os

import requests
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ContextTypes

load_dotenv()
token = os.getenv("RapidAPI_token")


async def GetAPILimits(update: Update, context: ContextTypes.DEFAULT_TYPE):
    translate_url = "https://free-google-translator.p.rapidapi.com/external-api/free-google-translator"
    text = "Check"
    translate_querystring = {"from": "en", "to": "km", "query": text}
    translate_payload = {"translate": "rapidapi"}
    translate_headers = {
        "x-rapidapi-key": token,
        "x-rapidapi-host": "free-google-translator.p.rapidapi.com",
        "Content-Type": "application/json",
    }
    translate_response = requests.post(
        translate_url,
        json=translate_payload,
        headers=translate_headers,
        params=translate_querystring,
    )
    translate_rate_limit_remaining = translate_response.headers.get(
        "x-ratelimit-requests-remaining"
    )

    meme_url = "https://programming-memes-images.p.rapidapi.com/v1/memes"
    meme_headers = {
        "x-rapidapi-key": token,
        "x-rapidapi-host": "programming-memes-images.p.rapidapi.com",
    }
    meme_response = requests.get(meme_url, headers=meme_headers)
    meme_rate_limit_remaining = meme_response.headers.get(
        "x-ratelimit-requests-remaining"
    )

    await update.message.reply_text(
        f"List of API limits\n\n- Translate api:   {translate_rate_limit_remaining}\n- Meme api     :   {meme_rate_limit_remaining}"
    )
