from threading import Thread
import pyttsx3
import speech_recognition as sr
from playsound import playsound


engine = pyttsx3.init('sapi5')

voice = engine.getProperty('voices')  # getting details of current voice
engine.setProperty('voice', voice[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


class App1(Thread):
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # playsound(
        #     'F:\\himanshu\\vscode files\\python\\chatbot\\start_assistant.wav')
        print("Listening...")
        # r.pause_threshold = 1
        r.energy_threshold = 500
        audio = r.listen(source, timeout=5)
        playsound(
            'F:\\himanshu\\vscode files\\python\\chatbot\\end_assistant.wav')
    try:
        print("Recognizing...")
        # Using google for voice recognition.
        query = r.recognize_google(audio, language='en-in')

        print("User said: {}".format(query))  # User query will be printed.

        print()
    except Exception as e:
        print("Say that again please...")
        speak("say that again please...")
    # return query


class App2(Thread):
    playsound('F:\\himanshu\\vscode files\\python\\chatbot\\start_assistant.wav')


# App1.start()
App2.start()
