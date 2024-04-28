# Robocup Symposium 2024
# Test client code written by:
# Pascal Sikorski

import requests
import time

# esp default IP in AP
pico_ip = 'http://192.168.4.1'

def sendMessage(message):
    requests.get(f'{pico_ip}/?message={message}')

userInput = input()
while userInput != "stop":
    sendMessage(userInput)
    userInput = input()