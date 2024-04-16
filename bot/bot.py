import sys
import telebot

#===[ Cообщения ]===

#Консольные
botName = "bot"

##Ошибки
error = "[!] Ошибка | "
errorWhileOpeningFile = error + "Невозможно открыть файл: "
errorWhileCreatingBot = error + "Ошибка при создании бота, убедитесь что в файле есть токен, а также ничего лишнего"

##Основные
welcome = "Приветствие"
test = "Тестовое сообщение"


#===[ Чтение файлов ]===

##Получение токена
def get_token(fileNamePath):
    try:
        f = open(fileNamePath, 'r')
        return f.read()
    except OSError:
        print(errorWhileOpeningFile, fileNamePath)
        quit()

#=== [ Основные методы ]===

#Консоль

##Логи
def log_bot(text):
    print(botName + ": " + text)

def log_user(message):
    print(str(message.chat.id) + ": " + message.text)

#Выключение
def quit():
    sys.exit()

#===[ Бот в тг ]===

# Приветствие
def welcome_message(message):
    bot.send_message(message.chat.id, welcome)
    log_user(message)
    log_bot(welcome)

# Подключение к боту в Telegram
def create_bot():
    try:
        return telebot.TeleBot(get_token("token.txt"))
    except:
        print(errorWhileCreatingBot)
        quit()

#======[ Старт программы]======
bot = create_bot()

# Приветствие бота
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_message(message)

# Тестовое сообщение
@bot.message_handler(func=lambda m: True)
def send_test(message):
    bot.send_message(message.chat.id, test)
    log_user(message)
    log_bot(test)

bot.infinity_polling()
