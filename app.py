from tkinter import Tk, Button
from time import strftime, localtime
from tkinter.messagebox import showinfo


def clicked():
    time = strftime('Day: %d %b %Y\nTime: %H:%M:%S %p\n', localtime())
    showinfo(message=time)

root = Tk()
button = Button(root, text='click it', command = clicked)

button.pack()
# root.mainloop()