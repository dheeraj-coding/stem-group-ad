import RPi.GPIO as gpio
import time
import os
import atexit

gpio.setmode(gpio.BOARD)
LEFT_PIN = 15
RIGHT_PIN = 13
LEFT_IR_PIN = 7
RIGHT_IR_PIN = 10

def setup():
	gpio.setup(LEFT_IR_PIN, gpio.IN)
	gpio.setup(RIGHT_IR_PIN, gpio.IN)
	gpio.setup(RIGHT_PIN, gpio.OUT)
	gpio.setup(LEFT_PIN, gpio.OUT)

def onKill():
	print("Cleaning ports...")
	gpio.cleanup()
	
if __name__ == "__main__":
	atexit.register(onKill)
	setup()
	while True:
		if gpio.input(LEFT_IR_PIN) == 1:
			os.system('clear')
			print("Left Sensor activated")
		if gpio.input(RIGHT_IR_PIN) == 1:
			os.system('clear')
			print("Right Sensor activated")
	
	
