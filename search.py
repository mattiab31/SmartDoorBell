import os
import time

if '01:17:C5:82:CA:D7' in open ('/home/pi/scanb.txt').read(): //here, the 01:17:xx:xx:xx:xx reprsent the uuid of the beacon. 
	print "OWNER AT HOME"				     //it basically check in the scanb file, if the beacon have been discovered
	os.remove("/home/pi/scanb.txt")                      //to avoid big increasing of size of the file, it's removed at each opening
	os.system("sudo python /home/pi/tg/apriporta.py")
else:
	print "Key unfound"
	os.remove("/home/pi/scanb.txt")
