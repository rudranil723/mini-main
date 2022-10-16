#import assets.noteapp as noteapp
from turtle import *
from cgitb import text
from email.mime import audio
from socket import TCP_NODELAY
#import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import random
import warnings
from toml import TomlDecodeError
import wikipedia
import calendar
from cgi import print_arguments
from traceback import print_tb
from datetime import date

# text password funtion to check wether the password entered is correct or not

def password(text):
    wakewords = ['mini', 'hey mini', 'hello mini']
    for phrase in wakewords:
        if phrase == text:
            print('welcome user')
            os.system('python assets/textcommandfuntion.py')
            break
        else:
            print('password entered is wrong,bye')
            break

# main funtion

def main():
    allowences = 3
    print(" ")
    print(":::::_WELLCOME USER_:::::")
    print(" ")
    print("please select how you want to run me(mi_ni)")
    print(" ")
    print("Enter: 1: for text command")
    print("  or   2: for voice command \n")
    while allowences > 0:
        c = int(input('\n enter choice: '))
        if c == 1:
            print('going forward with text commands')
            t = input('\n enter password: ')
            password(t)
            break
        if c == 2:
            # recordaudio(t)  # for calling in the voice control funtions
            break
        else:
            print('invalid input, try again ')
        allowences -= 1


if __name__ == "__main__":
    main()
