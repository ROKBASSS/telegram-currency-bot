import json
import telebot
from task import task
import markups as m
import sberparser
import vtbparser
import tinkoff
import os


if 'TOKEN' in os.environ:
    TOKEN = 'TOKEN' in os.environ
    print(TOKEN)
    bot = telebot.TeleBot(TOKEN)
else:
    with open('token.json') as file:
        TOKEN = json.load(file)
    print("Bot was started locally...")
    print(TOKEN[0]['token'])
    bot = telebot.TeleBot(TOKEN[0]['token']) 
    print("Token inserted! Working...")

task = task()

@bot.message_handler(commands=['start', 'go', 'help'])
def handle_start(message):
    if not task.isRunning:
        task.isRunning = True
        bot.register_next_step_handler(message, chooseBank)
        return


def chooseBank(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, 'Какой банк вы хотите?',
                           reply_markup=m.start_markup)
    bot.register_next_step_handler(msg, askCurrencies)
    return


def askCurrencies(message):
    chat_id = message.chat.id
    text = message.text.lower()
    if(text == 'сбербанк'):
        msg = bot.send_message(chat_id, 'Какую валюту вы хотите?', reply_markup=m.source_markup)
        bot.register_next_step_handler(msg, getValuesSber)
        return
    elif(text == 'втб'):
        msg = bot.send_message(chat_id, 'Какую валюту вы хотите?', reply_markup=m.source_markup)
        bot.register_next_step_handler(msg, getValuesVtb)
        return
    elif(text == 'тинькофф'):
        msg = bot.send_message(chat_id, 'Какую валюту вы хотите?', reply_markup=m.source_markup)
        bot.register_next_step_handler(msg, getValuesTink)
        return
    else:
        msg = bot.send_message(chat_id, 'Нет такого. Какой банк вы хотите?',reply_markup=m.start_markup)
        bot.register_next_step_handler(msg, askCurrencies)
        return


def getValuesSber(message):
    chat_id = message.chat.id
    text = message.text.lower()
    if text in task.names[0]:
        value = sberparser.getValues("dollar")
        msg = bot.send_message(chat_id, 'Покупается $ по {}, продаётся $ по {}'.format(
            value[0], value[1]), reply_markup=m.source_markup)
        bot.register_next_step_handler(msg, getValuesSber)
        task.isRunning = False
        return
    elif text in task.names[1]:
        value = sberparser.getValues("euro")
        msg = bot.send_message(chat_id, 'Покупается € по {}, продаётся € по {}'.format(
            value[0], value[1]), reply_markup=m.source_markup)
        bot.register_next_step_handler(msg, getValuesSber)
        task.isRunning = False
        return
    elif text == "назад":
        msg = bot.send_message(chat_id, 'Какой банк вы хотите?',
                               reply_markup=m.start_markup)
        bot.register_next_step_handler(msg, askCurrencies)
        return
    else:
        msg = bot.send_message(
            chat_id, 'Такой валюты нет. Выберите корректную валюту')
        bot.register_next_step_handler(msg, getValuesSber)
        task.isRunning = False
        return


def getValuesVtb(message):
    chat_id = message.chat.id
    text = message.text.lower()
    if text in task.names[0]:
        value = vtbparser.getValues("dollar")
        msg = bot.send_message(chat_id, 'Покупается $ по {}, продаётся $ по {}'.format(
            value[0], value[1]), reply_markup=m.source_markup)
        bot.register_next_step_handler(msg, getValuesVtb)
        task.isRunning = False
        return
    elif text in task.names[1]:
        value = vtbparser.getValues("euro")
        msg = bot.send_message(chat_id, 'Покупается € по {}, продаётся € по {}'.format(
            value[0], value[1]), reply_markup=m.source_markup)
        bot.register_next_step_handler(msg, getValuesVtb)
        task.isRunning = False
        return
    elif text == "назад":
        msg = bot.send_message(chat_id, 'Какой банк вы хотите?',
                               reply_markup=m.start_markup)
        bot.register_next_step_handler(msg, askCurrencies)
        return
    else:
        msg = bot.send_message(
            chat_id, 'Такой валюты нет. Выберите корректную валюту')
        bot.register_next_step_handler(msg, getValuesVtb)
        task.isRunning = False
        return


def getValuesTink(message):
    chat_id = message.chat.id
    text = message.text.lower()
    if text in task.names[0]:
        value = tinkoff.getValues("dollar")
        msg = bot.send_message(chat_id, 'Покупается $ по {}, продаётся $ по {}'.format(value[0], value[1]), reply_markup=m.source_markup)
        bot.register_next_step_handler(msg, getValuesTink)
        task.isRunning = False
        return
    elif text in task.names[1]:
        value = tinkoff.getValues("euro")
        msg = bot.send_message(chat_id, 'Покупается € по {}, продаётся € по {}'.format(value[0], value[1]), reply_markup=m.source_markup)
        bot.register_next_step_handler(msg, getValuesTink)
        task.isRunning = False
        return
    elif text == "назад":
        msg = bot.send_message(chat_id, 'Какой банк вы хотите?',reply_markup=m.start_markup)
        bot.register_next_step_handler(msg, askCurrencies)
        return
    else:
        msg = bot.send_message(
            chat_id, 'Такой валюты нет. Выберите корректную валюту')
        bot.register_next_step_handler(msg, getValuesTink)
        task.isRunning = False
        return

# Типы контента
# text, audio, document, photo, sticker,
# video, video_note, voice, location, contact, new_chat_members,
# left_chat_member, new_chat_title, new_chat_photo, delete_chat_photo,
# group_chat_created, supergroup_chat_created, channel_chat_created,
# migrate_to_chat_id, migrate_from_chat_id, pinned_message


bot.enable_save_next_step_handlers(delay=2)
# bot.load_next_step_handlers()
bot.polling()
