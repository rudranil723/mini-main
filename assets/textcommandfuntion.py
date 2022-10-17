
from asyncio import tasks
import os


def tasks(term):
    if term == 1:
        print('please chose which tasks you want me to perform')
        print('\n 1. for doing calculations \n 2. for know the date and time \n 3. for drawing heart \n 4. for launching notepadd app \n 5. EXIT')
        print("\n Enter choise: ")
        a = int(input())
        if a == 1:
            os.system('python assets/text-funtion/calculator.py')
            tasks(1)
        if a == 2:
            #this funtion is not working
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


tasks(1)
