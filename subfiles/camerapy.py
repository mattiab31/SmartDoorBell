import picamera
camera = picamera.PiCamera()
camera.capture('/home/pi/image.jpg')
camera.vflip = True
