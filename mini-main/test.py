# mini 2.0 date 18.01.2022

from email.mime import audio
import speech_recognition as sr
import os
from gtts import gTTS
import datetime
from datetime import datetime
import math
import wikipedia
import warnings
import warnings
import random

warnings.filterwarnings('ignore')  # this will ignore any unnessary warnings


def password(text):  # funtion to check password/wake word
    # words that can be used by the user as password/wakewords
    wake_word = ["hey mini", "mini", "yo mini", "hi mini", "okay mini"]
    text = text.lower()  # converting the input data to lower case
    for phrase in wake_word:
        if phrase == text:
            # return true if the password entered by the user is correct
            print("hellow user!!! :)")
            break
        else:
            # the program will not work of the passowrd is wrong
            print("you have entered a wrong password, mini won't work BYE.....")
            break


def recordaudio():  # function to record audio from the user
    r = sr.Recognizer()
    with sr.Microphone() as source:  # calling in the microphone to record the audio from user
        print("say the password: ")
        audio = r.listen(source)
    data = ""
    try:2
        data = r.recognize_google(audio)
        print("you said: "+data)
        password(data)  # sending the input data to check for password
    except sr.UnknownValueError:
        print("you have entered a wrong password, mini won't work BYE.....")
    except sr.RequestError as e:
        print("request result from google speech recognition service error"+e)
    return data


# this is the main part

allowences = 3  # the user has three chance to enter the correct choice
print(" ")
print(":::::_WELLCOME USER_:::::")
print(" ")
print("please select how you want to run me(mi_ni)")
print(" ")
print("Enter: 1: for text command")
print("  or   2: for voice command")
print(" ")
while allowences > 0:

    choice = input("enter choice: ")
    if choice == "1":
        print("you have selcted to procced with text commands")
        # its for entering the password/wake word using keyboard
        text = input("enter password: ")
        password(text)
        break
    elif choice == "2":
        recordaudio()
        break
    else:
        print("invalid input you have more " +
              str(allowences) + " out of 5 tries left")

    allowences = allowences-1
1
