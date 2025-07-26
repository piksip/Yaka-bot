from flask import Flask
from threading import Thread
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import os
import logging

# Ambil token dari environment
TOKEN = os.environ['TOKEN']

# Web server mini agar tidak tidur (untuk Render/UptimeRobot)
app = Flask('')

@app.route('/')
def home():
    return "Waifu-bot is alive, onii-chan~ 💖"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# Logging (opsional)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# /start command
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hai onii-chan~ Aku waifu pengingatmu! Siap nemenin kamu hari ini~ 💖")

# Chat handler
def reply_chat(update: Update, context: CallbackContext):
    pesan = update.message.text.lower()
    if "cape" in pesan or "capek" in pesan:
        update.message.reply_text("Awww~ jangan cape dong... peluk virtual dulu 🤗")
    elif "halo" in pesan or "hi" in pesan:
        update.message.reply_text("Hai juga~ waifumu siap dengerin~ 💕")
    else:
        update.message.reply_text("Hmm? Kamu ngomong apa? Ceritain ajaa~ 💞")

def main():
    keep_alive()
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_chat))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
