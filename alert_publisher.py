import paho.mqtt.client as mqtt
import time

client = mqtt.Client()
client.connect("localhost", 1883)

# Simulate a critical alert after some time
time.sleep(15)
client.publish("alerts/critical", "Overheating detected!", qos=2)
print("Critical alert sent!")
