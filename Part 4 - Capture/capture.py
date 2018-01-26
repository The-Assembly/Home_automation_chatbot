#!/usr/bin/python
import datetime
from telepot.loop import MessageLoop
import telepot, time
import picamera

def handle(msg):
   chat_id = msg['chat']['id']
   command = msg['text']
   if (command == '/capture'):
       camera = picamera.PiCamera()
       print ('Got command: %s' % command)
       camera.capture('img.jpg')
       bot.sendPhoto(chat_id, open('img.jpg'))
       bot.sendMessage(chat_id, str("Picture Captured"))
       camera.close()
       
# Creates a bot using the token provided by BotFather
bot = telepot.Bot('459117877:AAFd9UWpf1Wv2-zL43xyhJs3Aq1TnLHYSpA')

# Add the handle function to be called every new received message
MessageLoop(bot,handle).run_as_thread()
print("listening...") 

# Wait for new messages
while 1:
        time.sleep(20)
