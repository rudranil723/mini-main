from tkinter import *
import os

root = Tk()

# adding background color to the whole tab
root.configure(bg="pink")

# adjusting size of the window
root.geometry("600x600")
root.minsize(400, 400)

# declaring the main funtion

e = Entry(root)


def main():
    myLabel = Label(
        root, text="\n:::::_WELLCOME USER_:::::\n \nplease select how you want to run me(mi_ni)\n \npress button 1 for text command\n \n  or press button 2 for voice command \n", bg='pink', fg='green')
    myLabel2 = Label(root, text="Enter choise:")
    myLabel.pack()
    myLabel2.pack()
    myButton1 = Button(root, text="text command", width=15, height=2)
    myButton2 = Button(root, text="voice command", width=15, height=2)
    myButton1.pack()
    myButton2.pack()


main()
root.mainloop()
