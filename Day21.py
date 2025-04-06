import webbrowser
import time
import speech_recognition as sr
import os
import win32com.client
from datetime import datetime
import sys

def wishme():
    # Get the current time
    now = datetime.now()
    # Extract the current hour
    hour = now.hour

    # Determine the appropriate greeting based on the hour
    if 5 <= hour < 12:
        greeting = "Good morning daddy"
    elif 12 <= hour < 18:
        greeting = "Good afternoon daddy"
    elif 18 <= hour < 22:
        greeting = "Good evening daddy"
    else:
        greeting = "Good night daddy"

    # Print the greeting
    speaker = win32com.client.Dispatch('SAPI.SpVoice')
    print(greeting)
    speaker.speak(greeting)


def speak(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)

def takecommand():
    print("Listening...")
    r=sr.Recognizer()
    m=sr.Microphone()
    with m as source:
        r.pause_threshold=2
        r.energy_threshold=200
        audio=r.listen(source)
        try:
            query=r.recognize_google(audio,language='en-in')
            print(f'user said {query}')
        except:
            print("come again please")
            speak("Please say it again daddy")
    return query

def openweb():
    if "Open youtube".lower() in query.lower():
        webbrowser.open('https://www.youtube.com/')
        speak("Opening youtube")
    elif "Open GPT".lower() in query.lower():
        webbrowser.open('https://chatgpt.com/')
        speak("Opening Chat GPT")
    elif "Open my website".lower() in query.lower():
        webbrowser.open('https://www.pabitrachalise.com.np/')
        speak("Opening your website daddy")

    elif "Open insta".lower() in query.lower():
        webbrowser.open('https://www.instagram.com/')
        speak("Opening Instagram")

    elif "Open git".lower() in query.lower():
        webbrowser.open('https://github.com/')
        speak("Opening Git hub")
    elif "exit".lower() in query.lower():
        speak("Bye,Daddy")
def quit():
    while True:
            user_input = query.lower()
            if 'quit' in user_input:
                print("Terminating the program.")
                speak('Bye Daddy')
                sys.exit()
            # else:
            #     speak(f"You said: {user_input}")

if __name__ =="__main__":
    while True:
        wishme()
        query=takecommand()
        speak(f"You said{query}")
        openweb()
        quit()