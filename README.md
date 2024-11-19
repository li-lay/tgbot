# TgBot
Your neighborhood Telegram bot!
It's my first time using Telegram Bot API, so I'm still learning.

## Commands

| Command | Description |
| --- | --- |
| /chat | Chat with AI |
| /img | Generate AI Image |
| /km | Translate English to Khmer |
| /qrcode | Generate qrcode |
| /meme | Get random meme |
| /help | Show all commands |
| /cowsay | cow will say... |
| /caps | Capitalize your message |
| /myinfo | Show your account informations |

## Requirements
- Python 3.10 or above
- Telegram Bot API
- Huggingface Inference API
- RapidAPI

## Installation

1. Clone the repository
2. Create a .env file in the src directory with the following content:
```
Production_token=<your bot token> # telegram bot api for production
Development_token=<your bot token> # telegram bot api for testing
Huggingface_token=<your huggingface token> # AI
RapidAPI_token=<your rapidapi token> # Rapid API
```
3. Install the required packages using the following command:
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
4. Run the following command in the root directory of the project:
```
python src/main.py
```

## Or Using Docker
1. Build the image
```
docker build -t tgbot .
```
2. Run the container
```
docker run -d -p 8080:8080 tgbot
```
