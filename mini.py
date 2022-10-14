
import assets.noteapp as noteapp
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


def password(text):
    wakewords = ['mini', 'hey mini', 'hello mini']
    for phrase in wakewords:
        if phrase == text:
            print('welcome user')
            tasks(1)
            break
        else:
            print('password entered is wrong,bye')
            break

# calculator funtion


def calculations():
    os.system('python assets/calculator.py')


# date and time funtion


def dateandtime():
    today = date.today()
    today = today.strftime("%B %d %Y")
    print("today's date: ", today)


# funtion to draw heart
def heart():
    bgcolor("yellow")
    color("red")
    begin_fill()
    pensize(3)
    left(50)
    forward(133)
    circle(50, 200)
    right(140)
    circle(50, 200)
    forward(133)
    end_fill()

# note pad app


def notepad():
    os.system('python assets/noteapp.py')


# i want this command givinf part to be controlled by machine learning

def tasks(term):
    if term == 1:
        print('please chose which tasks you want me to perform')
        print('\n 1. for doing calculations \n 2. for know the date and time \n 3. for drawing heart \n 4. for launching notepadd app')
        a = int(input())
        if a == 1:
            calculations()
            tasks(1)
        if a == 2:
            dateandtime()
            tasks(1)
        if a == 3:
            heart()
            tasks(1)
        if a == 4:
            notepad()
            tasks(1)


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
