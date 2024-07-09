import telebot
a = 3,141592653589793
token='7219252695:AAHbHypk0Txi8jQ23fCGERxR6IGqMhd4dY8'
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, f'{a} число пи')
bot.infinity_polling()
