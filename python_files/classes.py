from tkinter import *
import tkinter as tk
import python_files.global_var as var

# region ====== Klasy ======

class Header(tk.Label):
    def __init__(self, frame, text_var):
        super().__init__(
            frame,
            text=text_var.upper(),
            font=("Helvetica", 40, "bold"),
            anchor="center",
            bg=var.COLOR
        )

class Gap(tk.Label):
    def __init__(self, frame, text):
        super().__init__(
            frame,
            text=text.upper(),
            font=("Helvetica", 14, "bold"),
            anchor="center",
            bg="white"
        )

class Custom_Button(tk.Button):
    def __init__(self, text, box, command):
       super().__init__(
            box, 
            text=text.upper(),
            font=("Helvetica", 20, "bold"),
            padx=40,
            pady=5,
            fg="white",
            bg="dodger blue",
            relief="solid",
            highlightbackground="black",
            highlightthickness=2,
            activebackground=var.COLOR,
            activeforeground="black",
            command=command
       ) 
#super() odwoluje sie do klasy nadrzednej(rodzica) danej klasy

class Action_Button(Custom_Button):
    def __init__(self, text, box, command):
        super().__init__(text, box, command)
        self.config(
            font=("Helvetica", 12, "bold"),
            padx=10,
            pady=5
        )

class Small_Button(Action_Button):
    def __init__(self, text, box, command):
        super().__init__(text, box, command)
        self.config(
            font=("Helvetica", 9, "bold"),
            padx=5,
            pady=2
        )

# Przycisk EXIT oraz cofania się na poprzednia strone
class Back_Button(Custom_Button):
    def __init__(self, text, box, command):
        super().__init__(text, box, command)
        self.config(
            font=("Helvetica", 14, "bold"),
            padx=20,
            pady=5
        )

# Miejsca na tekst gdzie mają byc umieszczane ścieżki do plikow
class Path_label(tk.Label):
    def __init__(self, frame, var):
        super().__init__(
            frame,
            bg="white", 
            textvariable=var, 
            font=("Helvetica", 10),
            padx=5,
            pady=2
        )

class Key_Label(Path_label):
    def __init__(self, frame, var):
        super().__init__(frame, var)
        self.config(
            width=45,
            borderwidth=2,
            relief="solid",
            highlightbackground="black"
        )

class Key_Entry(tk.Entry):
    def __init__(self, frame):
        super().__init__(frame)
        self.config(
            font=("Helvetica", 10), 
            width=50,
            borderwidth=2,
            relief="solid",
            highlightbackground="black"
        )
#endregion