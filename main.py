
from telegram import Update, Animation
from telegram.ext import filters, ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler

from env_keys import TG_BOT_API

from ready_messages import START_MESSAGE
from resp import get_response_text

from tg_bot_tools import app


app.run_polling()