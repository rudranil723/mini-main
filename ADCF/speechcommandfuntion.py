from email.mime import audio
import speech_recognition as sr
import pyttsx3
import os
from texttospeech import *

# initialize the recognition

r = sr.Recognizer()

# funtion to convert text to speech


def main():
    # def speechpassword(password):
    #     wakewords = ['mini', 'hey mini', 'hello mini', 'hello', 'hello hello']
    #     for i in range(0, len(wakewords)):
    #         if password == wakewords[i]:
    #             print('welcome!!')
    #             minisay('hellow')
    #             os.system('python assets/textcommandfuntion.py')

    def speaktext(command):

        # initialize the engine
        engine = pyttsx3.init()
        engine.say(command)
        engine.runAndWait()

    with sr.Microphone() as source2:
        # wait for a second
        r.adjust_for_ambient_noise(source2, duration=0.2)
        # listen to user's input
        audio2 = r.listen(source2)
        # using google to recognize audio
        Mytext = r.recognize_google(audio2)
        Mytext = Mytext.lower()
        print('you said : ' + Mytext)
        # speechpassword(Mytext)

        speaktext(Mytext)


if __name__ == "__main__":
    main()
