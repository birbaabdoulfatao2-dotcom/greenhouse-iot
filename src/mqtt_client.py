# Client MQTT - Serre Connectée
# Topic : greenhouse/humidity / greenhouse/pump

import paho.mqtt.client as mqtt
import json

BROKER = "localhost"
PORT = 1883

def on_message(client, userdata, message):
    data = json.loads(message.payload.decode())
    print(f"Message reçu : {data}")

client = mqtt.Client()
client.on_message = on_message
client.connect(BROKER, PORT)
client.subscribe("greenhouse/humidity")
client.subscribe("greenhouse/pump")
client.loop_forever()
