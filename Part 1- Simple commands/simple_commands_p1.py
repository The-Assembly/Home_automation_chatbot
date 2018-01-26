#!/usr/bin/python
import datetime
from telepot.loop import MessageLoop
import telepot, time


def handle(msg):
   chat_id = msg['chat']['id']
   command = msg['text']

   if (command == '/start'):
            bot.sendMessage(chat_id, str("Hello, Welcome to the Assembly ChatBot Workshop"))

   elif  (command == 'Hello' or command == 'Hi' or command == 'Hey'):
            bot.sendMessage(chat_id, emojize('Hello, Welcome to the Assembly ChatBot Workshop :smiley: ', use_aliases=True))

   elif  (command == 'How are you' or command == 'how r u'):
            bot.sendMessage(chat_id, str("Great, thank you "))


# Creates a bot using the token provided by BotFather
bot = telepot.Bot('459117877:AAFd9UWpf1Wv2-zL43xyhJs3Aq1TnLHYSpA') #enter your API token

# Add the handle function to be called every new received message
MessageLoop(bot,handle).run_as_thread()
print("listening...")
