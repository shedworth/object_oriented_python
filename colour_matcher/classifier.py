"""Produces training dataset from user input.
Users are asked to classify random colours.
Results are saved to a csv file."""

import random
import tkinter as tk
import csv


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid(sticky="news")
        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)
        self.create_widgets()
        self.file = csv.writer(open("colours.csv", "a"))

    def create_colour_button(self, label, column, row):
        button = tk.Button(
            self, command=lambda: self.click_colour(label), text=label
        )
        button.grid(column=column, row=row, sticky="news")

    def random_colour(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        return f"#{r:02x}{g:02x}{b:02x}"

    def create_widgets(self):
    """Box containing random colour for classification"""
        self.color_box = tk.Label(
            self, bg=self.random_colour(), width="30", height="15"
        )
        """Grid of buttons to collect user response"""
        self.color_box.grid(
            column=0, columnspan=2, row=0, sticky="news"
        )
        self.create_colour_button("Red", 0, 1)
        self.create_colour_button("Purple", 1, 1)
        self.create_colour_button("Blue", 0, 2)
        self.create_colour_button("Green", 1, 2)
        self.create_colour_button("Yellow", 0, 3)
        self.create_colour_button("Orange", 1, 3)
        self.create_colour_button("Pink", 0, 4)
        self.create_colour_button("Grey", 1, 4)
        """Quit button exits program and saves csv"""
        self.quit = tk.Button(
            self, text="Quit", command=root.destroy, bg="#ffaabb"
        )
        self.quit.grid(column=1, row=5, columnspan=2, sticky="news")

    def click_colour(self, label):
    """Action triggered when colour button clicked.
    Writes tuple of (user classified label, colour being classified)"""
        self.file.writerow([label, self.color_box["bg"]])
        self.color_box["bg"] = self.random_colour()


root = tk.Tk()
app = Application(master=root)
app.mainloop()