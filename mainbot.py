import sys
import time
import random
import datetime
import telepot
import os

time.sleep(30)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    if command == '/roll':
        bot.sendMessage(chat_id, random.randint(1,6))
    elif command == '/time':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))
    elif command == '/photo':
        os.system("sudo python /home/pi/tg/camerapy.py")
        bot.sendPhoto(chat_id, photo=open('/home/pi/image.jpg', 'rb'))
        os.remove("/home/pi/image.jpg")
    elif command == '/video':
        os.system("sudo python /home/pi/tg/videopy.py")
        bot.sendVideo(chat_id, video=open('/home/pi/video.h264','rb'))
	os.remove("/home/pi/video.h264")
    elif command == '/sound':
	os.system("omxplayer /home/pi/rec.mp3")
	bot.sendAudio(chat_id, audio=open('/home/pi/rec.mp3','rb'))
    elif command == '/open':
        os.system("sudo python /home/pi/tg/apriporta.py")
    elif command == '/openL':	
	os.system("sudo python /home/pi/tg/doorlight.py")
    elif command == '/light':
	os.system("sudo python /home/pi/tg/lighton.py")
    elif command == '/help':
	bot.sendDocument(chat_id, document=open('/home/pi/command.doc','rb'))
    elif command == '/rec':
	os.system("sudo arecord -t wav -d 5 /home/pi/mon.wav")
	bot.sendAudio(chat_id, audio=open('/home/pi/mon.wav','rb'))
	os.remove("/home/pi/mon.wav")
    elif command == '/reboot':
	os.system("sudo reboot")
	bot.sendMessage(chat_id, text="...DoorBell reboot!")
    elif command == '/shutdown':
        os.system("sudo shutdown -h now")
        bot.sendMessage(chat_id, text="DoorBell is down!")
bot = telepot.Bot('153736884:AAGY5qfwDcQE21HCYWY1JftScSYWAv7Lqo8')
bot.message_loop(handle)
print 'I am listening ...'
bot.sendMessage(-120421181, text="Welcome to DoorBell")

while 1:
    time.sleep(10)

