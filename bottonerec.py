import sys
import time
import random
import datetime
import telepot
import os
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.IN)

bot = telepot.Bot('Api Key of Your Telegram Bot')
while True:
   input_state = GPIO.input(24)
   if input_state == False:
       print('button pressed')
       os.system("sudo omxplayer /home/pi/lasciamessaggio.wav") //file used to play the audio before recording
       os.system("sudo arecord -t wav -d 6 /home/pi/Audio_from_door.wav") //file recorded by the mic
       bot.sendMessage(-120421181, text="button voice pressed")
       bot.sendAudio(-120421181, audio=open('/home/pi/Audio_from_door.wav', 'rb')) //audio is sent to the owner
       os.remove("/home/pi/Audio_from_door.wav")
       GPIO.cleanup()
   while input_state == False:
           input_state = GPIO.input(24) 
	   time.sleep(0.2)   


