# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 17:01:42 2023

@author: csadu
"""

#Create publisher
import time
import paho.mqtt.client as mqtt
import json

my_data = {
    'Time': time.asctime(),
    'HeartRate': 80,
    'RespiratoryRate': 12,
    'HeartRateVariability':65,
    'BodyTemperature': 99.08339,
    'BloodPressure': {
        'Systolic': 105,
        'Diastolic': 70}
    ,
    'Activity': 'Walking'
}

client = mqtt.Client()
client.connect('localhost', 1883)

client.loop_start()
time.sleep(1)
for x in range(10):
    my_data['Time'] = time.asctime()
    client.publish('COMP216/test', json.dumps(my_data))
    print('Message sent')
    time.sleep(15)
    
client.loop_stop()
