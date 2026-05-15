import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

listener = sr.Recognizer()

def command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            data = listener.recognize_google(voice)
            return data.lower()
    except:
        return ""

while True:
    text = command()

    if 'youtube' in text:
        speak("Opening YouTube")
        pywhatkit.playonyt("coding")

    elif 'time' in text:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak(time)

    elif 'google' in text:
        speak("Opening Google")
        pywhatkit.search("Python projects")

    elif 'stop' in text:
        speak("Goodbye")
        break