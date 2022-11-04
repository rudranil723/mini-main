from email.mime import audio
import speech_recognition as sr
import pyttsx3


r = sr.Recognizer()


def minihear():
    with sr.Microphone() as source2:
        r.adjust_for_ambient_noise(source2, duration=0.2)
        audio2 = r.listen(source2)
        Mytext = r.recognize_google(audio2)
        Mytext = Mytext.lower()
        print('you said : ' + Mytext)
        return Mytext
