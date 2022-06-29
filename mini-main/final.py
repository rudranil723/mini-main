# mi_ni will be created here how and when idk

# funtion for input using keyboard
import pyttsx3
from code import speak
from email.mime import audio
from django.template import engines
import speech_recognition as sr
from main import wakeword
import warnings
from gtts import gTTS


#funtion to recognise what the user is saying and can be called whenever the user wants to say anything
def speechrecognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening")
        r.pause_threshold = 0.7
        audio = r.listen(source)
        data = ''  # we will use google speech recognization to understand the said word
        try:
            data = r.recognize_google(audio)
            print('you said: '+data)
        except sr.UnknownValueError:  # this will help us to check for unknown errors
            print('sorry, did not get you, please repeat')
        except sr.RequestError as e:
            print('request result from google speech service error ' + e)

        return data


#funtion that is converting text to speech and can be called from anywhere 
def minisay(audio):
    engine = pyttsx3.init()
    # getter method(gets the current value
	# of engine property)
    voices= engine.getProperty('voices')
    # [1] for female voice 
    # [0] for male voice
    engine.setProperty('voice',voices[1].id)
    #methord for the speaking of the assistant
    engine.say(audio)
    engine.runAndWait()



def textfuntions(result):
    while (result == True):
        print("welcome, what do you want me to do?")


def speechfuntions(result):
    while (result == True):
        minisay("welcome, what do you want me to do?")
        


def speechpassword():
    voicepassword = speechrecognition()
    #converting the entered password/ wakeword to lower case to doudge bugs XD
    vp = voicepassword.lower()
    wakewords = ["mini", "hey mini", "hi mini", "ok","ok mini","hello","Ok"]
    #checking the password said with the list of wake word
    for i in wakewords:
        if vp == i:
            #calling the speechfuntion funtion 
            speechfuntions(True)
            break
        if vp != i:
            minisay("retry")
            speechpassword()


def textpasswordentry():
    # this are the words that can be used as password or wakeword to make the AI work further
    wakewords = ["mini", "hey mini", "hi mini", "ok mini","ok"]
    print("\nenter password: \n")
    textpass = input()
    tp = textpass.lower()
    # asking the user to enter the password from keyboard

    for i in wakewords:
        # checking if the user enter the correct password/ wakeword or not one by one
        if tp == i:
            print("\nwellcome user")
            # the text task funtion is called if the password entered is correct
            textfuntions(True)
            break
        if tp != i:
            print("\nwrong password\n retry:")
            # recalling the funtion if the password entered is wrong
            textpasswordentry()


def password():
    print("\n:::::_WELLCOME USER_:::::\n")
    print("enter the password: \n enter 1 to give the password from keyboard \n enter 2 to give password using voice recognition ")
    passwordvariable = int(input())
    if passwordvariable == 1:
        textpasswordentry()
    if passwordvariable == 2:
        speechpassword()
    if passwordvariable != 1 or passwordvariable !=2:
        print("wrong entry, please retry")
        password()

# main funtion
if __name__ == '__main__':
    password()
