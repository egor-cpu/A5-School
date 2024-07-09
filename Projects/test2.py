
import telebot
import random
token = '7497751318:AAFg9iHx12G0_i-dFYxxk9K7OB8dZD46__I'
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start', 'mes'])
def start_message(m):
    bot.send_message(m.chat.id,'3.141592653')
bot.infinity_polling()
