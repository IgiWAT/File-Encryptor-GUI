# region ====== Imports ======
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

import python_files.classes as cls
import python_files.functions as fc
import python_files.global_var as var
#endregion

# region ====== Ustawienia ======

root = tk.Tk()
root.title("File Encryptor")
root.geometry("1000x700")
root.configure(bg=var.COLOR)

var.init_variables(root) # Zmienne globalne trzeba zainicjalizowac dopiero po utworzeniu glownego okna

#endregion

# region - Kontener na zawartosci
container = tk.Frame(root, bg=var.COLOR)
container.pack(fill="both", expand=True)

container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)
#endregion

# region - Rozdzielenie podstron
page1 = tk.Frame(container, bg=var.COLOR)   #strona glowna
page2 = tk.Frame(container, bg=var.COLOR)   #strona szyfrowania  
page3 = tk.Frame(container, bg=var.COLOR)   #strona odszyfrowywania

for box in (page1, page2, page3):
    box.grid(row=0, column=0, sticky="nsew")
#endregion

# region ==== Strona 1 ======
# Naglowek
header1 = cls.Header(page1, "𝖥𝗂𝗅𝖾 𝖤𝗇𝖼𝗋𝗒𝗉𝗍𝗈𝗋")
header1.pack(pady=10)

frame1 = tk.Frame(page1, bg='white', width=8*var.COLUMN_WIDTH, height=10*var.ROW_HEIGHT)
frame1.grid_propagate(False)
frame1.pack(pady=10)

for i in range(2):
    frame1.columnconfigure(i, weight=1)
    frame1.rowconfigure(i, weight=1)

#Przycisk szyfrowania
enc_button = cls.Custom_Button("Encrypt file", frame1, lambda: fc.show_frame(page2))
enc_button.grid(row=0, column=0, sticky="s", pady=30)

#Przycisk szyfrowania
dec_button = cls.Custom_Button("Decrypt file", frame1, lambda: fc.show_frame(page3))
dec_button.grid(row=1, column=0, sticky="n", pady=30)

#Obraz
image = Image.open(var.img1)
image = image.resize((3*var.COLUMN_WIDTH, 6*var.ROW_HEIGHT))
image_object = ImageTk.PhotoImage(image)

label_img = tk.Label(frame1, image=image_object, bg="white")
label_img.image = image_object
label_img.grid(row=0, column=1, columnspan=2, rowspan=2, sticky="ew")

#Przycisk EXIT
exit_button = cls.Back_Button("Exit", page1, lambda: fc.exit(root))
exit_button.pack(pady=15)
#endregion

# region ==== Strona 2 ======
#====== Header ======
header2 = cls.Header(page2, "​𝐄𝐧𝐜𝐫𝐲𝐩𝐭𝐢𝐨𝐧")
header2.pack(pady=10)

#====== Bialy kontener ======
frame2 = tk.Frame(page2, bg='white', width=8*var.COLUMN_WIDTH, height=10*var.ROW_HEIGHT)
frame2.grid_propagate(False)
frame2.pack(pady=10)

for i in range(2):
    frame2.columnconfigure(i, weight=1)

choose_file_btt = cls.Action_Button("File to encrypt", frame2, lambda: fc.find_file(1))
choose_file_label = cls.Path_label(frame2, var.PATH_1_var)

enc_file_btt = cls.Action_Button("Encryption key file", frame2, lambda: fc.find_file(2))
enc_file_label = cls.Path_label(frame2, var.PATH_2_var)

generate_key_btt = cls.Action_Button("Generate encryption key", frame2, lambda: fc.generate_key())
key_label = cls.Key_Label(frame2, var.ENCRYPTION_KEY)
use_btt = cls.Action_Button("Use", frame2, lambda: fc.use_file())
key_file_label = cls.Path_label(frame2, var.PATH_3_var)

encryption_btt = cls.Custom_Button("Encrypt", frame2, lambda: fc.encrypt())

#----------------- Strefa pakowania----------------
choose_file_btt.grid(column=0, row=0, sticky="nw", pady=(30,5), padx=30)
choose_file_label.grid(column=0, row=1, sticky="nw", padx=30)

enc_file_btt.grid(column=0, row=2, sticky="nw", pady=(30,5), padx=30)
enc_file_label.grid(column=0, row=3, sticky="nw", padx=30)

generate_key_btt.grid(column=0, row=4, sticky="nw", pady=(30,5), padx=30)
key_label.grid(column=0, row=5, sticky="nw", padx=30, ipady=3)
use_btt.grid(column=0, row=6, sticky="w", padx=30, pady=3)
key_file_label.grid(column=0, row=7, sticky="w", padx=30)

encryption_btt.grid(column=0, row=8, sticky="sw", padx=30, pady=(30, 0))


#---------------- Obraz ----------------
image2 = Image.open(var.img2)
image2 = image2.resize((3*var.COLUMN_WIDTH, 6*var.ROW_HEIGHT))
image_object2 = ImageTk.PhotoImage(image2)

label_img2 = tk.Label(frame2, image=image_object2, bg="white")
label_img2.image = image_object2
label_img2.grid(row=0, column=1, rowspan=9, columnspan=1, sticky="nswe")

#====== BACK ======
back_button2 = cls.Back_Button("Back", page2, lambda: fc.back(page1))
back_button2.pack(pady=15)
#endregion

# region ==== Strona 3 ======
header3 = cls.Header(page3, "𝗗𝗲𝗰𝗿𝘆𝗽𝘁𝗶𝗼𝗻")
header3.pack(pady=10)

# ======== Bialy kontener =======
frame3 = tk.Frame(page3, bg='white', width=8*var.COLUMN_WIDTH, height=10*var.ROW_HEIGHT)
frame3.grid_propagate(False)
frame3.pack(pady=10)

for i in range(2):
    frame3.columnconfigure(i, weight=1)
frame3.rowconfigure(5, weight=1)

choose_file_btt_3 = cls.Action_Button("Encrypted file", frame3, lambda: fc.find_file(1))
choose_file_label_3 = cls.Path_label(frame3, var.PATH_1_var)

dec_file_btt = cls.Action_Button("Encryption key file", frame3, lambda: fc.find_file(2))
dec_file_label = cls.Path_label(frame3, var.PATH_2_var)

key_entry = cls.Key_Entry(frame3)

decryption_btt = cls.Custom_Button("Decrypt", frame3, lambda: fc.decrypt())

#----------------- Strefa pakowania----------------
choose_file_btt_3.grid(column=0, row=0, sticky="nw", pady=(30,5), padx=30)
choose_file_label_3.grid(column=0, row=1, sticky="nw", padx=30)

dec_file_btt.grid(column=0, row=2, sticky="nw", pady=(30,5), padx=30)
dec_file_label.grid(column=0, row=3, sticky="nw", padx=30)

key_entry.grid(column=0, row=4, sticky="nw", pady=(30,5), padx=30, ipadx=5, ipady=3)
fc.set_entry(key_entry)

decryption_btt.grid(column=0, row=5, sticky="sw", padx=30, pady=(0, 20))


#---------------- Obraz ----------------
image3 = Image.open(var.img3)
image3 = image3.resize((3*var.COLUMN_WIDTH, 6*var.ROW_HEIGHT))
image_object3 = ImageTk.PhotoImage(image3)

label_img3 = tk.Label(frame3, image=image_object3, bg="white")
label_img3.image = image_object3
label_img3.grid(row=0, column=1, rowspan=6, columnspan=1, sticky="nswe")

#====== BACK ======
back_button3 = cls.Back_Button("Back", page3, lambda: fc.back(page1))
back_button3.pack(pady=15)
#endregion

fc.show_frame(page1)
root.mainloop()