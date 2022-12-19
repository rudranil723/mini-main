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
        root, text="\n_____WELLCOME USER_____\n \nplease select how you want to run me (mi_ni)\n \npress button 1 for text command\n \n  or press button 2 for voice command \n", bg='pink', fg='purple', font=25)
    myLabel2 = Label(root, text="Enter choise:", font=20)
    myLabel.pack(pady=20, padx=20)
    myLabel2.pack(pady=20, padx=20)
    myButton1 = Button(root, text="text command", width=15,
                       height=2, bg='#FFFFE0', fg='blue')
    myButton2 = Button(root, text="voice command", width=15,
                       height=2, bg='#FFFFE0', fg='blue')
    # need to place the buttons side by side idk how
    myButton1.pack(padx=10)
    myButton2.pack(pady=20)


main()
root.mainloop()
