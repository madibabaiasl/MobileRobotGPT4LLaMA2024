# Robocup Symposium 2024
# Send function written by:
# Pascal Sikorski
# Kaleb Yu

import requests
import time

# ESP Default IP in AP
pico_ip = 'http://192.168.4.1'

def send_message(message):
    requests.get(f'{pico_ip}/?message={message}')

"""
userInput = input("Enter something")
while userInput != "stop":
    print("Enter again")
    send_message(userInput)
    userInput = input()
"""