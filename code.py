import sys
import os
import telepot

bot = telepot.Bot('153736884:AAGY5qfwDcQE21HCYWY1JftScSYWAv7Lqo8')
z= 1234
i=0
while 1:
	if i == 3:
		bot.sendMessage(-120421181, text="3 inserimenti errati")
		os.system("sudo python /home/pi/tg/camerapycode.py")
		bot.sendPhoto(-120421181, photo=open('/home/pi/imagecode.jpg', 'rb'))
        	os.remove("/home/pi/imagecode.jpg")
		i=0
		break
	x = input ("Immetti codice")
	if x == z :
		os.system("sudo python /home/pi/tg/apriporta.py")
		bot.sendMessage(-120421181, text="Qualcuno ha inserito il codice esatto!")
		i=0
		print("eureka")
	else: 
		bot.sendMessage(-120421181, text="Qualcuno ha inserito il codice ERRATO!")
		i=i+1
