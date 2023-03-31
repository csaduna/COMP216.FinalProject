# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 14:57:39 2023

@author: csadu
"""

# Create subscriber
import paho.mqtt.client as mqtt
import json

def on_message(client, userdata, message):
    data = message.payload.decode('utf-8')
    obj = json.loads(data)
    print(f'Blood Pressure @ Time: {obj["Time"]}')
    print(f'{obj["BloodPressure"]["Diastolic"]}(dia)', end=' ')
    print(f'{obj["BloodPressure"]["Systolic"]}(sys) ')
    
client = mqtt.Client()
client.on_message = on_message
client.connect('localhost', 1883)
client.subscribe('COMP216/test')

while True:
    client.loop_forever()
