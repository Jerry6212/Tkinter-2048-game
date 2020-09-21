from tkinter import *
import tkinter.messagebox

root = Tk()


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


# Toolbar
toolbar = Frame(root, bg="red")
button_insert = Button(toolbar, text="settings", command=DoSomething)
# inserts button into toolbar and has 2 pix padding
button_insert.pack(side=LEFT, padx=2, pady=2)

print_button = Button(toolbar, text="Print", command=DoSomething)
print_button.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

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

# status bar

status = Label(root, text="Doing nothing", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

canvas = Canvas(root, width=200, height=100)
canvas.pack()

black_line = canvas.create_line(0, 0, 200, 50)
red_line = canvas.create_line(0, 100, 200, 50, fill="red")
green_box = canvas.create_rectangle(25,25, 130, 60, fill="green")

# add picture
photo = PhotoImage(file="Jerry 2017 (1)small.png")
label = Label(root, image=photo)
label.pack(side=BOTTOM)


canvas.delete(green_box)
root.mainloop()
