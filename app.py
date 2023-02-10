from tkinter import Tk, Button, LEFT, RIGHT, Label, Entry, END, Text, BOTH, Canvas, Frame, SUNKEN
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

# root = Tk()

# def begin(event):
#     'initializes the start of the curve to mouse position'
#     global oldx, oldy, curve
#     oldx, oldy = event.x, event.y
#     curve = []


# def draw(event):
#     global oldx, oldy, canvas, curve
#     newx, newy = event.x, event.y

#     curve.append(canvas.create_line(oldx, oldy, newx, newy))
#     oldx, oldy = newx, newy

# def delete(event):
#     'delete last curve drawn'
#     global curve
#     for segment in curve:
#         canvas.delete(segment)


# oldx, oldy = 0, 0

# canvas = Canvas(root, height=150, width=300)

# canvas.bind("<Button-1>", begin)
# canvas.bind("<Button1-Motion>", draw)
# canvas.bind('<Control-Button-1>', delete)

# canvas.pack()
# root.mainloop()


# ------------------------------- 9.7 -------------------------------

# root = Tk()

# def up():
#     global y, canvas
#     canvas.create_line(x, y, x, y-10)
#     y -= 10


# def left():
#     global x, canvas
#     canvas.create_line(x, y, x-10, y)
#     x -= 10


# def right():
#     global x, canvas
#     canvas.create_line(x, y, x+10, y)
#     x += 10


# def down():
#     global y, canvas
#     canvas.create_line(x, y, x, y+10)
#     y += 10


# canvas = Canvas(root, height=100, width=150, relief=SUNKEN, borderwidth=3)
# canvas.pack(side=LEFT)

# box = Frame(root)
# box.pack(side=RIGHT)

# button = Button(box, text='Up', command=up)
# button.grid(row=0, column=0, columnspan=2)
# button = Button(box, text='Left', command=left)
# button.grid(row=1, column=0)
# button = Button(box, text='right', command=right)
# button.grid(row=1, column=1)
# button = Button(box, text='down', command=down)
# button.grid(row=2, column=0, columnspan=2)

# x, y = 50, 75

# root.mainloop()


# ------------------------------- 9.8 -------------------------------

# def clicked():
#     time = strftime('Day: %d %b %Y\nTime: %H:%M:%S %p\n', localtime())
#     showinfo(message=time)

# root = Tk()
# button = Button(root, text='Click it', command=clicked)

# button.pack()
# root.mainloop()


class ClickIt(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()
        button = Button(self, text='Click it', command=self.clicked)
        button.pack()

    def clicked(self):
        time = strftime('Day: %d %b %Y\nTime: %H:%M:%S %p\n', localtime())
        showinfo(message=time)

root = Tk()
app = ClickIt(root)
app.pack()
root.mainloop()