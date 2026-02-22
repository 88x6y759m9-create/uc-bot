import telebot
from telebot import types
import os

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton("💎 60 UC — 1€", callback_data="60")
    btn2 = types.InlineKeyboardButton("💎 325 UC — 5€", callback_data="325")

    markup.add(btn1)
    markup.add(btn2)

    bot.send_message(message.chat.id,
                     "💎 Выберите пакет UC:",
                     reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "60":
        bot.send_message(call.message.chat.id,
                         "✅ Вы выбрали 60 UC.\n\nНапишите ваш ID PUBG.")
    elif call.data == "325":
        bot.send_message(call.message.chat.id,
                         "✅ Вы выбрали 325 UC.\n\nНапишите ваш ID PUBG.")

print("Bot started")
bot.infinity_polling()
