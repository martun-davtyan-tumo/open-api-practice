from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from telegram.constants import ChatAction

from env_keys import TG_BOT_API
from ready_messages import START_MESSAGE, get_sticker_id
from resp import get_response_text

async def startCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(START_MESSAGE)

async def echoMsg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"{update.message.text}")

async def handleQuestion(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)

    answer = get_response_text(update.message.text)
    sticker_id = get_sticker_id(answer)

    if sticker_id:
        await sendSticker(update, context, sticker_id)

    await update.message.reply_text(answer.split('Stick{')[0])

async def sendSticker(update: Update, context: ContextTypes.DEFAULT_TYPE, file_id: str) -> None:
    await context.bot.send_sticker(chat_id=update.effective_chat.id, sticker=file_id)

async def get_sticker_unique_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_sticker(update.message.sticker)
    print(update.message.sticker)

async def get_animation_unique_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_animation(update.message.animation)
    print(update.message.animation.file_id, update.message.animation.file_unique_id)
    print(update.message.animation)

app = ApplicationBuilder().token(token=TG_BOT_API).build()



app.add_handler(CommandHandler("start", startCommand))
app.add_handler(MessageHandler(filters.TEXT & filters.Sticker.ALL, handleQuestion))
# app.add_handler(MessageHandler(filters.Sticker.ALL, get_sticker_unique_id))
# app.add_handler(MessageHandler(filters.ANIMATION, get_animation_unique_id))
