from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

import database
import script
import messages

router = Router()

def add_user(msg):
    if(database.add(msg)):
        messages.log_info(f"<{msg.from_user.id}>"  + messages.consoleAddMessage)
    else:
        messages.log_info(f"<{msg.from_user.id}>" + messages.alreadyInDatabase)

def remove_user(msg):
    if(database.remove(msg)):
        messages.log_info(f"<{msg.from_user.id}>"  + messages.consoleRemoveMessage)
    else:
        messages.log_info(f"<{msg.from_user.id}>"  + messages.userNotFound)
        
@router.message(Command("start")) 
async def start_handler(msg: Message):
    add_user(msg)
    database.set_task(msg, script.generate())
    await msg.reply(script.g_task + " = ?")
    database.set_time(msg)

@router.message()
async def message_handler(msg: Message):
    add_user(msg)
    task = database.get_task(msg)
    
    if not(task == "-"):
        if msg.text == task:
            database.add_point(msg)
            await msg.reply(f"😄 Верно! Молодец :) \n📈 Решено {database.get_points(msg)} пример(-а/-ов)\n{database.result_time(msg)}")
            database.set_task(msg, script.generate())
            await msg.answer(script.g_task + " = ?")
            database.set_time(msg)
        else:
            await msg.reply(f"😫 Неа, неверно :( \n❗ Правильный ответ: {task} \n{database.result_time(msg)}")
            database.set_task(msg, script.generate())
            await msg.answer(script.g_task + " = ?")
            database.set_time(msg)
    else:
        await msg.reply("Пиши /start")