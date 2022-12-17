from tkinter import *

root = Tk()
e = Entry(root, width=50)
e.pack()


def myClick():
    hello = 'hellow'+e.get()
    myLabel = Label(root, text="hellow " + e.get())
    myLabel.pack()


myButton = Button(root, text='enter name', command=myClick)
myButton.pack()

root.mainloop()
