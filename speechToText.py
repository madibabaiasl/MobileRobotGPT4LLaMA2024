# VOSK wrapper written by:
# Pascal Sikorski

from vosk import Model, KaldiRecognizer
import pyaudio
import json

model = Model(r"/home/group1/Desktop/fire/trainedModels/vosk-model-en-us-0.22")
recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16,
                  channels=1,
                  rate=16000,
                  input=True,
                  frames_per_buffer=8192)

print("AUDIO MODEL COMPILE SUCCESS -- READY FOR AUDIO")
stream.start_stream()

def speechToText():
    print("starting to listen for stuff")
    while True:
        data = stream.read(4096, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            text = recognizer.Result()
        else:
            text = recognizer.PartialResult()

        if text:
            textDict = json.loads(text)
            if 'text' in textDict and textDict['text']:
                if ("quit" in textDict['text']):
                    return None
                print(textDict['text'])
                return textDict['text']
