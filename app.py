from tkinter import Tk, Button, LEFT, RIGHT
from time import strftime, localtime, gmtime
from tkinter.messagebox import showinfo


def local():
    time = strftime('Day: %d %b %Y\nTime: %H:%M:%S %p\n', localtime())
    # showinfo(message=time)
    print(time)


root = Tk()
button = Button(root, text='Click for Local Time', command=local)
button.pack(side=LEFT)


def greenwhich():
    time = strftime('Day: %d %b %Y\nTime: %H:%M:%S %p\n', gmtime())
    # showinfo(message=time)
    print(time)


button2 = Button(root, text='Click for Greenwhich Time', command=greenwhich)
button2.pack(side=RIGHT)
root.mainloop()
