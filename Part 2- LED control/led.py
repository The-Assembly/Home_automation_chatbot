#!/usr/bin/python
import datetime
from telepot.loop import MessageLoop
import telepot, time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 17
GPIO.setup(led,GPIO.OUT)

def handle(msg):
   chat_id = msg['chat']['id']
   command = msg['text']
   if (command == '/lightson'):
       print ('Got command: %s' % command)
       GPIO.output(17,GPIO.HIGH)
       #time.sleep(1)
       bot.sendMessage(chat_id, str("led on"))
       
   elif (command == '/lightsoff'):
       print ('Got command: %s' % command)
       GPIO.output(17,GPIO.LOW)
       #time.sleep(1)
       bot.sendMessage(chat_id, str("led off"))

# Creates a bot using the token provided by BotFather
bot = telepot.Bot('459117877:AAFd9UWpf1Wv2-zL43xyhJs3Aq1TnLHYSpA')

# Add the handle function to be called every new received message
MessageLoop(bot,handle).run_as_thread()
print("listening...") 

# Wait for new messages
while 1:
        time.sleep(20)
