import sys
import time
import random
import datetime
import telepot
import os
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)
bot = telepot.Bot('Api Key of your telegram bot')
while True:
   input_state = GPIO.input(4)
   if input_state == False:
       print('button pressed')
       time.sleep(0.2)
       os.system("sudo python /home/pi/tg/camerapy.py") // script used to take the picture. Placed in folder subfiles
       bot.sendMessage(-120421181, text="button camera pressed")
       bot.sendPhoto(-120421181, photo=open('/home/pi/image.jpg', 'rb'))
       os.remove("/home/pi/image.jpg")
   while input_state == False:
           input_state = GPIO.input(4)
	   time.sleep(0.2)
	   

