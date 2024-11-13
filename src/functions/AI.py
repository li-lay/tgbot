# NOTE: This file is for /chat command (Chat with AI)
# import requests
# import json
import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from telegram import Update
from telegram.ext import ContextTypes

load_dotenv()
token = os.getenv("Huggingface_token")

# async def AskAI(update: Update, context: ContextTypes.DEFAULT_TYPE):
#   text = " ".join(context.args)
#   API_URL = "https://api-inference.huggingface.co/models/01-ai/Yi-1.5-34B-Chat/v1/chat/completions"
#   headers = {"Authorization": "Bearer hf_"}
#   payload = {
#       "inputs": text,
#   }
#   if payload["inputs"] != "":
#     response = requests.post(API_URL, headers=headers, json=payload)
#     response_json = response.json()
#     with open('response.json', 'w') as f:
#         json.dump(response_json, f)

#     if len(response_json) > 0:
#         await update.message.reply_text(response_json[0].get('generated_text', ''))
#     else:
#         await update.message.reply_text('No response from the AI model.')


async def AskAI(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = " ".join(context.args)  # type: ignore
    if text == "":
        await update.message.reply_text("Please provide a message to ask AI.")
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

    await update.message.reply_text(full_content)
