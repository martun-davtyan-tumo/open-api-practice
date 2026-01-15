
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler

from env_keys import TG_BOT_API

from ready_messages import START_MESSAGE
from resp import get_response_text

async def startCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(START_MESSAGE)

async def echoMsg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"{update.message.text}")

async def handleQuestion(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(get_response_text(update.message.text))

app = ApplicationBuilder().token(token=TG_BOT_API).build()

app.add_handler(CommandHandler("start", startCommand))
app.add_handler(MessageHandler(filters.TEXT, handleQuestion))

app.run_polling()