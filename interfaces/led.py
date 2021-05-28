# !/usr/bin/python
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import json
import time
import pixels

TOPIC_TTS = "hermes/tts/#"
TOPIC_HOTWORD = "hermes/hotword/#"
BROKER_ADDRESS = "smarthome.privat"
PORT = 1883
SIDE_ID = "MY_SITE_ID"

led = pixels.Pixels()


def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))
    m_in = json.loads(msg)
    side_id = m_in["siteId"]
    if side_id == SIDE_ID:
        print("message topic = ", message.topic)
        if message.topic == "hermes/hotword/jarvis_raspberry-pi/detected":
            led.wakeup()
            led.think()
            time.sleep(3)
            led.off()
        if message.topic == "hermes/tts/say":
            led.speak()
        if message.topic == "hermes/tts/sayFinished":
            led.off()


def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker: " + BROKER_ADDRESS)
    client.subscribe([(TOPIC_TTS, 0), (TOPIC_HOTWORD, 0)])


if __name__ == "__main__":
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER_ADDRESS, PORT)

    client.loop_forever()
