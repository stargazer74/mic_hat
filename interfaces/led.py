# !/usr/bin/python
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import json
import time
import pixels

TOPIC = "hermes/hotword/jarvis_raspberry-pi/detected"
BROKER_ADDRESS = "smarthome.privat"
PORT = 1883

foo = pixels.Pixels()


def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))
    m_in = json.loads(msg)
    print(m_in["siteId"])
    print("message received: ", msg)
    print("message topic: ", message.topic)
    while True:
        foo.wakeup()
        time.sleep(3)
        foo.off()


def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker: " + BROKER_ADDRESS)
    client.subscribe(TOPIC)


if __name__ == "__main__":
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER_ADDRESS, PORT)

    client.loop_forever()
