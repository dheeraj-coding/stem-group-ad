import RPi.GPIO as gpio
import time
import atexit

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
LEFT_PIN = 13
RIGHT_PIN = 15
LEFT_IR_PIN = 7
RIGHT_IR_PIN = 10

def leftOn():
	gpio.output(LEFT_PIN, 1)

def leftOff():
	gpio.output(LEFT_PIN, 0)

def rightOn():
	gpio.output(RIGHT_PIN, 1)

def rightOff():
	gpio.output(RIGHT_PIN, 0)
	
def stopAll():
	gpio.output(LEFT_PIN, 0)
	gpio.output(RIGHT_PIN, 0)

def setup():
	gpio.setup(LEFT_IR_PIN, gpio.IN)
	gpio.setup(RIGHT_IR_PIN, gpio.IN)
	gpio.setup(RIGHT_PIN, gpio.OUT)
	gpio.setup(LEFT_PIN, gpio.OUT)

def onExit():
	leftOff()
	rightOff()
	gpio.cleanup()
	
if __name__ == "__main__":
	atexit.register(onExit)
	setup()
	while True:
		if gpio.input(LEFT_IR_PIN) == 1 and gpio.input(RIGHT_IR_PIN) == 1:
			print("Straight")
			leftOn()
			rightOn()
		if gpio.input(LEFT_IR_PIN) == 0 and gpio.input(RIGHT_IR_PIN) == 0:
			leftOff()
			rightOff()
			print("Stop")
		if gpio.input(LEFT_IR_PIN) == 0 and gpio.input(RIGHT_IR_PIN) == 1:
			leftOff()
			rightOn()
			print("Left")
		if gpio.input(LEFT_IR_PIN) == 1 and gpio.input(RIGHT_IR_PIN) == 0:
			leftOn()
			rightOff()
			print("Right")
	gpio.cleanup()
	
	
