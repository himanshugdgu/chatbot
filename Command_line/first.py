import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import pyjokes
from selenium import webdriver
import time

engine = pyttsx3.init('sapi5')

voice = engine.getProperty('voices')  # getting details of current voice
engine.setProperty('voice', voice[0].id)


def speak(audio):
    engine.say(audio)
    # Without this command, speech will not be audible to us.
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    # # speak("I am Jarvis sir. Please tell me ")   
    # speak(" I'm Chitti the Robot. Speed 1 terahertz, memory 1 zigabyte.")   
    # print(" I'm Chitti your personal assistant. Speed 1 terahertz, memory 1 zigabyte.") 

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print("User said: {}".format(query))  #User query will be printed.
        print()
    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        speak("say that again please...")
        main()
        # return "None" #None string will be returned


    return query

def end():
    
    print("do you want to continue...")
    query = takeCommand().lower()

    if 'no' in query:
        i=0
        return(i)
        print("Quitting...")
    else :
        i=1
        return(i)
        print("Continuing...")
# if __name__ == "__main__":
def password():
    while True:
        print("enter password...")
        speak("enter password...")
        query=takeCommand().lower()
        print()
        if 'cool' in query:
            print('cool...')
            speak('cool...')
            break
        else:
            print('Wrong password...')
            speak('Wrong password...')
            
def main():
    
    
    # print("Wishing...")
    # wishMe()
    # print("DONE !!")
    # takeCommand()
    i=1

    while i==1:
        print("how may i help you")
        speak("how may i help you")
        query = takeCommand().lower()

        # Logic for executing tasks based on query

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print("According to Wikipedia")
            speak("According to Wikipedia")
            print(results)
            speak(results)
            i=end()
        elif 'hi' in query or 'hello' in query or 'how are you' in query:
            print("hey! i am fine ,thank you for asking me ")
            speak("hey! i am fine ,thank you for asking me ")
            main()

        elif 'youtube' in query:
            print("What do you want to search in youtube...")
            speak("what do you want to search in youtube...")
            query=takeCommand().lower()
            print("Searching...")
            speak("Searching...")
            PATH="C:\Program Files (x86)\chromedriver.exe"
            driver = webdriver.Chrome(PATH)
            driver.get("https://www.youtube.com/")
            sb=driver.find_element_by_xpath('//*[@id="search"]')
            sb.send_keys(query)
            sbt=driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
            
            sbt.click()
            time.sleep(100)
            i=0
        elif 'google' in query:
            print("What do you want to search in google...")
            speak("what do you want to search in google...")
            query=takeCommand().lower()
            print("Searching...")
            speak("Searching...")
            PATH="C:\Program Files (x86)\chromedriver.exe"
            driver = webdriver.Chrome(PATH)
            driver.get("https://www.google.com/")
            sb=driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
            sb.send_keys(query)
            s=driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[2]/center/input[1]")
            s.click()
            time.sleep(100)
            i=0
        # elif 'open stackoverflow' in query:
        #     webbrowser.open("stackoverflow.com")    
        #     i=end()

        elif 'open code' in query:
            codePath = "D:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            i=end()
        elif 'music' in query or 'song' in query:
            print("should i play your favourite music, or random music")
            speak("should i play your favourate music, or random music")
            query = takeCommand().lower()
            if 'favourite' in query:
                music_dir ='C:\\Users\\jindal\\Music\\favourate music'
                songs = os.listdir(music_dir)
                # print(songs)    
                length=len(songs)
                j=1
                while j==1:
                    i=random.randrange(1,length)
                    a=(songs[i])
                    if 'mp3' in a:
                        result=a
                        j=0
                print("Playing... ",result)
                os.startfile(os.path.join(music_dir, result))
                break
                

            elif 'random' in query:
                # music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
                music_dir ='C:\\Users\\jindal\\Music\\music'
                songs = os.listdir(music_dir)
                # print(songs)    
                length=len(songs)
                i=random.randrange(1,length)
                print("Playing... ",songs[i])
                os.startfile(os.path.join(music_dir, songs[i]))
                break
            else:
                i=end()

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            print(strTime)
            speak("Sir, the time is {}".format(strTime))

        elif 'stop' in query or 'tata' in query or 'shut up' in query or 'quit' in query or 'bye' in query or 'close' in query:
            print("Quiting...")
            speak('Quiting...')
            print('and thank you for using me ')
            speak('and thank you for using me ')
            break

        elif 'joke' in query:
            print('hope u will like this...')
            speak('hope u will like this...')
            j=pyjokes.get_joke()
            print(j)
            speak(j)
            i=end()
        elif 'you do' in query or 'what can' in query :
            print("i can :-")
            print("search on google ,youtube ,as well as on wikipedia ")
            speak("i can search on google ,youtube ,as well as on wikipedia ")
            print("i can tell you time ")
            speak("i can tell you time ")
            print("i can play your favourate or random music")
            speak("i can play your favourate or random music")
            print("i can play with you by telling jokes ")
            speak("i can play with you by telling jokes ")
            print("and i keep learning and exploring...")
            speak("and i keep learning and exploring...")
        else:
            query=takeCommand().lower()
            print("Searching online...")
            speak("Searching online...")
            PATH="C:\Program Files (x86)\chromedriver.exe"
            driver = webdriver.Chrome(PATH)
            driver.get("https://www.google.com/")
            sb=driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
            sb.send_keys(query)
            s=driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[2]/center/input[1]")
            s.click()
            time.sleep(10)
            i=0
print()
# print("hello sir ")
# speak("hello sir ")
wishMe()
# password()
main()