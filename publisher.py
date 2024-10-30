import paho.mqtt.client as mqtt
import time
import random

client = mqtt.Client()
client.connect("localhost", 1883)

while True:
    temperature = random.uniform(20, 30)  # Simulated temperature value
    humidity = random.uniform(40, 60)     # Simulated humidity value

    client.publish("sensor/temperature", temperature, qos=0)
    client.publish("sensor/humidity", humidity, qos=1)

    time.sleep(5)
