import telebot
import psycopg2
from telebot.types import Message

TOKEN = '896316693:AAE20bxKggrR7ZvXOXySh8gVBgweMmKhVkA'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Напиши мне номер модели, и ты получишь всю необходимую информацию\n" +
                 "Если же ты хочешь добавить свою технику в нашу базу для быстрого поиска клиентов, то сделать это можно по ссылке: " +
                 "https://beta-equipment.herokuapp.com")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    conn = psycopg2.connect(dbname='dfttd1019a6clc', user='pmjdivbrbpkefa',
                            password='0d2581df34fa354b9f6b2b1d0a613e63404d501ee39b2a6fcf3b47e4d0c126ce',
                            host='ec2-54-225-129-101.compute-1.amazonaws.com')

    cursor = conn.cursor()
    cursor.execute(
        'SELECT home_dealer.name, home_dealer.phone_number, home_car.model, home_car.year, home_car.city, home_car.count FROM home_car, home_dealer WHERE home_car.user_id = home_dealer.id AND model = %s',
        (message.text,))
    s = ''
    for row in cursor:
        s = ''
        for i in row:
            s += str(i) + '\n'
        bot.reply_to(message, s)
    if s == '':
        bot.reply_to(message, 'К сожалению, данной модели нет в наличии')
    cursor.close()
    conn.close()


bot.polling(timeout=60)
