# NOTE: This file is for /chat command (Chat with AI)
import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from telegram import Update
from telegram.ext import ContextTypes

load_dotenv()
token = os.getenv("Huggingface_token")


async def AskAI(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_chat_action("typing")  # type: ignore
    text = " ".join(context.args)  # type: ignore
    if text == "":
        await update.message.reply_text("Please provide a message to ask AI.")  # type: ignore
        return

    client = InferenceClient(api_key=token)
    full_content = ""

    for message in client.chat_completion(
        model="01-ai/Yi-1.5-34B-Chat",
        messages=[{"role": "user", "content": text}],
        max_tokens=500,
        temperature=0.5,
        stream=True,
    ):
        content = message.choices[0].delta.content
        # print(content, end="")
        full_content += content  # type: ignore

    await update.message.reply_text(full_content)  # type: ignore
