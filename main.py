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
root.geometry("1000x800")
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

frame1 = tk.Frame(page1, bg='white', width=8*var.COLUMN_WIDTH, height=12*var.ROW_HEIGHT)
frame1.grid_propagate(False)
frame1.pack(pady=10)

for i in range(2):
    frame1.columnconfigure(i, weight=1)
    frame1.rowconfigure(i, weight=1)

#Przycisk szyfrowania
enc_button = cls.Custom_Button("Encrypt file", frame1, lambda: fc.show_frame(page2))
enc_button.grid(row=0, column=0, sticky="s", pady=30)

#Przycisk deszyfrowania
dec_button = cls.Custom_Button("Decrypt file", frame1, lambda: fc.show_frame(page3))
dec_button.grid(row=1, column=0, sticky="n", pady=30)

#Obraz
image1 = Image.open(fc.resource_path(var.img1))
image1 = image1.resize((3*var.COLUMN_WIDTH, 6*var.ROW_HEIGHT))
image_object = ImageTk.PhotoImage(image1)

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
frame2 = tk.Frame(page2, bg='white', width=8*var.COLUMN_WIDTH, height=12*var.ROW_HEIGHT)
frame2.grid_propagate(False)
frame2.pack(pady=10)

for i in range(2):
    frame2.columnconfigure(i, weight=1)

choose_file_btt = cls.Action_Button("File to encrypt", frame2, lambda: fc.find_file(1))
dec_choose_file_label = cls.Key_Label(frame2, var.origin_file_path)
delete_btt_1 = cls.Small_Button("Cancel file", frame2, lambda: fc.cancel_path(1))

enc_file_btt = cls.Action_Button("Encryption key file", frame2, lambda: fc.find_file(2))
enc_file_label = cls.Key_Label(frame2, var.encryption_key_file_path)
delete_btt_2 = cls.Small_Button("Cancel file", frame2, lambda: fc.cancel_path(2))

or_gap = cls.Gap(frame2, text="or")
#====== Strefa generowania klucza ======
generate_key_btt = cls.Action_Button("Generate encryption key", frame2, lambda: fc.generate_key())
key_label = cls.Key_Label(frame2, var.ENCRYPTION_KEY)

frame_three_buttons = tk.Frame(frame2, bg='white')
for i in range(3):
    frame_three_buttons.columnconfigure(i, weight=1)

save_btt = cls.Small_Button("Save", frame_three_buttons, lambda: fc.save_file())
copy_btt = cls.Small_Button("Copy", frame_three_buttons, lambda: fc.copy_key())
delete_btt_3 = cls.Small_Button("Cancel", frame_three_buttons, lambda: fc.cancel_path(3))

encryption_btt = cls.Custom_Button("Encrypt", frame2, lambda: fc.encrypt())

#----------------- Strefa pakowania----------------
choose_file_btt.grid(column=0, row=0, sticky="nw", pady=(30,5), padx=30)
dec_choose_file_label.grid(column=0, row=1, sticky="nw", pady=(0, 5), padx=30)
delete_btt_1.grid(column=0, row=2, sticky="nw", pady=(0, 15), padx=30)

enc_file_btt.grid(column=0, row=3, sticky="nw", pady=(30,5), padx=30)
enc_file_label.grid(column=0, row=4, sticky="nw", pady=(0,5), padx=30)
delete_btt_2.grid(column=0, row=5, sticky="nw", padx=30)

or_gap.grid(column=0, row=6, sticky="ew", pady=20)

generate_key_btt.grid(column=0, row=7, sticky="nw", pady=(0,5), padx=30)
key_label.grid(column=0, row=8, sticky="nw", padx=30, ipady=3)
frame_three_buttons.grid(column=0, row=9, sticky="w", padx=30, pady=3)

save_btt.grid(column=0, row=0, sticky="w", padx=(0, 10))
copy_btt.grid(column=1, row=0, sticky="w", padx=(0, 10))
delete_btt_3.grid(column=2, row=0, sticky="w")

encryption_btt.grid(column=0, row=10, sticky="sw", padx=30, pady=(40, 0))


#---------------- Obraz ----------------
image2 = Image.open(fc.resource_path(var.img2))
image2 = image2.resize((3*var.COLUMN_WIDTH, 6*var.ROW_HEIGHT))
image_object2 = ImageTk.PhotoImage(image2)

label_img2 = tk.Label(frame2, image=image_object2, bg="white")
label_img2.image = image_object2
label_img2.grid(row=0, column=1, rowspan=10, columnspan=1, sticky="nswe")

#====== BACK ======
back_button2 = cls.Back_Button("Back", page2, lambda: fc.back(page1))
back_button2.pack(pady=15)
#endregion

# region ==== Strona 3 ======
header3 = cls.Header(page3, "𝗗𝗲𝗰𝗿𝘆𝗽𝘁𝗶𝗼𝗻")
header3.pack(pady=10)

# ======== Bialy kontener =======
frame3 = tk.Frame(page3, bg='white', width=8*var.COLUMN_WIDTH, height=12*var.ROW_HEIGHT)
frame3.grid_propagate(False)
frame3.pack(pady=10)

for i in range(2):
    frame3.columnconfigure(i, weight=1)

dec_choose_file_btt = cls.Action_Button("Encrypted file", frame3, lambda: fc.find_file(1))
dec_choose_file_label_3 = cls.Key_Label(frame3, var.origin_file_path)
dec_delete_btt_1 = cls.Small_Button("Cancel file", frame3, lambda: fc.cancel_path(1))

dec_file_btt = cls.Action_Button("Encryption key file", frame3, lambda: fc.find_file(2))
dec_file_label = cls.Key_Label(frame3, var.encryption_key_file_path)
dec_delete_btt_2 = cls.Small_Button("Cancel file", frame3, lambda: fc.cancel_path(2))

dec_or_gap = cls.Gap(frame3, text="or")

key_entry = cls.Key_Entry(frame3)

dec_frame_three_buttons = tk.Frame(frame3, bg='white')
for i in range(3):
    dec_frame_three_buttons.columnconfigure(i, weight=1)

dec_save_btt = cls.Small_Button("Save", dec_frame_three_buttons, lambda: fc.save_file())
dec_copy_btt = cls.Small_Button("Copy", dec_frame_three_buttons, lambda: fc.copy_key())
dec_delete_btt_3 = cls.Small_Button("Cancel", dec_frame_three_buttons, lambda: fc.cancel_path(3))

decryption_btt = cls.Custom_Button("Decrypt", frame3, lambda: fc.decrypt())

#----------------- Strefa pakowania----------------
dec_choose_file_btt.grid(column=0, row=0, sticky="nw", pady=(30,5), padx=30)
dec_choose_file_label_3.grid(column=0, row=1, sticky="nw", pady=(0, 5), padx=30)
dec_delete_btt_1.grid(column=0, row=2, sticky="nw", pady=(0, 15), padx=30)

dec_file_btt.grid(column=0, row=3, sticky="nw", pady=(30,5), padx=30)
dec_file_label.grid(column=0, row=4, sticky="nw", pady=(0,5), padx=30)
dec_delete_btt_2.grid(column=0, row=5, sticky="nw", padx=30)

dec_or_gap.grid(column=0, row=6, sticky="ew", pady=20)

key_entry.grid(column=0, row=7, sticky="nw", pady=(0,5), padx=30, ipadx=5, ipady=3)
fc.set_entry(key_entry)

dec_frame_three_buttons.grid(column=0, row=8, sticky="w", padx=30, pady=3)
dec_save_btt.grid(column=0, row=0, sticky="w", padx=(0, 10))
dec_copy_btt.grid(column=1, row=0, sticky="w", padx=(0, 10))
dec_delete_btt_3.grid(column=2, row=0, sticky="w")

decryption_btt.grid(column=0, row=9, sticky="sw", padx=30, pady=(80, 0))


#---------------- Obraz ----------------
image3 = Image.open(fc.resource_path(var.img3))
image3 = image3.resize((3*var.COLUMN_WIDTH, 6*var.ROW_HEIGHT))
image_object3 = ImageTk.PhotoImage(image3)

label_img3 = tk.Label(frame3, image=image_object3, bg="white")
label_img3.image = image_object3
label_img3.grid(row=0, column=1, rowspan=9, columnspan=1, sticky="nswe")

#====== BACK ======
back_button3 = cls.Back_Button("Back", page3, lambda: fc.back(page1))
back_button3.pack(pady=15)
#endregion

fc.show_frame(page1)
root.mainloop()