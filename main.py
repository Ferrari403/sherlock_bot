#!/usr/bin/env python3
# -*- coding: utf-8 -*-
######### made by Ferarri403
import telebot
import config
import re
import subprocess
import time
from time import sleep


bot = telebot.TeleBot(config.TOKEN)


#реакция бота на команду /start
@bot.message_handler(commands=['start'])
def first_start(message):


    bot.send_message(message.chat.id, "Hello dear users, to launch the bot, write the nickname below (without using @), or use /about\nЗдравствуйте уважаемые пользователи, чтобы запустить бота напишите ниже ник (не используя @) или используйте /about")

    


#реакция бота на команду /about
@bot.message_handler(commands=['about'])
def about(message):

    bot.send_message(message.chat.id, "The bot checks for registration a nickname on all the most popular resources and finds accounts. remember that not only your target can use such a nickname !!!The BOT is not working properly yet and there may be all sorts of bugs. Thanks for your Understanding!\nБот проверяет на наличие регистрации ника на всех самых популярных ресурсах и находит аккаунты. помните, что не только ваша цель может использовать такой ник !!!БОТ еще не до конца исправно работает и могут быть всевозможные баги. Спасибо за Понимаение!")



#бот получает ник цели и обробатывает его в скрипте
@bot.message_handler(content_types=["text"])
def target_func(message):
    global nickname
    global target_result
    nickname = message.text
    #   message_limit(message)
    check_splcharacter(message,nickname)
    

    
#проверка на наличие спецсимволов и отправляет результат скрипта
@bot.message_handler(content_types=["text"])
def check_splcharacter(message,user_nickname):
    specialCharacters = '[@_!#$%^&*()<>?/\|}{~:]'
    string_check = re.compile(specialCharacters)
    if((string_check.search(user_nickname) == None)) & (len(nickname) < 40):
        bot.send_message(message.chat.id, "Please wait... (1-5min)")
        subprocess.call(["python ","sherlock.py " , nickname])
        target_result = open(f"{nickname}.txt")
        bot.send_message(message.chat.id, target_result.read())
    else:
        bot.send_message(message.chat.id,f"Nickname shouldn't contain {specialCharacters} \nand not exceeding 40 characters \nНик не должен содержать {specialCharacters} \nи не привышать 40 символов")




#run
bot.polling(none_stop=True)
