from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import sys
from cryptography.fernet import Fernet
import clipboard

import python_files.global_var as var

# region ====== Funkcje =======

def resource_path(relative_path):
    """
    Zwraca poprawną ścieżkę zarówno w trybie skryptu (.py),
    jak i spakowanego pliku (.exe)
    """
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller rozpakowuje dane do folderu tymczasowego
        return os.path.join(sys._MEIPASS, relative_path)
    else:
        return os.path.join(os.path.abspath("."), relative_path)


# Wyswietlenie wskazanej podstrony
def show_frame(frame):
    frame.tkraise()

# Zamyka cała aplikację
def exit(root):
    root.destroy()

# Cofa o jedna strone do tylu
def back(page): 
    show_frame(page)
    set_default()

def check_path():
    if var.INITIAL_DIRECTORY.get() =="" or not os.path.isdir(var.INITIAL_DIRECTORY.get()):
        var.INITIAL_DIRECTORY.set(os.getcwd())
    else: pass

# Znajduje sciezke do pliku i w zaleznosci od opcji zapisuje w zmiennej globalnej
def find_file(option):
    check_path()

    if option==1: #Dla szukania pliku do szyfrowania/odszyfrowania
        file_path = filedialog.askopenfilename(title="Find file to encrypt",
        initialdir=var.INITIAL_DIRECTORY.get()
        )

        var.origin_file_path.set(file_path)

        # Ustawienie katalogu w ktorym znajdowal sie poprzedni plik jako ten domyslny
        var.INITIAL_DIRECTORY.set(os.path.dirname(file_path))

    elif option==2: #Dla szukania pliku z kluczem
        while True:
            check_path()
            file_path = filedialog.askopenfilename(title="Find encryption key file",
            initialdir=var.INITIAL_DIRECTORY.get()
            ) 

            file_extension = os.path.splitext(file_path)[1] # Wyciaga rozszerzenie pliku

            if file_extension == ".key":
                var.encryption_key_file_path.set(file_path)
                var.INITIAL_DIRECTORY.set(os.path.dirname(file_path))
                break
            elif file_path=="": # jeżeli użytkownik kliknie "Anuluj" to nie wyskoczy błąd
                break
            else:
                messagebox.showerror("Error", "File with encryption key must be \".key\" extension file")
            
def generate_key():
    var.ENCRYPTION_KEY.set(Fernet.generate_key().decode('utf-8'))
    #trzeba zdekodowac klucz bo inaczej bedzie w bajtach

def save_file():
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
                var.encryption_key_file_path.set(file_path)
        else:
            messagebox.showerror("Error", "Saving cancelled")
        var.ENCRYPTION_KEY.set("")
    else:
        messagebox.showerror("Error", "First generate key")

def find_extension(path):
    dot_pos = path.rfind(".")
    ext = path[dot_pos:] #zwraca reszte znakow po podanej pozycji
    return ext

def set_default():
    var.origin_file_path.set("")
    var.encryption_key_file_path.set("")
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
    origin_file_path = var.origin_file_path.get().strip()
    encryption_key_file_path = var.encryption_key_file_path.get().strip()

    if origin_file_path != "":
        if os.path.isfile(origin_file_path):
            if encryption_key_file_path != "":
                if os.path.isfile(encryption_key_file_path):
                
                    key = "" 
                    plain_text = ""
                    
                    with open(origin_file_path, 'rb') as origin:
                        plain_text = origin.read()

                    with open(encryption_key_file_path, "rb") as keyfile:
                        key=keyfile.read()

                    # Tworzy instancję obiektu Fernet, która bedzie uzywana do szyfrowania i deszyfrowania danych
                    f = Fernet(key)

                    file_path = filedialog.asksaveasfilename(
                        defaultextension=find_extension(origin_file_path),
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

                else: messagebox.showerror("Error", "Check if \"Encryption key file\" still available on the computer")
            else: messagebox.showerror("Error", "Choose file with encryption key")
        else: messagebox.showerror("Error", "Check if \"File to encrypt\" still available on the computer")
    else: messagebox.showerror("Error", "Choose file to encrypt")


def decrypt():
    origin_file_path = var.origin_file_path.get().strip()
    encryption_key_file_path = var.encryption_key_file_path.get().strip()
    key = var.ENCRYPTION_KEY.get().strip()

    if origin_file_path != "":
            if (encryption_key_file_path != "" and key != ""):
                messagebox.showerror("Error", "Choose ONLY ONE way to decrypt file")
            elif (encryption_key_file_path == "" and key == ""):
                messagebox.showerror("Error", "You must provide key (file or text)")
            else:
                key = key.encode("utf-8")
                ciphered_text = ""
                
                with open(origin_file_path, 'rb') as origin:
                    ciphered_text = origin.read()

                if encryption_key_file_path != "":
                    with open(encryption_key_file_path, "rb") as keyfile:
                        key=keyfile.read()
                else: pass

                # Tworzy instancję obiektu Fernet, która bedzie uzywana do szyfrowania i deszyfrowania danych
                f = Fernet(key)

                file_path = filedialog.asksaveasfilename(
                    defaultextension=find_extension(origin_file_path),
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
 
def cancel_path(option):
    if option==1:
        var.origin_file_path.set("")
    elif option==2:
        var.encryption_key_file_path.set("")
    elif option==3:
        var.ENCRYPTION_KEY.set("")
    else: pass

def copy_key():
    clipboard.copy(var.ENCRYPTION_KEY.get().strip())
#endregion