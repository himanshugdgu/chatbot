import pyttsx3
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 200)
voice = engine.getProperty('voices')  # getting details of current voice
# for v in voice:
#     print(v.name)
def speak(audio,name="Mark"):
    idx=3
    if(name=="Ravi"):
        idx=1
    elif(name=="David"):
        idx=2
    elif(name=="Mark"):
        idx=3
    elif(name=="Heera"):
        idx=4
    elif(name=="Zira"):
        idx=5
    engine.setProperty('voice', voice[idx].id)
    engine.say(audio)
    engine.runAndWait()