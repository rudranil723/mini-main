import gtts
from playsound import playsound
import os

language = 'en'



def minisay(voice):
    t1 = gtts.gTTS(voice)
    # t1 = gtts(text=voice, lang=language, slow=False)
    t1.save("mini.mp3")
    playsound("mini.mp3")


# this will fix the voice to null to make it re-run
voice = ''
