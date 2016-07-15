import sys
import os
import telepot

bot = telepot.Bot('Api Key of your telegram bot')
z= 1234
i=0
while 1:
	if i == 3:
		bot.sendMessage(-120421181, text="3 Wrong accesses!")
		os.system("sudo python /home/pi/tg/camerapycode.py") 
		bot.sendPhoto(-120421181, photo=open('/home/pi/imagecode.jpg', 'rb'))
        	os.remove("/home/pi/imagecode.jpg")
		i=0
		break
	x = input ("Insert the secret code!")
	if x == z :
		os.system("sudo python /home/pi/tg/apriporta.py") //script to open the door
		bot.sendMessage(-120421181, text="Qualcuno ha inserito il codice esatto!")
		i=0
		print("eureka")
	else: 
		bot.sendMessage(-120421181, text="Qualcuno ha inserito il codice ERRATO!")
		i=i+1
