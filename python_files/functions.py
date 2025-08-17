from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
from cryptography.fernet import Fernet

import python_files.global_var as var

# region ====== Funkcje =======

# Wyswietlenie wskazanej podstrony
def show_frame(frame):
    frame.tkraise()

# Zamyka cała aplikację
def exit(root):
    root.destroy()

# Cofa o jedna strone do tylu
def back(page): 
    show_frame(page)

# Znajduje sciezke do pliku i w zaleznosci od opcji zapisuje w zmiennej globalnej
def find_file(option):
    path = filedialog.askopenfilename(title="Find file to encrypt",
        initialdir=os.getcwd() #otworzy sie w katalagu w ktorym jestesmy
        )
    if option==1: var.PATH_1_var.set(path)
    elif option==2: var.PATH_2_var.set(path)

def generate_key():
    var.ENCRYPTION_KEY.set(Fernet.generate_key().decode('utf-8'))
    #trzeba zdekodowac klucz bo inaczej bedzie w bajtach

def use_file():
    if var.ENCRYPTION_KEY.get() != "":
        file_path = filedialog.asksaveasfilename(
            defaultextension=".key",
            filetypes=[("Key files", "*key")],
            title="Zapisz plik z kluczem"
        )
        #Zapisywanie do pliku
        if file_path:  # jeśli użytkownik nie anulował
            with open(file_path, "wb") as f:
                f.write(var.ENCRYPTION_KEY.get().encode("utf-8"))
                var.PATH_3_var.set(file_path)
        else:
            messagebox.showerror("Error", "Saving cancelled")
    else:
        messagebox.showerror("Error", "First generate key")

def find_extension(path):
    dot_pos = path.rfind(".")
    ext = path[dot_pos:] #zwraca reszte znakow po podanej pozycji
    return ext

def set_default():
    var.PATH_1_var.set("")
    var.PATH_2_var.set("")
    var.PATH_3_var.set("")
    var.ENCRYPTION_KEY.set("")

def set_entry(entry):
    placeholder = "Encryption key"
    entry.insert(0, placeholder)
    entry.config(fg="grey")

    def on_focus_in(event):
         if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg="black")

    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(fg="grey")
        else:
            var.ENCRYPTION_KEY.set(entry.get())

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

def encrypt():
    path1 = var.PATH_1_var.get().strip()
    path2 = var.PATH_2_var.get().strip()
    path3 = var.PATH_3_var.get().strip()

    if path1 != "":
        if path2 != "" or path3 != "":
            if path2 != "" and  path3 != "":
                messagebox.showerror("Error", "Choose ONLY ONE way to encrypt file")
            else:
                key = "" 
                plain_text = ""
                
                with open(path1, 'rb') as origin:
                    plain_text = origin.read()

                if path2!="": 
                    with open(path2, "rb") as keyfile:
                        key=keyfile.read()
                else:
                    with open(path3, "rb") as keyfile:
                        key=keyfile.read()

                # Tworzy instancję obiektu Fernet, która bedzie uzywana do szyfrowania i deszyfrowania danych
                f = Fernet(key)

                file_path = filedialog.asksaveasfilename(
                    defaultextension=find_extension(path1),
                    title = "Zapisz zaszyfrowany plik"
                )

                if file_path:
                    with open(file_path, "wb") as enc_file:
                        encrypted = f.encrypt(plain_text)
                        enc_file.write(encrypted)
                        messagebox.showinfo("Good job", "File has been sucessfully encrypted")

                        set_default()
                else:
                    messagebox.showerror("Error", "Saving cancelled")

        else: messagebox.showerror("Error", "Choose way to encrypt file")
    else: messagebox.showerror("Error", "Choose file to encrypt")


def decrypt():
    path1 = var.PATH_1_var.get().strip()
    path2 = var.PATH_2_var.get().strip()
    key = var.ENCRYPTION_KEY.get().strip()
    print(path1)
    print(path2)
    print(key)

    if path1 != "":
            if (path2 != "" and key != ""):
                messagebox.showerror("Error", "Choose ONLY ONE way to decrypt file")
            elif (path2 == "" and key == ""):
                messagebox.showerror("Error", "You must provide key (file or text)")
            else:
                key = key.encode("utf-8")
                ciphered_text = ""
                
                with open(path1, 'rb') as origin:
                    ciphered_text = origin.read()

                if path2 != "":
                    with open(path2, "rb") as keyfile:
                        key=keyfile.read()
                else: pass

                # Tworzy instancję obiektu Fernet, która bedzie uzywana do szyfrowania i deszyfrowania danych
                f = Fernet(key)

                file_path = filedialog.asksaveasfilename(
                    defaultextension=find_extension(path1),
                    title = "Zapisz odszyfrowany plik"
                )

                if file_path:
                    with open(file_path, "wb") as dec_file:
                        decrypted = f.decrypt(ciphered_text)
                        dec_file.write(decrypted)
                        messagebox.showinfo("Good job", "File has been sucessfully decrypted")

                        set_default()
                else:
                    messagebox.showerror("Error", "Saving cancelled")
    else: messagebox.showerror("Error", "Choose file to decrypt")
 

#endregion