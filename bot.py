import telebot
from telebot import types
import os

TOKEN = os.getenv("TOKEN")
ADMIN_ID = 8019231475  # твой Telegram ID

bot = telebot.TeleBot(TOKEN)

user_data = {}

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("💎 60 UC — 1€", callback_data="60")
    btn2 = types.InlineKeyboardButton("💎 325 UC — 5€", callback_data="325")
    markup.add(btn1, btn2)

    bot.send_message(
        message.chat.id,
        "💎 Добро пожаловать в UC SHOP\n\nВыберите пакет:",
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    user_data[call.from_user.id] = {"package": call.data}
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, "📥 Введите ваш PUBG ID:")

@bot.message_handler(func=lambda message: message.from_user.id in user_data)
def get_pubg_id(message):
    package = user_data[message.from_user.id]["package"]
    pubg_id = message.text

    username = message.from_user.username
    if username:
        username = "@" + username
    else:
        username = "Без username"

    order_text = f"""
🛒 Новый заказ!

👤 Пользователь: {username}
📦 Пакет: {package} UC
🆔 PUBG ID: {pubg_id}
"""

    bot.send_message(ADMIN_ID, order_text)
    bot.send_message(
        message.chat.id,
        "✅ Заказ отправлен администратору.\n\nОжидайте пополнение 💎"
    )

    del user_data[message.from_user.id]

print("Bot started")
bot.infinity_polling()
