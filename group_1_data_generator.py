# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 17:52:08 2023

@author: marte
"""


humidity = float(input("Enter humidity level between 0 and 100: "))
if humidity <= 20:
    print("The humidity is Uncomfortably dry")
elif humidity <= 60:
    print("The humidity is at a comfortable range")
elif humidity <= 100:
    print("The humidity is Uncomfortably wet")
else:
    print("Invalid humidity value")
print("----------------------------------------------------------------------")
temperature = float(input("Enter a Target Outdoor Temperature between -20 and 20: "))

if int(temperature) in range(-21,-15):
    print("The temperature is extremely cold, there is a risk of developing frost bite")
elif int(temperature) in range(-14, -10):
    print("The temperature is very cold, wear appropriate clothing")
elif int(temperature) in range(-9,-5):
    print("The temperature is fairly cold outside")
elif int(temperature) in range(-4,-1):
    print("The temperature slightly below freezing, watch out for frozen bodies of water")
elif temperature == 0:
    print("The temperature is at the freezing mark")
elif int(temperature) in range(1,5):
    print("The temperature is cool outside")
elif int(temperature) in range(6,10):
    print("The temperature is mild outside")
elif int(temperature) in range(10,15):
    print("The temperature is comfortable outside")
elif int(temperature) in range(15,21):
    print("The temperature is very nice outside, suitable for outdoor activities")
else:
    print("Invalid temperature value")
print("----------------------------------------------------------------------")

print("Random Humidity Generator")
    
import random

humidity_level = random.randint(0, 100)

if humidity_level <= 20:
    print("Uncomfortably Dry")
elif humidity_level <= 60:
    print("Comfortable")
else:
    print("Uncomfortably Wet")
print("----------------------------------------------------------------------")
print("Random Temperature Generator")
temperature2 = random.randint(-21, 21)

if int(temperature2) in range(-21,-15):
    print("The temperature is extremely cold, there is a risk of developing frost bite")
elif int(temperature2) in range(-14, -10):
    print("The temperature is very cold, wear appropriate clothing")
elif int(temperature2) in range(-9,-5):
    print("The temperature is fairly cold outside")
elif int(temperature2) in range(-4,-1):
    print("The temperature slightly below freezing, watch out for frozen bodies of water")
elif temperature2 == 0:
    print("The temperature is at the freezing mark")
elif int(temperature2) in range(1,5):
    print("The temperature is cool outside")
elif int(temperature2) in range(6,10):
    print("The temperature is mild outside")
elif int(temperature2) in range(10,15):
    print("The temperature is comfortable outside")
elif int(temperature2) in range(15,21):
    print("The temperature is very nice, suitable for outdoor activities")
else:
    print("Invalid temperature value")
