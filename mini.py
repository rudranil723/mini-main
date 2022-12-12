# main file of mi_ni 2.0

# required imports

from logging import warning
from turtle import *
from cgitb import text
from email.mime import audio
from socket import TCP_NODELAY
import speech_recognition as sr
import os
from gtts import gTTS
import warnings
from toml import TomlDecodeError
from cgi import print_arguments
from traceback import print_tb
from datetime import date

# importing sub-files required for the project
import passwordcheck
import ear
import mouth

# fillter warning funtion to ignore all other unnecessary errors

warnings.filterwarnings("ignore")

# main funtion

# this mini.py file is the main file from where the project starts


def main():
    # the user is allowed to enter choice only 3 times
    allowences = 3
    # mouth.minisay(voice="welcome user")
    print("\n:::::_WELLCOME USER_:::::\n")
    print("please select how you want to run me(mi_ni)\n")
    print("Enter: 1: for text command")
    print("  or   2: for voice command \n")

    while allowences > 0:
        c = int(input('\n enter choice: '))

        if c == 1:
            print('\nGoing forward with text commands')
            t = input('\n enter password: ')
            # calling in the passwordcheck.py file to check wether the phrase entered by the user contains the password/ wake-word
            # passwordcheck.py file location - mini-main/passwordcheck.py
            passwordcheck.text_password(t)
            break

        if c == 2:
            print('\nGoing forward with voice control password: \n')
            print('please say any of the wake-words\n')

            # calling the mouth.py
            # making mini say by calling the mouth.py ,after which the user shall say the password/ wake word phrase
            # passwordcheck.py file location - mini-main/mouth.py
            mouth.minisay(voice='okay going foward with voice control')
            # calling the ear.py file to make mini listen the input by the user
            key = ear.minihear()
            # sending the password/ wake-word to the passwordcheck file to check the file
            # passwordcheck.py file location - mini-main/passwordcheck.py
            passwordcheck.speech_password(key)
            break

        else:
            print('invalid input, try again ')
        allowences -= 1


if __name__ == "__main__":
    main()
