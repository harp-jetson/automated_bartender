import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

relay_pins = [27, 22, 23, 24, 25, 5, 6, 16]

for relay in relay_pins:
	GPIO.setup(relay, GPIO.OUT)
	GPIO.output(relay, GPIO.HIGH)
	print(relay)

for test_relay in relay_pins:
	GPIO.output(test_relay, GPIO.LOW)
	time.sleep(1)
	GPIO.output(test_relay, GPIO.HIGH)
	print(test_relay)
