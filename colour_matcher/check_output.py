import tkinter as tk
import csv


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid(sticky="news")
        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)
        self.csv_reader = csv.reader(open("output.csv"))
        self.create_widgets()
        self.total_count = 0
        self.right_count = 0

    def next_colour(self):
        return next(self.csv_reader)

    def mk_grid(self, widget, column, row, columnspan=1):
        widget.grid(
            column=column, row=row, columnspan=columnspan, sticky="news"
        )

    def create_widgets(self):
        colour_text, colour_bg = self.next_colour()
        self.colour_box = tk.Label(
            self, bg=colour_bg, width="30", height="15"
        )
        self.mk_grid(self.colour_box, 0, 0, 2)

        self.colour_label = tk.Label(self, text=colour_text, height="3")
        self.mk_grid(self.colour_label, 0, 1, 2)

        self.no_button = tk.Button(
            self, command=self.count_next, text="No"
        )
        self.mk_grid(self.no_button, 0, 2)

        self.yes_button = tk.Button(
            self, command=self.count_yes, text="Yes"
        )
        self.mk_grid(self.yes_button, 1, 2)

        self.percent_accurate = tk.Label(self, height="3", text="0%")
        self.mk_grid(self.percent_accurate, 0, 3, 2)

        self.quit = tk.Button(
            self, text = "Quit", command=root.destroy, bg="#ffaabb"
        )
        self.mk_grid(self.quit, 0, 4, 2)

    def count_yes(self):
        self.right_count += 1
        self.count_next()

    def count_next(self):
        self.total_count += 1
        percentage = self.right_count / self.total_count
        self.percent_accurate["text"] = f"{percentage:.0%}"
        try:
            colour_text, colour_bg = self.next_colour()
        except StopIteration:
            colour_text = "DONE"
            colour_bg = "#ffffff"
            self.colour_box["text"] = "DONE"
            self.yes_button["state"] = tk.DISABLED
            self.no_button["state"] = tk.DISABLED
        self.colour_label["text"] = colour_text
        self.colour_box["bg"] = colour_bg

root = tk.Tk()
app = Application(master=root)
app.mainloop()