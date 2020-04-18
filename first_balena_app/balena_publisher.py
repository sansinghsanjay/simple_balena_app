import paho.mqtt.client as mqtt
import random
import time
import os 
import sys
from PIL import Image
from serial import SerialException
import picamera

print("* * * PIL installed and imported successfully * * *")
print("* * * serial / SerialException installed and imported successfully * * *")
print("* * * picamera imported successfully * * *")

# importing the home variable
sys.path.append("/first_balena_app/folder1")
sys.path.append("/first_balena_app/folder1/folder2")

from folder1_script import folder1_function
from folder2_script import folder2_function

folder1_function()
folder2_function()

print("* * * THIS IS THE FINAL RUN * * *")

# camera module
camera = picamera.PiCamera()
camera.capture("/a.jpg")

# create mqtt client object
client = mqtt.Client()

# connect this publisher to the mosquitto broker
client.connect("test.mosquitto.org", 1883, 60)

# publish 30 random values after 2 second interval
for i in range(30):
	# get a random value within 0 and 100
	random_pressure_value = random.randint(0, 100)
	# publish this value
	client.publish("topic/string/sansingh", random_pressure_value)
	# update status
	print(i, ". Sent: ", random_pressure_value)
	# pause execution for 2 seconds
	time.sleep(2)

# disconnect client
client.disconnect()
