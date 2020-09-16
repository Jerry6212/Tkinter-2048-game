from tkinter import *

root = Tk()


topframe = Frame(root)
topframe.pack(side=TOP)
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

button1 = Button(topframe, text="This is button1", fg="red")
button2 = Button(topframe, text="This is button2", fg="blue")
button3 = Button(topframe, text="This is button3", fg="green")
button4 = Button(bottomframe, text="This is button4", fg="orange")
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop()