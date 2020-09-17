from tkinter import *


class JerryButton:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.print_button = Button(frame, text="Print message", command=self.print_message)
        self.print_button.pack(side=LEFT)
        self.quit_button = Button(frame, text="Quit", command=frame.quit)
        self.quit_button.pack(side=LEFT)

    def print_message(self):
        print("message")


root = Tk()
b = JerryButton(root)
root.mainloop()
