#!/usr/bin/python
import datetime
from telepot.loop import MessageLoop
import telepot, time
import picamera
import Adafruit_DHT
import RPi.GPIO as GPIO
from emoji import emojize
from subprocess import *
from time import sleep, strftime
from datetime import datetime
from RPLCD import CharLCD

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(27,GPIO.IN)
sensor = Adafruit_DHT.DHT11
pin = 23

GPIO.setup(2, GPIO.OUT)
pwm=GPIO.PWM(2, 50)
pwm.start(0)

def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(2, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(2, False)
	pwm.ChangeDutyCycle(0)

lcd = CharLCD(cols=16, rows=2, pin_rs=26, pin_e=19, pins_data=[13, 6, 5, 11])

def run_cmd(cmd):
        p = Popen(cmd, shell=True, stdout=PIPE)
        output = p.communicate()[0]
        return output
    
cmd = "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1"

chat_id1 = 433599048 #enter your chat id

def handle(msg):
   chat_id = msg['chat']['id']
   command = msg['text']
   print (chat_id)
   
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

   elif (command == '/time'):
       ipaddr = run_cmd(cmd)
       bot.sendMessage(chat_id, datetime.now().strftime('%b %d  %H:%M\n'))
       sleep(2)

   elif (command == '/door'):
    print ('Got command: %s' % command)
    while True:
        input_state = GPIO.input(27)
        if (input_state == False):
           print('Button Pressed')
           time.sleep(0.2)
           bot.sendMessage(chat_id, str("Someone's at the door..."))
           camera = picamera.PiCamera()
           camera.capture('img2.jpg')
         
           bot.sendPhoto(chat_id, open('img2.jpg'))
           bot.sendMessage(chat_id, str("See who is at the door"))
           camera.close()
           bot.sendMessage(chat_id, str("Type '/yes' to open the door or '/no' for them to come back later"))
           
        else:
           continue
        
   if (command == '/yes'):
      lcd.clear()
      print ('Got command: %s' % command)
      SetAngle(0)
      bot.sendMessage(chat_id, str('Door is now open...'))
      lcd.write_string(u'Open!')
      sleep(5)
      SetAngle(180)

   elif (command == '/no'):
       lcd.clear()
       print ('Got command: %s' % command)
       bot.sendMessage(chat_id, str('Please come back later...'))
       lcd.write_string(u'Please come back later...')
       
       
   elif (command == '/dht'):
       print ('Got command: %s' % command)
       humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
       print(humidity)
       bot.sendMessage(chat_id, str('Humidity= %i Percent' % humidity))
       bot.sendMessage(chat_id, str('Temperature= %i C' % temperature))
       
   elif (command == '/capture'):
       camera = picamera.PiCamera()
       print ('Got command: %s' % command)
       camera.capture('img.jpg')
       bot.sendPhoto(chat_id, open('img.jpg'))
       bot.sendMessage(chat_id, str("Picture Captured"))
       camera.close()
                  
   elif  (command == '/start'):
            bot.sendMessage(chat_id, str("Hello, Welcome to the Assembly ChatBot Workshop"))

   elif  (command == 'Hello' or command == 'Hi' or command == 'Hey'):
            bot.sendMessage(chat_id, emojize('Hello, Welcome to the Assembly ChatBot Workshop :smiley: ', use_aliases=True))

   elif  (command == 'How are you' or command == 'how r u'):
            bot.sendMessage(chat_id, str("Great, thank you "))

   elif  (command == 'Bye' or command == 'bye'):
            bot.sendMessage(chat_id, emojize('See you later! :v: ', use_aliases=True))

   elif  (command == emojize(':smiley:', use_aliases=True)):
            bot.sendMessage(chat_id, emojize('Cool... ', use_aliases=True))
   else:
      bot.sendMessage(chat_id, str("Please type '/' to view available commands"))

# Creates a bot using the token provided by BotFather
bot = telepot.Bot('459117877:AAFd9UWpf1Wv2-zL43xyhJs3Aq1TnLHYSpA') #enter your API token

# Add the handle function to be called every new received message
MessageLoop(bot,handle).run_as_thread()
print("listening...")

# Wait for new messages
while 1:
        input_state = GPIO.input(27)
        if (input_state == False):
           print('Button Pressed')
           time.sleep(0.2)
           bot.sendMessage(chat_id1, str("Someone's at the door..."))
           camera = picamera.PiCamera()
           camera.capture('img2.jpg')
         
           bot.sendPhoto(chat_id1, open('img2.jpg'))
           bot.sendMessage(chat_id1, str("See who is at the door"))
           camera.close()
           bot.sendMessage(chat_id1, str("Type '/yes' to open the door or '/no' for them to come back later"))
           
        else:
           continue
        time.sleep(20)
 
