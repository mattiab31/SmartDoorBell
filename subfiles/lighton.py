import RPi.GPIO as GPIO
import time
import telepot

bot = telepot.Bot('Your api telegram bot')
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21,GPIO.OUT)
GPIO.output(21,GPIO.HIGH)
bot.sendMessage(-120421181, text="LIGHT ON")
time.sleep(10)
GPIO.output(21,GPIO.LOW)
bot.sendMessage(-120421181, text="LIGHT OFF")
GPIO.cleanup()

