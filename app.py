from tkinter import Tk, Button, LEFT, RIGHT, Label, Entry, END, Text, BOTH, Canvas
from time import strftime, localtime, gmtime, strptime
from tkinter.messagebox import showinfo

# ------------------------------- 9.3 -------------------------------
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


# ------------------------------- 9.4 -------------------------------
# def compute():
#     global dateEnt

#     date = dateEnt.get()
#     weekday = strftime('%A', strptime(date, '%b %d, %Y'))
#     # showinfo(message='{} was a {}'.format(date, weekday))
#     dateEnt.insert(0, weekday+' ')

# def clear():
#     dateEnt.delete(0, END)

# root = Tk()

# # label
# label = Label(root, text='Enter date')
# label.grid(row=0, column=0)

# # entry
# dateEnt = Entry(root)
# dateEnt.grid(row=0, column=1)

# # button
# button = Button(root, text='Enter', command=compute)
# button.grid(row=1, column=0, columnspan=2)

# # Delete Button
# delBut = Button(root, command=clear, text="Clear")
# delBut.grid(row=1, column=0, columnspan=1)

# root.mainloop()

# ------------------------------- 9.5 -------------------------------
# def record(event):
#     print('char = {}'.format(event.num))

# root = Tk()
# text = Text(root, width=20, height=5)
# text.bind('<KeyPress>', record)
# text.pack(expand=True, fill=BOTH)

# root.mainloop()


# def compute():
#     global dateEnt

#     date = dateEnt.get()
#     weekday = strftime('%A', strptime(date, '%b %d, %Y'))
#     showinfo(message='{} was a {}'.format(date, weekday))
#     dateEnt.insert(0, weekday+' ')
#     # dateEnt.delete(0, END)

# def compute2(event):
#     compute()

# root = Tk()

# # label
# label = Label(root, text='Enter date')
# label.grid(row=0, column=0)

# # entry
# dateEnt = Entry(root)
# dateEnt.grid(row=0, column=1)

# # button
# button = Button(root, text='Enter', command=compute)
# button.grid(row=1, column=0, columnspan=2)

# # Bind a key press event handling function record()
# dateEnt.bind('<Return>', compute2)

# root.mainloop()


# ------------------------------- 9.6 -------------------------------

root = Tk()

def begin(event):
    'initializes the start of the curve to mouse position'
    global oldx, oldy
    oldx, oldy = event.x, event.y


def draw(event):
    global oldx, oldy, canvas
    newx, newy = event.x, event.y

    canvas.create_line(oldx, oldy, newx, newy)

    oldx, oldy = newx, newy


oldx, oldy = 0, 0

canvas = Canvas(root, height=150, width=300)

canvas.bind("<Button-1>", begin)
canvas.bind("<Button1-Motion>", draw)

canvas.pack()
root.mainloop()
