import tkinter as tk
import colors


# the "Game" class constructs the frame and sets the title to "2048"
class Game(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.cells = []
        self.grid()
        self.master.title("2048")
        self.main_grid = tk.Frame(

            self, bg=colors.grid_color, bd=3, width=600, height=600
        )
        self.main_grid.grid(pady=(100, 0))
        self.make_GUI()
        self.mainloop()
    # Make grid
    def make_GUI(self):
        for i in range(4):
            row = []
            for j in range(4):
                cell_frame = tk.Frame(
                    self.main_grid,
                    bg=colors.empty_cell_color, width=150, height=150)
                cell_frame.grid(row=i, column=j, padx=5, pady=5)
                cell_number = tk.Label(self.main_grid, bg=colors.empty_cell_color)
                cell_number.grid(row=i, column=j)
                cell_data = {"frame": cell_frame, "number": cell_number}
                row.append(cell_data)
            self.cells.append(row)

            # score board
            score_frame = tk.Frame(self)
            score_frame.place(relx=0.5, y=45, anchor="center")
            tk.Label(
                score_frame,
                text="Score",
                font=colors.score_label_font).grid(row=0)
            self.score_label = tk.Label(score_frame, text="0", font=colors.score_font)
            self.score_label.grid(row=1)


Game()





