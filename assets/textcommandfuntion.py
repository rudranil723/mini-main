
from asyncio import tasks
import os
import sys
import arrayformationusing_nltk


def tasks(term):
    if term == 1:
        # print('please chose which tasks you want me to perform')
        # print('\n 1. for doing calculations \n 2. to know the date and time \n 3. for drawing heart \n 4. for launching notepadd app \n 5. EXIT \n 6.RESTART(not yet working)')
        # print("\n Enter choise: ")
        # here is where i want to apply machine learning so thata the mini can perform multiplke funtuoin withoutr a list
        a = input('\n user : ')
        # pa refers to the array formed by the entered phase
        pa = arrayformationusing_nltk.arrayformationby_nltk(a)

        for i in pa:

            # key words  that the user must use in his phase or command to activate calculator funtion
            cal = ['calculation', 'calculator', 'add',
                   'substract', 'divide', 'multiply', 'cal']
            if i in cal:
                # calling the calculator file location assets/text-funtion/calculator.py to perform calculation
                os.system('python assets/text-funtion/calculator.py')
                tasks(1)
                break

            # key words  that the user must use in his phase or command to activate date&time funtion
            dt = ['date', 'time', 'date time', 'clock']
            if i in dt:
                os.system('python assets/text-funtion/date-timefuntion.py')
                tasks(1)
                break

            # key word  that the user must use in his phase or command to activate heart funtion
            hrt = ['heart']
            if i in hrt:
                os.system('python  assets/text-funtion/heart.py')
                tasks(1)
                break

            # key word  that the user must use in his phase or command to activate note-pad funtion
            np = ['notepad', 'list', 'note']
            if i in np:
                os.system('python  assets/text-funtion/noteapp.py')
                tasks(1)
                break

            # key word  that the user must use in his phase or command to activate stopwatch funtion
            sw = ['stopwatch', 'timer']
            if i in sw:
                os.system('python assets/text-funtion/stopwatch.py')

            # here enter more tasks that the AI must perform

            # final command
            else:
                print('sorry mini did not understand your command please retry')
                tasks(1)


tasks(1)
