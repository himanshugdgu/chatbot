import string
from gtts import gTTS
import pyttsx3
import speech_recognition as sr
from playsound import playsound
from questions import finder
from AppOpener import run
# from translate import Translator
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from app_runner import runner
import news
from datetime import date
from datetime import datetime
import random
from music_player import music_url_opener
import pyjokes
from query_timer import timer1
from AppOpener import run
# translator = Translator(from_lang="hindi", to_lang="english")
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 200)
voice = engine.getProperty('voices')  # getting details of current voice
# for v in voice:
#     print(v.name)
engine.setProperty('voice', voice[1].id)


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
        r.energy_threshold = 700
        audio = r.listen(source, timeout=5)
        playsound(
            "F://himanshu//vscode files//python//chatbot//Command_line//end_assistant.wav")
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        # query = translator.translate(query)
        # print("User said: {}".format(query))
        # print()
        return query
    except Exception as e:
        print("Say that again please...")
        speak("say that again please...")
        takeCommand()


def Basics_questions(query):
    if "hello" in query or "hi" in query or "hey" in query:
        list = ["Hi there",
                "Hey, What's up?",
                "What's going on?",
                "How's everything?"
                ]
        return list[random.randrange(0, len(list))]
    elif "what's up" in query:
        return "My josh is up"
    elif "timer" in query:
        timer1(query)
        return "Time up!!!"
    elif "your name" in query:
        return "I am Jarvis Your Virtual Assistant"
    elif "your age" in query or "old are you" in query:
        return "Actually i am an Women, Sorry I am an object..."
    elif "you do" in query:
        return "Ask My Father for that..."
    elif "what are you doing" in query:
        return "just talking to you"
    elif "your owner" in query:
        return "Himanshu is my owner"
    elif "your father" in query:
        return "My father name is Himanshu"
    elif "how are you" in query:
        return "I am good how about you..."
    elif "who are you" in query:
        return "i am your virtual assistant and i can do whatever you want"
    elif 'feel' in query:
        return "I am feeling very exited today..."
    elif "who made you" in query:
        return "Himanshu is my owner"
    # elif "date" in query:
    #     today = date.today()
    #     return "Today's date: " + str(today)
    # elif "time" in query:
    #     return datetime.now().strftime('%H:%M:%S')
    elif "take a note" in query:
        run("notepad")
        return "opening..."
    else:
        return None

def url_opener(query):
    query = query.lower()
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(
        executable_path=r"C:\Users\HIMANSHU SINGH\Downloads\Compressed\c_14\chromedriver.exe", options=chrome_options)
    if "youtube" in query:
        driver.get("https://www.youtube.com/")
    elif "facebook" in query:
        driver.get("https://www.facebook.com/")
    elif "reddit" in query:
        driver.get("https://www.reddit.com/")
    elif "instagram" in query:
        driver.get("https://www.instagram.com/")
    elif 'twitter' in query:
        driver.get("https://www.twitter.com/")
    elif "whatsapp" in query:
        driver.get("https://web.whatsapp.com/")

    return None


def player(query):
    print("sd")
    music_url_opener(query)
    return ""


def analyzer():
    query = takeCommand()
    return query
    # main(query)


def main(query):
    ans = Basics_questions(query)
    if 'open' in query:
        query.replace('open', "")
        if (runner(query) != -1):
            return "Opening "+query
        elif (url_opener(query) != None):
            return "Opening "+query
    elif 'play' in query:
        query.replace('play', '')
        player(query)
        return "playing"
    elif ans != None:
        return ans
    elif "weather" in query:
        text = finder(query)
        text = ''.join(text.split())
        text = text[:-2]
        return text+" °C"
    elif 'jokes' in query or 'joke' in query:
        My_joke = pyjokes.get_joke(language="en", category="all")
        return My_joke

    elif 'quit' in query or 'close' in query or 'stop' in query:
        return 100
    # elif 'news' in query or 'headline' in query or 'headlines' in query:
    #     text = news.extract()
    #     text = text[:3]
    #     for headlines in text:
    #         print(headlines)
    #         speak(headlines)

    else:
        text = finder(query)
        return text


    # main()
loop = 1
if __name__ == '__main__':
    while loop:
        a = analyzer()
        print(a)
        if (a == -1):
            break


def func(name):
    return "hello "+name
