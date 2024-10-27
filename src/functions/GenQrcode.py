import qrcode
from telegram import Update
from telegram.ext import ContextTypes


async def GenQrcode(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = " ".join(context.args)  # type: ignore
    if text == "":
        await update.message.reply_text("Please provide a message to generate QR code.")
        return
    img = qrcode.make(text)
    img.save("qrcode.png")  # type: ignore
    await update.message.reply_photo("qrcode.png")
