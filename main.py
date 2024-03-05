import telebot
import time

API_TOKEN = '6888317939:AAGMYMAbR5IvZAlAbxDydszn_e3QXUxceVY'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hi, negro. What are you gey?")


@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "/FuckNiggers - fucking niggers \n")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
#@bot.message_handler(func=lambda message: True)
#def echo_message(message):
#    bot.reply_to(message, message.text)


bot.infinity_polling(none_stop=True)