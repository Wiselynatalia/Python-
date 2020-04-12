#Smartspeaker
import speech_recognition as sr
import time 
from win32com.client import Dispatch
speak = Dispatch("SAPI.SpVOice")
speak.Speak("Hello Wisely")
speak.Speak("I will remind you to...")
r = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    print("Speak Now:")
    audio = r.listen(source, phrase_time_limit=3)
    x = r.recognize_google(audio, language="en-US")
speak.Speak("Okay I will remind you to "+ x+"every how many minutes")
with mic as source:
    print("Minutes:")
    audio1 = r.listen(source, phrase_time_limit=2)
    t = r.recognize_google(audio1)
speak.Speak("Okay I will remind you to "+ x+"every"+t+"minutes")
t = float(t) * 60
t1= time.time()
i=0
while(1):
    try:
        with mic as source:
            print("Speak now (stop):",i)
            audio2 = r.listen(source, phrase_time_limit=2)
            z = (r.recognize_google(audio2, language="en-US"))
            print(z)
            if z == "stop":
                print("it works!")
                break
    except:
        i+=1
        t2 = time.time()
        if (t2-t1) > t:
            speak.Speak("Do not forget to " + x)
            t1 = time.time()