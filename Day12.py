import win32com.client

def speak(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Voice = speaker.GetVoices().Item(0)
    speaker.Speak(text)

run=True
while run:
    x=input("Enter text,press q to quit:\n")
    if(x.lower()=="q"):
        run=False
        break
    speak(x)

