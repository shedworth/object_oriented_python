"""The command pattern links an invoker to a receiver.

e.g.
INVOKER-------->COMMAND-------->RECEIVER
(button)------->(maximise)----->(window)

"""

import sys


"""Define some receiver classes"""
class Window:
    def exit(self):
        sys.exit(0)


class Document:
    def __init__(self, filename):
        self.filename = filename
        self.contents = "This file cannot be modified"

    def save(self):
        with open(self.filename, 'w') as file:
            file.write(self.contents)


"""Define some invoker classes"""
class ToolbarButton:
    def click(self):
        self.commmand()


class MenuItem:
    def click(self):
        self.command()


class KeyboardShortcut:
    def keypress(self):
        self.command()


"""Define some commands"""
class SaveCommand:
    def __init__(self, document):
        self.document = document

    def __call__(self):
        self.document.save()



"""Invoking command directly on receiving object"""
window = Window()
menu_item = MenuItem()
menu_item.command = window.exit


"""Using explicit command class bound to receiving object"""
document = Document("a_file.txt")
shortcut = KeyboardShortcut()
save_command = SaveCommand(document)
shortcut.command = save_command