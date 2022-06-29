
from turtle import *
from cgitb import text
from email.mime import audio
from socket import TCP_NODELAY
import speech_recognition as sr
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
    print('what do you want to calculate?')
    print('addition substraction multiplication divid')
    print('   1          2             3           4')
    calculationvariable = input()
    if calculationvariable == '1':
        print('please eter two numbers you wish to add: ')
        num1, num2 = map(int, input().split(' '))
        print('result: '+(num1+num2))
    elif calculationvariable == '2':
        print('please eter two numbers you wish to add: ')
        num1, num2 = map(int, input().split(' '))
        print('result: '+(num1-num2))
    elif calculationvariable == '3':
        print('please eter two numbers you wish to add: ')
        num1, num2 = map(int, input().split(' '))
        print('result: '+(num1*num2))
    elif calculationvariable == '4':
        print('please eter two numbers you wish to add: ')
        num1, num2 = map(int, input().split(' '))
        print('result: '+(num1/num2))

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


def tasks(term):
    if term == 1:
        print('please chose which tasks you want me to perform')
        print('1 for doing calculations 2. for know the date and time 3.for aming heart')
        a = int(input())
        if a == 1:
            calculations()
        if a == 2:
            dateandtime()
        if a == 3:
            heart()


allowences = 3
print(" ")
print(":::::_WELLCOME USER_:::::")
print(" ")
print("please select how you want to run me(mi_ni)")
print(" ")
print("Enter: 1: for text command")
print("  or   2: for voice command")
print(" ")
while allowences > 0:
    c = int(input('enter choice: '))
    if c == 1:
        print('going forward with text commands')
        t = input('enter password: ')
        password(t)
        break
    if c == 2:
        # recordaudio(t)  # for calling in the voice control funtions
        break
    else:
        print('invalid input, try again ')
    allowences -= 1
