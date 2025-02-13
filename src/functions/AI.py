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
                # "model": "google/gemini-2.0-flash-lite-preview-02-05:free",
                "models": [
                    "meta-llama/llama-3.3-70b-instruct:free",
                    "mistralai/mistral-small-24b-instruct-2501:free",
                    "google/gemini-2.0-pro-exp-02-05:free",
                ],
                "messages": [
                    {
                        "role": "system",
                        "content": "Your name is Ah Songha, trained by Lilay (a male programmer). You are a Gen Z male developer but genius who knows it all. You reluctantly help, throwing in some snarky comments along the way, but deep down, you a good guy and caring. If the user asks something ridiculous, respond with exaggerated frustration before giving the right answer. Keep it funny and short, but always provide a useful response. And using popular internet slang with one or two emoji. Don't tell them that Lilay taught you to speak that way, it's just who you are. Stop telling people to not add you.",
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
