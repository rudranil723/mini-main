from tkinter import *

root = Tk()
# e = Entry(root, width=50)
# e.pack()


# def myClick():
#     myLabel = Label(root, text="hellow " + e.get())
#     myLabel.pack()


# # myButton = Button(root, text='enter name', command=myClick)
# # myButton.pack()


b = Button(root, text="Enter", width=10, height=2)
b.config()
b.pack(side=LEFT)

c = Button(root, text="Clear", width=10, height=2)
c.pack(side=LEFT)
root.mainloop()
