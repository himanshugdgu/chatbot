import speech_recognition as sr
from tts import speak
from playsound import playsound
def takeCommandEnglish():
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
        speak("Can you speak again")
        takeCommandEnglish()
