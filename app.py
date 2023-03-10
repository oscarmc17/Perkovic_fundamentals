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

# class ClickIt(Frame):
#     def __init__(self, master):
#         Frame.__init__(self, master)
#         self.pack()
#         button = Button(self, text='Click it', command=self.clicked)
#         button.pack()

#     def clicked(self):
#         time = strftime('Day: %d %b %Y\nTime: %H:%M:%S %p\n', localtime())
#         showinfo(message=time)

# class Day(Frame):

#     def __init__(self, master):
#         Frame.__init__(self, master)
#         self.pack()

#         label = Label(self, text='Enter date')
#         label.grid(row=0, column=0)

#         self.dateEnt = Entry(self)
#         self.dateEnt.grid(row=0, column=1)

#         button = Button(self, text='Enter', command=self.compute)
#         button.grid(row=1, column=0, columnspan=2)

#     def compute(self):

#         date = self.dateEnt.get()
#         weekday = strftime('%A', strptime(date, '%b %d, %Y'))
#         showinfo(message='{} was a {}'.format(date, weekday))
#         self.dateEnt.delete(0, END)

# root = Tk()
# day = Day(root)
# day.pack()
# clickit = ClickIt(root)
# clickit.pack()
# root.mainloop()

# ------------------------------- 9.9 -------------------------------

# class Draw(Frame):
#     def __init__(self, parent):
#         Frame.__init__(self, parent)
#         self.pack()

#         self.oldx, self.oldy = 0, 0

#         self.canvas = Canvas(self, height=150, width=300)
#         self.canvas.bind("<Button-1>", self.begin)
#         self.canvas.bind("<Button1-Motion>", self.draw)
#         self.canvas.pack(expand=True, fill=BOTH)

#     def begin(self, event):
#         'initializes the start of the curve to mouse position'
#         self.oldx, self.oldy = event.x, event.y

#     def draw(self, event):
#         newx, newy = event.x, event.y
#         self.canvas.create_line(self.oldx, self.oldy, newx, newy)
#         self.oldx, self.oldy = newx, newy


# root = Tk()
# draw = Draw(root)
# draw.mainloop()


class Draw(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()

        self.x, self.y = 50, 75

        self.canvas = Canvas(self, height=100, width=150,
                             relief=SUNKEN, borderwidth=3)
        self.canvas.pack(side=LEFT)

        self.buttons = Frame(self)
        self.buttons.pack(side=RIGHT)

        b1 = Button(self.buttons, text='up', command=self.up)
        b2 = Button(self.buttons, text='left', command=self.left)
        b3 = Button(self.buttons, text='right', command=self.right)
        b4 = Button(self.buttons, text='down', command=self.down)
        clear = Button(self.buttons, text='clear', command=self.clear)
        b1.grid(row=0, column=0, columnspan=2)
        b2.grid(row=1, column=0, columnspan=1)
        b3.grid(row=1, column=1, columnspan=2)
        b4.grid(row=2, column=0, columnspan=2)
        clear.grid(row=5, column=0, columnspan=3)
        # master.bind('<KeyPress-w>', lambda event: self.up())
        master.bind('<KeyPress-w>', self.up)
        master.bind('<a>', self.left)
        master.bind('<s>', self.down)
        master.bind('<KeyPress-d>', self.right)
        master.bind('<Return>', self.clear)

    def up(self, _event=None):
        self.canvas.create_line(self.x, self.y, self.x, self.y-10)
        self.y -= 10

    def left(self, _event=None):
        self.canvas.create_line(self.x, self.y, self.x-10, self.y)
        self.x -= 10

    def right(self, _event=None):
        self.canvas.create_line(self.x, self.y, self.x+10, self.y)
        self.x += 10

    def down(self, _event=None):
        self.canvas.create_line(self.x, self.y, self.x, self.y+10)
        self.y += 10

    def clear(self, _event=None):
        self.canvas.delete('all')


root = Tk()
app = Draw(root)
root.mainloop()
