
from asyncio import tasks
import os
import sys


def tasks(term):
    if term == 1:
        print('please chose which tasks you want me to perform')
        print('\n 1. for doing calculations \n 2. to know the date and time \n 3. for drawing heart \n 4. for launching notepadd app \n 5. EXIT \n 6.RESTART(not yet working)')
        print("\n Enter choise: ")
        # here is where i want to apply machine learning so thata the mini can perform multiplke funtuoin withoutr a list
        a = int(input())
        if a == 1:
            os.system('python assets/text-funtion/calculator.py')
            tasks(1)
        if a == 2:
            # this funtion is not working
            os.system('python assets/text-funtion/datetime.py')
            tasks(1)
        if a == 3:
            os.system('python  assets/text-funtion/heart.py')
            tasks(1)
        if a == 4:
            os.system('python  assets/text-funtion/noteapp.py')
            tasks(1)
        if a == 5:
            print('goodbye')
        # i want to implement restert in the code but dont know how to go out of the current folder and call mini.py
        # if a == 6:
            # sys.path.insert(0, '/mini-main/mini.py')
            # os.system('python ')


tasks(1)
