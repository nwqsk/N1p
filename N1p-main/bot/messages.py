# 1. Console
console = "$"

# 1.1. Errors
error = "[!] Ошибка | "
unknownCommand = "Неизвестная команда: "

# 1.1.1. File
errorWhileOpeningFile = error + "Невозможно открыть файл: "
errorWhileCreatingBot = error + "Ошибка при создании бота, убедитесь что в файле есть токен, а также ничего лишнего"

# 1.2. Database


# 1.3. Bot
botPrefix = "Bot"


# 2. Bot
welcome = "Приветствие"
test = "Тестовое сообщение"


# Methods
def console_log(message):
    print(console + " " + message)

def log_bot(message):
    console_log(botPrefix + ": " + message)

def log_user(userName, message):
    console_log(userName + ": " + message)