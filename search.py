import os
import time

if '01:17:C5:82:CA:D7' in open ('/home/pi/scanb.txt').read():
	print "OWNER AT HOME"
	os.remove("/home/pi/scanb.txt")
	os.system("sudo python /home/pi/tg/apriporta.py")
else:
	print "Key unfound"
	os.remove("/home/pi/scanb.txt")
