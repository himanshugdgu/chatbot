from translate import Translator

import pyttsx3

translator= Translator(from_lang="hindi",to_lang="english")
# translation = translator.translate("Today is Tuesday")
translation = translator.translate("ॐ नमः शिवाय  सबसे लोकप्रिय हिन्दू मन्त्रों में से एक है और शैव ")
print(translation)
engine = pyttsx3.init()
engine.setProperty("languages",'hi')
engine.say(translation)
engine.runAndWait()