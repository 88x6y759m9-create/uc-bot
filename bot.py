import telebot
import os

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     "💎 UC SHOP\n\n"
                     "60 UC — 1€\n"
                     "325 UC — 5€")

print("Bot started")
bot.infinity_polling()
