import gtts
from playsound import playsound

language = 'en'

t1 = gtts.gTTS("hi pilot")
t1.save("mini.mp3")
playsound("mini.mp3")
