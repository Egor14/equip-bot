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
    #print(message.text)
    conn = psycopg2.connect(dbname='dfttd1019a6clc', user='pmjdivbrbpkefa',
                            password='0d2581df34fa354b9f6b2b1d0a613e63404d501ee39b2a6fcf3b47e4d0c126ce',
                            host='ec2-54-225-129-101.compute-1.amazonaws.com')
    #print(message.text)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM home_car')
    records = cursor.fetchall()
    bot.reply_to(message, 'Egor')
    #print(records)
    cursor.close()
    conn.close()

    #print(message.text)
    bot.reply_to(message, 'Такой модели нет в наличии')


bot.polling(timeout=60)
