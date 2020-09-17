from tkinter import *


class JerryButton:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.print_button = Button(frame, text="Print message", command=self.print_message)
        self.print_button.pack(side=BOTTOM)
        self.quit_button = Button(frame, text="Quit", command=frame.quit)
        self.quit_button.pack(side=BOTTOM)

    def print_message(self):
        print("message")

def DoSomething():
    print("Doing thing")




root = Tk()
b = JerryButton(root)
menu = Menu(root)
root.config(menu=menu)
sub_menu = Menu(menu)
menu.add_cascade(label="File", menu=sub_menu)
sub_menu.add_command(label="New file", command=DoSomething)
sub_menu.add_separator()
sub_menu.add_command(label="Open", command=DoSomething)
sub_menu.add_separator()
sub_menu.add_command(label="Exit", command=DoSomething)
edit_menu = Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Redo", command=DoSomething)
root.mainloop()
