from tkinter import *
master = Tk()
Label(master, text="Hello World!").pack()
Label(master, text="This is a simple GUI application.").pack()
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
mainloop()
