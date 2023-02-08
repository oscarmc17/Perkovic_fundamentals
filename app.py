from tkinter import Tk, Button, LEFT, RIGHT, Label, Entry, END
from time import strftime, localtime, gmtime, strptime
from tkinter.messagebox import showinfo


# def local():
#     time = strftime('Day: %d %b %Y\nTime: %H:%M:%S %p\n', localtime())
#     # showinfo(message=time)
#     print(time)


# root = Tk()
# button = Button(root, text='Click for Local Time', command=local)
# button.pack(side=LEFT)


# def greenwhich():
#     time = strftime('Day: %d %b %Y\nTime: %H:%M:%S %p\n', gmtime())
#     # showinfo(message=time)
#     print(time)


# button2 = Button(root, text='Click for Greenwhich Time', command=greenwhich)
# button2.pack(side=RIGHT)
# root.mainloop()


def compute():
    global dateEnt

    date = dateEnt.get()
    weekday = strftime('%A', strptime(date, '%b %d, %Y'))
    showinfo(message='{} was a {}'.format(date, weekday))
    dateEnt.delete(0, END)

root = Tk()

# label
label = Label(root, text='Enter date')
label.grid(row=0, column=0)

# entry
dateEnt = Entry(root)
dateEnt.grid(row=0, column=1)

# button
button = Button(root, text='Enter', command=compute)
button.grid(row=1, column=0, columnspan=2)

root.mainloop()