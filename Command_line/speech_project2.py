from gtts import gTTS
import pyttsx3
import speech_recognition as sr
from playsound import playsound
from questions import finder
from AppOpener import run
# from translate import Translator
from app_runner import runner
import sys
import news
# translator = Translator(from_lang="hindi", to_lang="english")
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 200)
voice = engine.getProperty('voices')  # getting details of current voice
# for v in voice:
#     print(v.name)
engine.setProperty('voice', voice[5].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        playsound(
            "F://himanshu//vscode files//python//chatbot//Command_line//start_assistant.wav")
        print("Listening...")
        # r.pause_threshold = 1
        r.energy_threshold = 1600
        audio = r.listen(source, timeout=5)
        playsound(
            "F://himanshu//vscode files//python//chatbot//Command_line//end_assistant.wav")
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        # query = translator.translate(query)
        print("User said: {}".format(query))
        print()
        return query
    except Exception as e:
        print("Say that again please...")
        speak("say that again please...")
        takeCommand()


def Basics_questions(str):
    dict = {'how are you': "Actually that dosen't matter",
            'what is your name': "My name is Laura , but i don't know why people call me lawda"}
    return dict.get(str)


def analyzer():
    query = takeCommand()
    main(query)


def main(query):
    query = query.lower()
    ans = Basics_questions(query)
    if 'open' in query:
        query.replace('open', "")
        if (runner(query) == -1):
            # text =
            speak(query+"does not exist")
        else:
            runner(query)
            speak("opening")
    elif ans != None:
        speak(ans)
        print(ans)
    elif 'quit' in query or 'close' in query or 'stop' in query :
        print("ennds")
        return -1
    elif 'news' in query or 'headline' in query or 'headlines' in query:
        text = news.extract()
        text = text[:3]
        for headlines in text:
            print(headlines)
            speak(headlines)

    else:
        text = finder(query)
        print(text)
        speak(text)
        return text

# analyzer()
    # main()
loop = 0
if __name__ == '__main__':
    while loop:
        a = analyzer()
        print(a)
        if(a==-1):
            break

main(sys.argv[1])