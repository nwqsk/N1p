import sys
import telebot

import console
import messages 

def quit():
    sys.exit()

def get_token(fileNamePath):
    try:
        f = open(fileNamePath, 'r')
        return f.read()
    except OSError:
        print(messages.errorWhileOpeningFile, fileNamePath)
        quit()

def welcome_message(message):
    bot.send_message(message.chat.id, messages.welcome)
    messages.log_user(message.from_user.first_name, message.text)
    messages.log_bot(messages.welcome)

def create_bot():
    try:
        return telebot.TeleBot(get_token('token.txt'))
    except:
        print(messages.errorWhileCreatingBot)
        quit()

#$
messages.console_log('Запускаем...')

bot = create_bot()
messages.console_log('Бот создан!')

running = True

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_message(message)

while(running):
    command = input('$ ')

    if(command == "quit"):
        running = False
    else:
        messages.console_log(messages.unknownCommand + command)
        bot.poll()
else: 
    bot.stop_bot()
    sys.exit(0)