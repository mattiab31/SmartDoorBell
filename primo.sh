#!/bin/bash

while true; do
	sudo hciconfig hci0 reset
	sudo timeout -s SIGINT 10s hcitool -i hci0 lescan >> scanb.txt
	sleep 1
	python /home/pi/search.py
done
