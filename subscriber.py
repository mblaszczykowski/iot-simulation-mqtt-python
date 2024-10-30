import paho.mqtt.client as mqtt
import requests

API_URL = "http://localhost:8000/items"

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker")
    client.subscribe("sensor/temperature", qos=0)
    client.subscribe("sensor/humidity", qos=1)
    client.subscribe("alerts/critical", qos=2)

def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode()
    print(f"Received message: {topic} - {payload}")

    if topic == "sensor/temperature":
        item_id = 2
        item = {
            "id": item_id,
            "name": "Temperature Sensor",
            "value": float(payload)
        }
    elif topic == "sensor/humidity":
        item_id = 3
        item = {
            "id": item_id,
            "name": "Humidity Sensor",
            "value": float(payload)
        }
    elif topic == "alerts/critical":
        print("Critical alert received!")
        return
    else:
        return

    # Check if item exists
    response = requests.get(f"{API_URL}/{item_id}")

    if response.status_code == 200:
        # Item exists, update it
        response = requests.put(f"{API_URL}/{item_id}", json=item)
        if response.status_code == 200:
            print(f"Updated item in API: {item}")
        else:
            print(f"Failed to update item: {response.status_code}")
    elif response.status_code == 404:
        # Item does not exist, create it
        response = requests.post(API_URL, json=item)
        if response.status_code == 200:
            print(f"Created new item in API: {item}")
        else:
            print(f"Failed to create item: {response.status_code}")
    else:
        print(f"Error checking item existence: {response.status_code}")

client = mqtt.Client(protocol=mqtt.MQTTv311)
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883)
client.loop_forever()
