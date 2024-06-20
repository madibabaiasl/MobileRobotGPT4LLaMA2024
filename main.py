# Main controller written by:
# Kaleb Yu
# Pascal Sikorski

from speechToText import speechToText
from llmapi import parsedGPT
import httpsend

if __name__ == "__main__":
    while True:
        userInput = speechToText()
        if userInput is None:
            break
        serverRecieved = parsedGPT(userInput)
        print(serverRecieved)
        httpsend.send_message(serverRecieved)
        #confirm = input("Enter y/n for confirmation")
        #if confirm == 'y':
        #    httpsend.send_message(serverRecieved)

        print(serverRecieved, "Just sent")
