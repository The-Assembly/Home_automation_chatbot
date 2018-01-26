#!/usr/bin/python
import datetime
from telepot.loop import MessageLoop
import telepot, time
import Adafruit_DHT
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

sensor = Adafruit_DHT.DHT11
dht= 23
GPIO.setup(23,GPIO.OUT)

def handle(msg):
   chat_id = msg['chat']['id']
   command = msg['text']
   if (command == '/dht'):
       print ('Got command: %s' % command)
       humidity, temperature = Adafruit_DHT.read_retry(sensor, dht)
       print(humidity)
       bot.sendMessage(chat_id, str('Humidity= %i percent' % humidity))
       bot.sendMessage(chat_id, str('Temperature= %i C' % temperature))

# Creates a bot using the token provided by BotFather
bot = telepot.Bot('459117877:AAFd9UWpf1Wv2-zL43xyhJs3Aq1TnLHYSpA')

# Add the handle function to be called every new received message
MessageLoop(bot,handle).run_as_thread()
print("listening...") 

# Wait for new messages
while 1:
        time.sleep(20)
 
