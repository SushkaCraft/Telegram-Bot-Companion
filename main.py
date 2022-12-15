import telebot
from cfg import *
from time import sleep


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, 'Привет')
    elif message.text == "Как дела?":
        sleep(5)
        bot.send_message(message.from_user.id, 'Нормально.')

    elif message.text == "Что делаешь?":
        sleep(2)
        bot.send_message(message.from_user.id, 'Ничего.')
    else:
        bot.send_message(message.from_user.id, 'Я тебя не понял.')

bot.infinity_polling()
