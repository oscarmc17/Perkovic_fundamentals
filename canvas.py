# from tkinter import Tk, Button, LEFT, RIGHT, Label, Entry, END, Text, BOTH, Canvas, Frame, SUNKEN
# from time import strftime, localtime, gmtime, strptime
# from tkinter.messagebox import showinfo

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
