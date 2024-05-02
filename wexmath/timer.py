import time

def current():
    return str(time.time())

def format(value):
    days = value // (24 * 3600)
    value = value % (24 * 3600)
    hours = value // 3600
    value %= 3600
    minutes = value // 60
    value %= 60
    seconds = value
    return "🕑 Затраченное время: " + str(seconds//1)[:-2] + " секунд(-ы) " + str(minutes//1)[:-2] + " минут(-ы) " + str(hours//1)[:-2] + " час(-ов) " + str(days)[:-2] + " дня(-ей)"

def count(value):
    return format((float(current()) - value)//1)
    