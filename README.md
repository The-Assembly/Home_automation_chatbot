# Home automation with chatbots

## Introduction to Today's Workshop
**OBJECTIVE**: What are chatbots? Why are they such a big opportunity? How do they work? How can I build one? How can I meet other people interested in chatbots?<br/>

A chatbot is a service, powered by rules and sometimes artificial intelligence, that you interact with via a chat interface. The service could be any number of things, ranging from functional to fun, and it could live in any major chat product (Facebook Messenger, Slack, Telegram, Text Messages, etc.). Fun fact- One of the first bot that were created and tested was <a href="https://en.wikipedia.org/wiki/ELIZA"> Eliza </a>and dates all the way to the 1960's.  

#### Examples of Chatbots
- <a href="https://m.me/hiponcho"> Weather bot </a> : Get the weather whenever you ask.
- <a href="https://www.meetcleo.com/"> News bot  </a>: Ask it to tell you when ever something interesting happens.
- <a href="https://www.woebot.io/"> Therapist bot <a/>: I’ll tell it my problems and it helps me think of solutions.
- <a href="https://www.meetcleo.com/"> Personal finance bot </a>: It helps me manage my money better.
- <a href="https://x.ai/"> Scheduling bot </a>: Get me a meeting with someone on the Messenger team at Facebook.
- <a href="http://www.msxiaoice.com/"> A bot that’s your friend </a>: In China there is a bot called Xiaoice, built by Microsoft, that over 20 million people talk to.
- <a href="http://www.boibot.com/en/index.html/"> Boibot/Evie </a>: Moving avatars built using Adobe Flash and Existor Avatar Player. They figure out what to say using AI software created by Rollo Carpenter and Existor, the same software holding text conversations at Cleverbot. The avatars also feature a text-to-speech engine, and display emotional responses to what you say that were learned from real people <br/> 
  
The Flow diagram below provides as simple guide as to how we will be conducting the workshop.<br/>

![flow diagram](https://user-images.githubusercontent.com/32713072/35462640-3dea1b4c-0306-11e8-822a-243b52013281.jpg)


For the circuit diagram, use the image below as a guide.<br/>
![chatbot_circuit_ Diagram](https://user-images.githubusercontent.com/32713072/35446659-dcfb9536-02ce-11e8-936b-d2365057543c.jpg)

## Setting up a Telegram account 
This API allows you to connect bots to our system. Telegram Bots are special accounts that do not require an additional phone number to set up. These accounts serve as an interface for code running somewhere on your server.
- First install the app for either Windows/MacOS ,Android or any platform (https://telegram.org/).
- After installation open the app, you will be asked to enter your **Location** and **Mobile number** with the correct country code
- After your enter those details you will recieve and *SMS* and a *missed call* (With a counter counting down from 2 minutes)
- Enter your **First name** and **Last name**
- You have successfully registered.  

## Making a bot through Telegram
At the core, Telegram Bots are special accounts that do not require an additional phone number to set up. <br/>
Sending messages and commands to bots by opening a chat with them or by adding them to groups. This is useful for chat bots or news bots like the official TechCrunch bot.
- After Registering, go to the Search icon
- Search for **BotFather** and press **Start**
- Next, you will get a list of commands you can use to set up different variants/mods for your bot.
- Type **/newbot** on the text box
- Choose a name for your bot, and type it 
- Next, select a username for the bot (eg: Assembly_bot)
- After typing the username, you will recieve an API key from BotFather, something of this form **123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ**
- go to https://api.telegram.org/bot<token>/getMe to get the following info:<br/>
  
![setup](https://user-images.githubusercontent.com/32713072/35451193-e280ae44-02db-11e8-8058-e36f765d2ed3.jpg)

- you can type **/setcommands** to set the commands which would showup as a list, whenever you type "/" on the text box.
- Similarly you can follow the text message that you initially got, which consists a list of all the commands to manage your telegram bot.

## Installing the Libraries
To enable the functionalities of all the different functions we will be using on python, certain libraries need to be installed to enable the use of these "functionalities". 

### Pi camera
```python-picamera``` is a pure Python interface to the Raspberry Pi camera module for Python 2.7 (or above) or Python 3.2 (or above). The library is written and maintained by Dave Jones.

#### Enable the camera <br/>

Run ```sudo raspi-config``` and choose in the menu to enable the pi camera. A reboot is needed after this.

#### Installation

The ```python-picamera``` library is available in the Raspbian archives. Install with ```apt```:
- sudo apt-get update
- sudo apt-get install python-picamera

Alternatively, the Python3 package is installed with  
- sudo apt-get install python3-picamera

#### Taking an image 

First, at the Python prompt or at the top of a Python script, enter: <br/>
```import picamera```

This will make the library available to the script. Now create an instance of the PiCamera class: <br/>
```camera = picamera.PiCamera()```

And take a picture: <br/>
```camera.capture('image.jpg')```

**FOR MORE INFO: https://www.raspberrypi.org/documentation/usage/camera/python/README.md** <br/>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;&nbsp;  **http://picamera.readthedocs.io/en/release-1.13/**


### Install Python 3 and PIP
Usually Python3 is pre-installed when you install Raspbian on your Raspberry PI. 

But, not all Python packages are available in the Raspbian archives, and those that are can sometimes be out-of-date. If you can't find a suitable version in the Raspbian archives, you can install packages from the Python Package Index (PyPI). To do so, use the pip tool.

**Pip** is installed by default in Raspbian Jessie (but not Raspbian Wheezy or Jessie Lite). You can install it with apt:

-sudo apt-get install python3-pip

### DHT library 
Python library to read the DHT series of humidity and temperature sensors on a Raspberry Pi or Beaglebone Black. <br/>
Designed specifically to work with the Adafruit DHT series sensors ----> https://www.adafruit.com/products/385 <br/>
Currently the library is only tested with Python 2.6/2.7. <br/>

#### Installation
- git clone https://github.com/adafruit/Adafruit_Python_DHT.git
- cd Adafruit_Python_DHT
- sudo apt-get install build-essential python-dev python-openssl
- sudo python setup.py install

### RPLCD library
A Python 3/2 Raspberry PI Character LCD library for the Hitachi HD44780 controller. It supports both GPIO (parallel) mode as well as boards with an I2C port expander (e.g. the PCF8574 or the MCP23008).<br/>
This library is inspired by Adafruit Industries' CharLCD library as well as by Arduino's LiquidCrystal library. <br/>
No external dependencies (except the ```RPi.GPIO``` library, which comes preinstalled on Raspbian) are needed to use this library. <br/>

#### Installation 
- sudo pip install RPLCD

#### Alternative library Installation
- apt-get install git
- git clone git://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code.git
- cd Adafruit-Raspberry-Pi-Python-Code
- cd Adafruit_CharLCD

**FOR MORE INFO: http://rplcd.readthedocs.io/en/stable/** <br/>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;&nbsp; **https://learn.adafruit.com/character-lcd-with-raspberry-pi-or-beaglebone-black/wiring**

### Telepot 
Telepot helps you build applications for Telegram Bot API. It works on Python 2.7 and Python 3. For Python 3.5+, it also has an async version based on asyncio.

#### Installation 
**pip:**
- pip install telepot
- pip install telepot --upgrade  

**easy_install:** 
- easy_install telepot
- easy_install --upgrade telepot 

#### Get a token
To use the Telegram Bot API, you first have to get a bot account by chatting with BotFather.<br/>
BotFather will give you a token, something like <b>123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ </b>. With the token in hand, you can start using telepot to access the bot account.

#### Test the account
On a python script type: <br/>
```
import telepot
bot = telepot.Bot('***** PUT YOUR TOKEN HERE *****')
bot.getMe()
{'first_name': 'Your Bot', 'username': 'YourBot', 'id': 123456789} ## go to https://api.telegram.org/bot<token>/getMe to get the following info
```
**FOR MORE INFO: https://github.com/nickoala/telepot** <br/>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;&nbsp;  **https://gist.github.com/iliakonnov/05e1bf2e36b77baa317604528f0fc983**

### Emoji library
The entire set of Emoji codes as defined by the unicode consortium is supported in addition to a bunch of aliases. By default only the official list is enabled but doing ```emoji.emojize(use_aliases=True)``` enables both the full list and aliases.

#### Installation
**pip:**
- pip install emoji --upgrade

**Alternative Installation** 
- git clone https://github.com/carpedm20/emoji.git
- cd emoji
- python setup.py install

#### Example 
**On a python script:** 
```
import emoji
print(emoji.emojize('Python is :thumbs_up_sign:'))
print(emoji.emojize('Python is :thumbsup:', use_aliases=True))
```
**On the prompt:** <br/>
Python is 👍<br/>
Python is 👍<br/>

**FOR MORE INFO: https://github.com/python-telegram-bot/python-telegram-bot/wiki/Emoji** <br/>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;&nbsp; **https://github.com/python-telegram-bot/python-telegram-bot/wiki/Emoji** <br/>

**EMOJI CHEAT SHEET:  https://www.webpagefx.com/tools/emoji-cheat-sheet/**

### Setting up the GPIO pins on a Raspberry PI
The newest version of Raspbian has the RPi.GPIO library pre-installed. You’ll probably need to update your library, so using the command line, run:
- sudo apt-get install rpi.gpio
If it isn’t already installed it will be installed. If it is already installed it will be upgraded if a newer version is available.
#### Using the RPi.GPIO Library
Now that you’ve got the package installed and updated, let’s take a look at some of the functions that come with it. Open the Leafpad text editor and save your sketch as “myInputSketch.py”. From this point forward, we’ll execute this script using the command line:

- sudo python myInputSketch.py

All of the following code can be added to this same file. Remember to save before you run the above command. To exit the sketch and make changes, press Ctrl+C.

To add the GPIO library to a Python sketch, you must first import it: <br/>
```python
import RPi.GPIO as GPIO
```

Then we need to declare the type of numbering system we’re going to use for our pins: <br/>
```python
#set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)
#setup GPIO using Board numbering
GPIO.setmode(GPIO.BOARD)
```
#### Examples: 
https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins <br/>
https://www.raspberrypi-spy.co.uk/2012/05/install-rpi-gpio-python-library/

### Setting up the program to run on terminal, after boot
A simple way to see how you can setup to run python file on Raspberry Pi startup (using the terminal).

- Save the python file on home/pi
- On the terminal, navigate to  /home/pi
- now open a hidden file  .bashrc  ( type "sudo nano .bashrc" on terminal and press enter)
- At the end of the file type "python" followed by your file name (eg: python3 speechtotext)
- If you want the terminal to revert back to its normal format, either comment out the command on the .bashrc file or remove it (you can access the bash file in /home/pi).




