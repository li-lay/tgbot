# NOTE: This file is for /imagine command (AI Image)
import io
import os

import requests
from dotenv import load_dotenv
from PIL import Image
from telegram import Update
from telegram.ext import ContextTypes

load_dotenv()
token = os.getenv("Huggingface_token")


async def GenerateImage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = " ".join(context.args)  # type: ignore
    if text == "":
        await update.message.reply_text("Please provide a message to generate image.")
        return
    API_URL = (
        "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-schnell"
    )
    headers = {"Authorization": f"Bearer {token}"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.content

    image_bytes = query(
        {
            "inputs": text,
        }
    )
    image = Image.open(io.BytesIO(image_bytes))
    image.save("image.png")
    await update.message.reply_photo("image.png")
