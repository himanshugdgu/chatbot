# import required module
import speech_recognition as sr
from translate import Translator
from tts import speak
from playsound import playsound


def takeCommandHindi():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        playsound(
            "F://himanshu//vscode files//python//chatbot//Command_line//start_assistant.wav")
        print('Listening')
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            playsound(
                "F://himanshu//vscode files//python//chatbot//Command_line//end_assistant.wav")
            print("Recognizing")
            Query = r.recognize_google(audio, language='hi-In')
            # print("the query is printed='", Query, "'")
            translator = Translator(from_lang="Hindi", to_lang="English")
            translation = translator.translate(Query)
            return translation
        except Exception as e:
            speak("Can you speak again")
            takeCommandHindi()


if __name__ == "__main__":
    print(takeCommandHindi())
