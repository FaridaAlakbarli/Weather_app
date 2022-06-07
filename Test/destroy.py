from tkinter import *

root = Tk()
root.geometry('200x200')
root.resizable(0, 0)

button1 = Button(root, text = 'this is unnecessary')
button1.pack()

button2= Button(root, text = 'click to close the unnecessary button', command = button1.destroy)
button2.pack()

root.mainloop()
