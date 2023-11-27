import google.generativeai as palm
import pandas as pd
import time
import speech_recognition as sr
import pyttsx3 
import google.generativeai as palm

#Write here your API KEY
palm.configure(api_key='Your_PALM_AI_APIKEY')

r = sr.Recognizer()

def SpeakText(command):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        if "english" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
    engine.setProperty('rate', 150) 
    engine.setProperty('volume', 1.0)
    engine.say(command)
    engine.runAndWait()
    
while(1):    
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            print("start")
            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            print(MyText)
            if MyText.lower()=="stop":
                break
            response = palm.chat(messages=MyText)

            print(response.last)
            SpeakText(response.last)
    except sr.UnknownValueError:
        print("unknown error occurred")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    