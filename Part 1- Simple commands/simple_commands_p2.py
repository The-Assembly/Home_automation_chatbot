#!/usr/bin/python
import datetime
from telepot.loop import MessageLoop
import telepot, time
from emoji import emojize


def handle(msg):
   chat_id = msg['chat']['id']
   command = msg['text']

   if  (command == 'Bye' or command == 'bye'):
            bot.sendMessage(chat_id, emojize('See you later! :v: ', use_aliases=True))

   elif  (command == emojize(':smiley:', use_aliases=True)):
            bot.sendMessage(chat_id, emojize('Cool... ', use_aliases=True))
# Creates a bot using the token provided by BotFather
bot = telepot.Bot('459117877:AAFd9UWpf1Wv2-zL43xyhJs3Aq1TnLHYSpA') #enter your API token

# Add the handle function to be called every new received message
MessageLoop(bot,handle).run_as_thread()
print("listening...")
