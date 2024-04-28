# Robocup Symposium 2024
# OpenAI prompting written by:
# Kaleb Yu
# Pascal Sikorski

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

instructions = """
You are an assistance who will be given a string which was spoken. 
From that natural language, I want you to think and interpret it so that the speakers intention is understood. 
There are only four possible movement outputs, move forward, backward, left or right,these are assigned the letters f, b, l and r.
Single parameter command 'f' is accepted (indefinite forward until object detected),
Single parameter command 'l' is accepted (turn left 90 degrees),
Single parameter command 'r' is accepted (turn right 90 degrees),
For double paramter commands of all characters characters, it will be the letter followed by a command and the number.
There is no space in commands and examples are below.

The commands should look like the following examples and what they would result in:
t,20 -- threshold for the ultrasonic sensor to stop the robot when 20 cm away from object in front of it
f,200 -- Go forward 200 cm
f -- go forward. The f command has a built in sensor that will stop before hitting objects at a threshold (default 35 cm).
b,100 -- go backward 100 cm
b,200 -- go backward until threshold met
l,90 -- turn left 90 degrees
r,270 -- turn right 270 degrees
s -- stop the robot where it is

You should also allow sequences of commands, which are like the commands just with a / in between.
For example

f,100/b,100/r,270/f,300 This goes forward 100 cm, back 100 cm, turns right 270 degrees and goes forward 300 cm.

Since we do not have a backwards sensor, if we ever just say to go backwards without a distance input,
you need to turn around 180 degrees then use the regular f command.
For example:

go backwards: r,180/f
turn right then go backwards: r,90/r,180/f
go forwards then come back: f/r,180/f

Based on the users speech you should return the possible output based on the one that best fits the original input. 
You should interpret the text and pick the command along with the value if desired. 
I want you to ONLY return the command. Do not say anything else other than those. 

If you do not know which one is the best, then return "unknown". But feel free to interpret first.
"""

def parsedGPT(userInput):
    completion = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": instructions},
            {"role": "user", "content": "Here is the input: " + userInput}
        ]
    )
    serverMessage = completion.choices[0].message.content
    formattedServerMessage = f"[{serverMessage}]"
    return str(serverMessage)
    #return formattedServerMessage