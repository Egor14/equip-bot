import telebot
import psycopg2
from telebot.types import Message

TOKEN = '896316693:AAE20bxKggrR7ZvXOXySh8gVBgweMmKhVkA'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Пришли мне фотографию и жди результата!")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    conn = psycopg2.connect(dbname='dfttd1019a6clc', user='pmjdivbrbpkefa',
                            password='0d2581df34fa354b9f6b2b1d0a613e63404d501ee39b2a6fcf3b47e4d0c126ce',
                            host='ec2-54-225-129-101.compute-1.amazonaws.com')

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM home_car WHERE model = %s', (message.text,))
    if len(cursor) > 0:
        for row in cursor:
            s = ''
            for i in row:
                s += str(i) + '\n'
            bot.reply_to(message, s)
    else:
        bot.reply_to(message, 'К сожалению, данной модели нет в наличии')
    cursor.close()
    conn.close()


bot.polling(timeout=60)
