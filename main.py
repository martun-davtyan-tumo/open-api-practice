
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler

from env_keys import TG_BOT_API
from resp import get_response_text

async def startCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello Martun")

async def echoMsg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"{update.message.text}")

app = ApplicationBuilder().token(token=TG_BOT_API).build()

app.add_handler(CommandHandler("start", startCommand))
app.add_handler(MessageHandler(None, echoMsg))

app.run_polling()