#strting to write mi_ni 16.04.2022

#importing necessary libraries 

from cgitb import text
from email.mime import audio
import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import random
import warnings
import wikipedia
import calendar

warnings.filterwarnings('ignore')  #this will avoid unnessary warnings 

#record audio and return audio as a string 

def recordaudio():  #funtion to record audio and return as a string
    #record audio
    r=sr.Recognizer()  #creating a recognizer object
    with sr.Microphone() as source:
        print('say something')
        audio= r.listen(source)

        data = ''   #we will use google speech recognization to understand the said word 
        try:
              data = r.recognize_google(audio)
              print('you said '+data)
        except sr.UnknownValueError:   #this will help us to check for unknown errors
            print('unknown error has been detected')
        except sr.RequestError as e:
            print('request result from google speech service error ' + e)

        return data

# fiuntion to get the AI response with the words we said 

def assistantResponse(text):
    print(text)

    myobj=gTTS(text= text,lang='en',slow=False)  #convert the text to speech
    myobj.save('assistant_response.mp3') #save the audio file to play it 
    os.system('start assistant_response.mp3')

# wakeword funtion or password funtions

def wakeword(text):
    wake_words=['mini','hey mini','hello mini','okay mini'] #list of wake words(passwords)
    text=text.lower() #coneverting all words to lower case
    # now we will see if the users input contents a wakee word/password
    for phrase in wake_words:
        if phrase in text:
            return True
            
        return False