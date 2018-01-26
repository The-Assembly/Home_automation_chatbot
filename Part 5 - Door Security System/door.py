import datetime
from telepot.loop import MessageLoop
import telepot, time
import picamera
import Adafruit_DHT
import RPi.GPIO as GPIO
from RPLCD import CharLCD

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27,GPIO.IN)

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

bot = telepot.Bot('459117877:AAFd9UWpf1Wv2-zL43xyhJs3Aq1TnLHYSpA')

chat_id1 = 433599048 #enter your chat id

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    #print(chat_id)

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
       
  
# Add the handle function to be called every new received message
MessageLoop(bot,handle).run_as_thread()
print("listening...")

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
