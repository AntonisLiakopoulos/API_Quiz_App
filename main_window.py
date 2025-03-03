from tkinter import*
THEME_COLOR = "#375362"


class OriginalWindow:
    def __init__(self):
        self.window = Tk()
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.title("Quizmania")


