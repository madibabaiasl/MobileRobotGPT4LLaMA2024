# Deployment of NLP and LLM Techniques to Control Mobile Robots at the Edge: A Case Study Using GPT-4-Turbo and LLaMA 2

Pascal Sikorski, Leendert Schrader, Kaleb Yu, Lucy Billadeau, Fnu Jinka Meenakshi, Naveena Mutharasan, Flavio Esposito, Hadi AliAkbarpour, Madi Babaiasl

This repository houses the code and data for our project that integrates _______ to create ___. Our work demonstrates _____. This project aims to _____

# Dependencies
Our implementation was developed and tested on Ubuntu 22.04.4/Python 3.10.12.

Libraries and their respective dependencies build form:

LLM Implementation: llama.cpp (llama-2-7b-chatQ5_K_S)

# Usage
To use the system, follow these steps:

Robotic Setup and Configuration: Ensure the smart robot car is correctly setup and connected to your computing environment. A complete guide can be found here: https://www.elegoo.com/blogs/arduino-projects/elegoo-smart-robot-car-kit-v4-0-tutorial. **(ADD INFO ABT IDE)**

Audio Speech-to-Text Configuration: We will provide instruction assuming implementation of the offline speech-to-text model, VOSK. After installing the required packages listed above, navigate to the VOSK model webpage and download a model best suited for your system. Our implementation utilized vosk-model-en-us-0.22, finding high performance and efficiency in testing. After installation, navigate to our repo file "gptSpeech.py", and configure the path location to the now downloaded location of the VOSK model. **(check models)**

OpenAI API Key Configuration: Again, after installing the required packages listed, navigate to OpenAI API webpage. If prompted to log in or create an account for the service, do so. Afterward, follow the prompts to generate an agent key, and save this key as we will need it for API use within our program. If you have not already, create a ".env" file. Add the line "OPENAI_API_KEY = < YOUR KEY HERE >" as the only related key needed for our program to follow. Replace < YOUR KEY HERE > with your key generated from the Open AI key generation step. You have now connected your personal Open AI account for use in our framework. Note, that only GPT-3.5 will be supported on the starting free plan.

Execution: Following correct setup of the steps above, we now will be able to connect to our robot and begin use. **(ADD MORE INFO)**

# Example Results

# Citation (BibTeX)
