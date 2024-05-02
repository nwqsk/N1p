# Сообщения

# 1. Консоль
consolePrefix = "Console"

# 1.1. База данных
consoleAddMessage = " добавлен в базу данных"
consoleRemoveMessage = " удален из базы данных"

# 2. Ошибки
errorPrefix = "Ошибка"

# 2.1. Файл
errorWhileOpeningFile = "Невозможно открыть файл: "

# 2.2. База данных
alreadyInDatabase = " уже записан в базу данных"
userNotFound = " не найден"

# 2.3. Бот
botPrefix = "Бот"
errorWhileCreatingBot = "Ошибка при создании бота, убедитесь что в файле есть токен, а также ничего лишнего"

# 3. Сообщения бота
welcome = "Приветствие"
test = "Тестовое сообщение"

userAddMessage = "Вы были добавлены в бд бота"
userRemoveMessage = "Вы были удалены из бд бота"

# Методы
def log_console_command(command):
    print(consolePrefix + ": " + command)

def log_info(text):
    print(text)

def log_bot_message(text):
    print("<" + botPrefix + ">" + ": " + text)

def log_error(errorMessage):
    print(errorPrefix + ": " + errorMessage)

def log_users_message(message):
    print("<" + str(message.chat.id) + ">" + ": " + message.text)
