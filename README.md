# Deployment of Large Language Models to Control Mobile Robots at the Edge

Pascal Sikorski, Leendert Schrader, Kaleb Yu, Lucy Billadeau, Fnu Jinka Meenakshi, Naveena Mutharasan, Flavio Esposito, Hadi AliAkbarpour, Madi Babaiasl


[Associated publication](https://arxiv.org/abs/2405.17670).

# Dependencies
Our implementation was developed and tested on Ubuntu 22.04.4/Python 3.10.12.

Libraries and their respective dependencies build from:

LLM Implementation: llama.cpp (llama-2-7b-chatQ5_K_S)

OpenAI Implementation: openai (1.12.0) json (2.0.9)

Offline Speech Recogniton: vosk (0.3.45) pyaudio (0.2.11)

# Usage
To use the system, follow these steps:

Robotic Setup and Configuration: Ensure the smart robot car is correctly setup and connected to your computing environment. A complete guide can be found here: https://www.elegoo.com/blogs/arduino-projects/elegoo-smart-robot-car-kit-v4-0-tutorial.

Audio Speech-to-Text Configuration: We will provide instruction assuming implementation of the offline speech-to-text model, VOSK. After installing the required packages listed above, navigate to the VOSK model webpage and download a model best suited for your system. Our implementation utilized vosk-model-en-us-0.22, finding high performance and efficiency in testing. After installation, navigate to our repo file "speechToText.py", and configure the path location to the now downloaded location of the VOSK model.

OpenAI API Key Configuration: Again, after installing the required packages listed, navigate to OpenAI API webpage. If prompted to log in or create an account for the service, do so. Afterward, follow the prompts to generate an agent key, and save this key as we will need it for API use within our program. If you have not already, create a ".env" file. Add the line "OPENAI_API_KEY = < YOUR KEY HERE >" as the only related key needed for our program to follow. Replace < YOUR KEY HERE > with your key generated from the Open AI key generation step. You have now connected your personal Open AI account for use in our framework. Note, that only GPT-3.5 will be supported on the starting free plan.

Offline quantized llama. Install here: https://github.com/ggerganov/llama.cpp
To obtain models, you may use any gguf extension model. Here is where we find the ones for this experiment. https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF
Place llamacpp.py in the root directory of the llamacpp folder. This will allow you to access everything from llamacpp.
Take the model you downloaded, then you can drop it in the folder in "models" of llamacpp.
Afterwards, make sure you change the llamacpp.py Python file to include the correct model name before running.
The offline LLM model will sometimes output a command along with some words or sentences. We can use a Regex parser to search for valid commands in the output string in order to extract the command.


Execution: Following correct setup of the steps above, we now will be able to connect to our robot and begin use.

# Example Results
https://youtu.be/zHunM45R7AU

# Citation (BibTeX)

@article{sikorski2025mobile,
 author = {Sikorski, Pascal and Schrader, Leendert and Yu, Kaleb and Billadeau, Lucy and Meenakshi, Jinka and Mutharasan, Naveena and Esposito, Flavio and AliAkbarpour, Hadi and Babaiasl, Madi},
 title = {Deployment of Large Language Models to Control Mobile Robots at the Edge},
 booktitle = {3rd International Conference on Mechatronics,  Control and Robotics (ICMCR)},
 year = {2025},
} 
