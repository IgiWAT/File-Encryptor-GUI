from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from cryptography import fernet

# region ====== Klasy ======
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
            activebackground=COLOR,
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

class Back_Button(Custom_Button):
    def __init__(self, text, box, command):
        super().__init__(text, box, command)
        self.config(
            font=("Helvetica", 14, "bold"),
            padx=20,
            pady=5
        )
#endregion

# region ====== Ustawienia ======
COLUMN_WIDTH = 100
COLUMNS = 10
ROW_HEIGHT = 50
ROWS = 12
COLOR = "#E9EEF5"

root = tk.Tk()
root.title("File Encryptor")
root.geometry("1000x700")
root.configure(bg=COLOR)
#endregion

# region ====== Funkcje =======
PATH_1_var = tk.StringVar(value="")
PATH_2_var = tk.StringVar(value="")

def show_frame(frame):
    frame.tkraise()

def exit():
    root.destroy()

def back():
    show_frame(page1)

def find_file(option):
    path = filedialog.askopenfilename(title="Find file to encrypt",
        initialdir=os.getcwd() #otworzy sie w katalagu w ktorym jestesmy
        )
    if option==1: PATH_1_var.set(path)
    elif option==2: PATH_2_var.set(path)

def set_placeholder(entry, text):
    entry.insert(0, text)
    entry.config(fg="grey")

    def on_focus_in(event):
        if entry.get() == text:
            entry.delete(0, tk.END)
            entry.config(fg="black")
    
    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, text)
            entry.config(fg="grey")
    
    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

def encrypt(entry):
    path1 = PATH_1_var.get().strip()
    path2 = PATH_2_var.get().strip()
    entry = entry.get().strip()

    if path1 != "":
        if path2 != "" or entry != "Type your encryption key":
            if path2 != "" and  entry != "Type your encryption key":
                messagebox.showerror("Error", "Choose ONLY ONE way to encrypt file")
            else: 
                #with open(f"{path1}", 'rb') as plain_file:
                pass
        else: messagebox.showerror("Error", "Choose way to encrypt file")
    else: messagebox.showerror("Error", "Choose file to encrypt")

    

#endregion


# region - Kontener na zawartosci
container = tk.Frame(root, bg=COLOR)
container.pack(fill="both", expand=True)

container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)
#endregion

# region - Rozdzielenie podstron
page1 = tk.Frame(container, bg=COLOR)   #strona glowna
page2 = tk.Frame(container, bg=COLOR)   #strona szyfrowania  
page3 = tk.Frame(container, bg=COLOR)   #strona odszyfrowywania

for box in (page1, page2, page3):
    box.grid(row=0, column=0, sticky="nsew")
#endregion

# region ==== Strona 1 ======
# Naglowek
header1 = tk.Label(
    page1, 
    text="𝖥𝗂𝗅𝖾 𝖤𝗇𝖼𝗋𝗒𝗉𝗍𝗈𝗋".upper(), 
    font=("Helvetica", 40, "bold"),
    anchor="center",
    bg=COLOR
)
header1.pack(pady=10)

frame1 = tk.Frame(page1, bg='white', width=8*COLUMN_WIDTH, height=10*ROW_HEIGHT)
frame1.grid_propagate(False)
frame1.pack(pady=10)

for i in range(2):
    frame1.columnconfigure(i, weight=1)
    frame1.rowconfigure(i, weight=1)

#Przycisk szyfrowania
enc_button = Custom_Button("Encrypt file", frame1, lambda: show_frame(page2))
enc_button.grid(row=0, column=0, sticky="s", pady=30)

#Przycisk szyfrowania
dec_button = Custom_Button("Decrypt file", frame1, lambda: show_frame(page3))
dec_button.grid(row=1, column=0, sticky="n", pady=30)

#Obraz
image = Image.open(r"File-Encryptor-GUI\icon.png")
image = image.resize((3*COLUMN_WIDTH, 6*ROW_HEIGHT))
image_object = ImageTk.PhotoImage(image)

label_img = tk.Label(frame1, image=image_object, bg="white")
label_img.image = image_object
label_img.grid(row=0, column=1, columnspan=2, rowspan=2, sticky="ew")

#Przycisk EXIT
exit_button = Back_Button("Exit", page1, lambda: exit())
exit_button.pack(pady=15)
#endregion


# region ==== Strona 2 ======
header2 = tk.Label(
    page2, 
    text="​𝐄𝐧𝐜𝐫𝐲𝐩𝐭𝐢𝐨𝐧".upper(), 
    font=("Helvetica", 40, "bold"),
    anchor="center",
    bg=COLOR
)
header2.pack(pady=10)

frame2 = tk.Frame(page2, bg='white', width=8*COLUMN_WIDTH, height=10*ROW_HEIGHT)
frame2.grid_propagate(False)
frame2.pack(pady=10)

for i in range(2):
    frame2.columnconfigure(i, weight=1)

choose_file_btt = Action_Button("File to encrypt", frame2, lambda: find_file(1))
choose_file_label = tk.Label(frame2, 
                             textvariable=PATH_1_var, 
                             font=("Helvetica", 10),
                             borderwidth=2,
                             relief="solid",
                             highlightbackground="black",
                             padx=5,
                             pady=2)

key_entry = tk.Entry(frame2, font=("Helvetica", 14), width=30, borderwidth=2,highlightbackground="black")
set_placeholder(key_entry, "Type your encryption key")
enc_file_btt = Action_Button("Encryption key file", frame2, lambda: find_file(2))
enc_file_label = tk.Label(frame2, 
                             textvariable=PATH_2_var, 
                             font=("Helvetica", 10),
                             borderwidth=2,
                             relief="solid",
                             highlightbackground="black",
                             padx=5,
                             pady=2)
encryption_btt = Custom_Button("Encrypt", frame2, lambda: encrypt(key_entry))


choose_file_btt.grid(column=0, row=0, sticky="nw", pady=(30,5), padx=30)
choose_file_label.grid(column=0, row=1, sticky="nw", padx=30)
key_entry.grid(column=0, row=2, sticky="nw", padx=30, pady=(60, 5), ipadx=5, ipady=2)
enc_file_btt.grid(column=0, row=3, sticky="nw", pady=(30,5), padx=30)
enc_file_label.grid(column=0, row=4, sticky="nw", padx=30)
encryption_btt.grid(column=0, row=5, sticky="sw", padx=30, pady=(80, 0))


#====== BACK ======
back_button2 = Back_Button("Back", page2, lambda: back())
back_button2.pack(pady=15)
#endregion

# region ==== Strona 3 ======
header3 = tk.Label(
    page3, 
    text="𝗗𝗲𝗰𝗿𝘆𝗽𝘁𝗶𝗼𝗻".upper(), 
    font=("Helvetica", 40, "bold"),
    anchor="center",
    bg=COLOR
)
header3.pack(pady=10)

frame3 = tk.Frame(page3, bg='white', width=8*COLUMN_WIDTH, height=10*ROW_HEIGHT)
frame3.grid_propagate(False)
frame3.pack(pady=10)

for i in range(2):
    frame3.columnconfigure(i, weight=1)



# przycik BACK
back_button3 = Back_Button("Back", page3, lambda: back())
back_button3.pack(pady=15)
#endregion

show_frame(page1)

root.mainloop()