# bot.py
'''
from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text('Hola! Soy tu bot de Telegram.')

def main():
    updater = Updater(token='6482190280:AAFWokLhZNBzp4TtNXjg9RGYB_BiF6Zt7eg', use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':main()





'''

from pytgbot import Bot

API_KEY='6482190280:AAFWokLhZNBzp4TtNXjg9RGYB_BiF6Zt7eg'  # change this to the token you get from @BotFather
CHAT='@SwipBot'  # can be a @username or a id, change this to your own @username or id for example.

bot = Bot(API_KEY)

# sending messages:
bot.send_message(CHAT, "Hola Soy el mejor")

# getting events:
for x in bot.get_updates():
    print(x)


'''
import telebot

#CONEXION CON NUESTRO BOT
TOKEN = '6482190280:AAFWokLhZNBzp4TtNXjg9RGYB_BiF6Zt7eg'
bot = telebot.TeleBot(TOKEN)

#COMANDOS SIMPLES START Y HELP
@bot.message_handlers(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Soy una bariable de la libreria')

@bot.message_handlers(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'Puedes intectactuar conmigo')

@bot.message_handlers(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)

if __name__ == "__main":
    bot.polling(none_stop=True)
'''