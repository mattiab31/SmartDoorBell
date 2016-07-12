import RPi.GPIO as GPIO
import time
import telepot

bot = telepot.Bot('153736884:AAGY5qfwDcQE21HCYWY1JftScSYWAv7Lqo8')
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21,GPIO.OUT)
GPIO.output(21,GPIO.HIGH)
bot.sendMessage(-120421181, text="LIGHT ON")
time.sleep(10)
GPIO.output(21,GPIO.LOW)
bot.sendMessage(-120421181, text="LIGHT OFF")
GPIO.cleanup()

