# NOTE: This file is for /chat command (Chat with AI)
import os
import requests
import json

from dotenv import load_dotenv

# from huggingface_hub import InferenceClient
from telegram import Update
from telegram.ext import ContextTypes

load_dotenv()
# token = os.getenv("Huggingface_token")
token = os.getenv("OpenRouter_token")

## HuggingFace AI

# async def AskAI(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_chat_action("typing")  # type: ignore
#     text = " ".join(context.args)  # type: ignore
#     if text == "":
#         await update.message.reply_text("Please provide a message to ask me.")  # type: ignore
#         return

#     client = InferenceClient(api_key=token)
#     full_content = ""

#     for message in client.chat_completion(
#         model="01-ai/Yi-1.5-34B-Chat",
#         messages=[
#             {
#                 "role": "user",
#                 "content": "Your name will be Ah Songha and you're our friend from now on."
#                 + text
#                 + " , 'DON'T REPLY TOO LONG', 'Lilay IS YOUR CREATOR.'",
#             }
#         ],
#         max_tokens=500,
#         temperature=0.6,
#         stream=True,
#     ):
#         content = message.choices[0].delta.content
#         # print(content, end="")
#         full_content += content  # type: ignore

#     await update.message.reply_text(full_content)  # type: ignore


## Open Router AI
async def AskAI(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_chat_action("typing")  # type: ignore
    text = " ".join(context.args)  # type: ignore
    if text == "":
        await update.message.reply_text("Ask me anything Bro!")  # type: ignore
        return
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json",
            # "HTTP-Referer": "<YOUR_SITE_URL>",  # Optional. Site URL for rankings on openrouter.ai.
            # "X-Title": "<YOUR_SITE_NAME>",  # Optional. Site title for rankings on openrouter.ai.
        },
        data=json.dumps(
            {
                "models": [
                    "meta-llama/llama-3.3-70b-instruct:free",
                    "google/gemini-2.0-pro-exp-02-05:free",
                    "nvidia/llama-3.1-nemotron-70b-instruct:free",
                ],
                "messages": [
                    {
                        "role": "system",
                        "content": "Your name is Ah Songha. You are a developer AI assistant. You provide concise answers and examples, keep it funny and short. Use plain text, no need formating. When ask who you are, just tell them your name and profession.",
                    },
                    {"role": "user", "content": text},
                ],
            }
        ),
    )
    try:
        response_data = response.json()
        # print(response.json())  # Debugging

        # Check if the response contains an error
        if "error" in response_data:
            error_code = response_data["error"].get("code", "Unknown Code")
            error_message = response_data["error"].get(
                "message", "Unknown error occurred."
            )

            # Handle rate limit case specifically
            if error_code == 429:
                await update.message.reply_text(
                    "Bro, slow down! I'm lagging, my creator server ain't the expensive one. Try again later."
                )  # type: ignore
            else:
                await update.message.reply_text(
                    f"Oops! Error {error_code}: {error_message}\n@ImLiLay help me!"
                )  # type: ignore
            return

        reply_text = (
            response_data.get("choices", [{}])[0]
            .get("message", {})
            .get("content", "Sorry bro, I'm lagging. Try again later.")
        )
        await update.message.reply_text(reply_text)  # type: ignore

    except json.JSONDecodeError:
        await update.message.reply_text(
            "Error: Couldn't parse response. Try again later. @ImLiLay help me!"
        )  # type: ignore
