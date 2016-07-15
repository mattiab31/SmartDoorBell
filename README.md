### University of Rome "La Sapienza"
Master of Science in Engineering in Computer Science
Pervasive Systems, a.y. 2015-16
Pervasive Systems Group Project by Marco Casini and Mattia Brunetti


![logodoorbell](https://cloud.githubusercontent.com/assets/17788819/16867680/61f7ab28-4a73-11e6-9513-46ac97008287.jpg)
# Welcome to the SmartDoorbell 

## Finally the complete solution to control your whole entrance with just one click!
SmartDoorbell allows you to

- Communicate with your entrance system simply using telegram app
- Take a photo, record a video, play a sound, record a voice message from the guest to the owner
- Open the door  with freehands, (using beacon)
- Share a code to known people to enter into the house

# Main Idea

## Our idea is to manage basically 3  kinds of possibilities:
- Owner
- Friends
- Strangers

**## The Owner:**
This should be the owner of the house, he can simply enter using a beacon, maybe in his pocket. Using beacon he can simply stay near the door, (50 cm approx) and the door will automatically open, you do not need an app for this!

**## Friends**
The Smartdoorbell has a numeric keypad where you can simply enter the secret code and then you are in! Usefull  if you are chilling with friends and  you're too busy to buy beers instead of opening the door! After the 3 failed login attempts, the keypad control system is shutted down and the owner is alerted 

**## Strangers**
This should be used for any other possible situations. Stranger or people who is not trustworthy can simply press the button,  a photo is automatically taken and sent to the owner via telegram. The owner can play from remote, an audio to inform the guest about something, or  can take a video (30sec) to go deeper. 
If the stranger press the REC button, he can also record an audio message who will be delivered to the owner. 

# Functionalities
Everything runs on a telegram bot, where the owner of the house can communicate just simply typing some special commands as:

- open --> This will simply open the door from remote
- light --> This will just switch on the lihgt. Usefull for garden door or garage door.
- openL--> Open the door + light
- photo --> Simply take a photo using the camera installed on the doorbell. Automatically sent to     the owner via telegram
- video --> Simply record a video of 30 sec from the camera. Automatically sent to the owner via telegram
- sound --> Play a prerecorded  from the doorbell speakers
- reboot --> To reboot the rasberry pi and so the entire system

# Architecture

## Lots of single action scripts, runs on   a Raspberry Pi 2 with raspbian installed. 

**Everything is managed by the telegram bot, which starts at the startup of the system, and there is a python script for all the actions which the system can perform. (codes on the top )**

![schermata 2016-07-15 alle 10 48 09](https://cloud.githubusercontent.com/assets/17788819/16868765/c274674c-4a79-11e6-8fdb-e99e0c2c2837.png)


#  Our timeline

![schermata 2016-07-15 alle 10 53 28](https://cloud.githubusercontent.com/assets/17788819/16868950/bb452514-4a7a-11e6-9a39-73ce64a9359c.png)


#  What you need

This is the list of the exact items that we used. Of course you can use what do you want:


- A raspberry pi 2  --> http://amzn.to/2a32PPd
- A MicroUsb charger for Raspberry pi (2A minimum) --> http://amzn.to/29Bc8Bw
- A microsd card (16 gb minimum) --> http://amzn.to/2a31SGq
- A camera module (usb camera or RPI Cam) --> http://amzn.to/29zLJaU
- Speakers 
- USB Wifi adapter --> http://amzn.to/29HG0kG
- Bluetooth BLE Adapter (this is just for beacon use) --> http://amzn.to/29zLTza
- A multichannel relay --> http://amzn.to/29HGdnO
- A door lock 
- A Lamp
- A USB keypad --> http://amzn.to/29HGgjv
- Breadboard --> http://amzn.to/29IwBnB
- Jumpers and wires plus a bunch of buttons -->http://amzn.to/29IwCIb
- An external audio board for handling the microphone  --> http://amzn.to/29IwLvj
- A beacon (ibeacon or estimote), used to perform the OWNER mode --> 




![schermata 2016-07-15 alle 11 01 53](https://cloud.githubusercontent.com/assets/17788819/16869143/9b1be9c0-4a7b-11e6-81d9-34627682de2a.png)


#  Installations instructions

- Download and install raspbian for raspberry pi
- Set up the Raspberry Pi, Enabling SSH, drivers and updates
- Install python 2.7 or above
- Connect and enabling the PiCamera on Raspberry Pi
- Set up Buttons and realy using jumpers in the breadboards
- Read the code to get familiarity with buttons, GPIO commands, and relay


# WHAT'S MISSING 

Everything works fine. There just some some bugfixiing problems to improve and some new little features that should be developed.

## In progress tasks:

1) An authorization control mechanism for telegram is missing. This means that everyone can communicate to the bot if this is discovered  (really simple to add)
2) There is no way to change the secret code outside the code. This should be impletented dinamically and remotely, using a form to collect data maybe.
3) Beacon broadcast signale range must be settled up to low meters. This means like 80cm because it will open the door everytime the raspberry catch the beacon. Everytime the raspberry catch the beacon, it opens the door, so this means that beacon must stay more than 80cm after used.




# Description of files:

- bottonerec.py --> To record a sound from mic when a button is pressed
- button.py--> The main button, take a picture when is pressed (act as a buzzer)
- code.py-->To unnlock the door with a secure code from keypad 
- mainbot.py-->The Brain of the system. The Telegram Bot. Used  to manage all the actions and interoperate with the owner
- search.py--> To automatically unlock the door when a beacon is catched/detected

# Info & Contacts


You can find us and of course, feel free to contact for any kind of informations:

- Marco Casini : https://it.linkedin.com/in/marcocasini2
- Mattia Brunetti : https://it.linkedin.com/in/mattiabrunetti

Slideshare page: http://www.slideshare.net/MattiaBrunetti/smart-doorbell

Some photos of the project : http://imgur.com/a/iopHl

The project was developed and has been presented within the course of "Pervasive Systems", held by Prof. Ioannis Chatzigiannakis within the Master of Science in Computer Science (MSE-CS), at University of Rome "La Sapienza".






