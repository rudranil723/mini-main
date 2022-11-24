# file to check if the user has entered the right password or not
import os
import mouth
#python file to cheack password or wake-word by the user input both by terxt ad speech

def text_password(key):
    # you can use any phrase as passowrd just the word mini needs to be present
    wakewords = ['mini', 'hey mini', 'hello mini']
    for phrase in wakewords:
        # if phrase == text:
        if phrase in key:
            print('welcome user')
            os.system('python assets/textcommandfuntion.py')
            break
        else:
            print('password entered is wrong,bye')
            break


def speech_password(key):
    # you can say anything as wake word just word mini needs to be present
    wakewords = ['mini', 'hey mini', 'hello mini', 'hello', 'hey', 'mini mini']
    for phrase in wakewords:
        if key in phrase:
            mouth.minisay(voice='welcome buddy, what do you want me to do?')
            os.system('python assets/textcommandfuntion.py')
        else:
            mouth.minisay(voice='sorry retry again')
            