import random
import telebot
token='7352538828:AAGwT_7rAPmP-y8zk54Wg0ELmaqSUB55wDQ'
bot=telebot.TeleBot(token)
@bot.message_handler(commands = ['start'])
def start_message(message):
    bot.send_message(message.chat.id,random.choice(rando))
rando = ['https://web.telegram.org/k/','ttps://dzen.ru/?clid=2411725&yredirect=true','https://ru.piliapp.com/emoji/list/']
bot.infinity_polling()
