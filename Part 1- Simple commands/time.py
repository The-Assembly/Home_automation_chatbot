from telepot.loop import MessageLoop
import telepot, time
from subprocess import *
from time import sleep, strftime
from datetime import datetime

def run_cmd(cmd):
        p = Popen(cmd, shell=True, stdout=PIPE)
        output = p.communicate()[0]
        return output
    
cmd = "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1"

def handle(msg):
   chat_id = msg['chat']['id']
   command = msg['text']
   if (command == '/time'):
       ipaddr = run_cmd(cmd)
       bot.sendMessage(chat_id, datetime.now().strftime('%b %d  %H:%M\n'))
       sleep(2)
      
# Creates a bot using the token provided by BotFather
bot = telepot.Bot('506058190:AAGpSoYzoWI-FbcQXYsZ9tb36tEFoCjt4WE')

# Add the handle function to be called every new received message
MessageLoop(bot,handle).run_as_thread()
print("listening...") 

# Wait for new messages
while 1:
   time.sleep(20)
