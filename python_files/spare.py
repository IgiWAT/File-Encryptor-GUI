txt = "B0D8wUCROvgUUOFbXFD5sqcsB6jvSdAHcrQt3pK3b84="
print(len(txt))

'''
    def is_valid_base64_urlsafe_2(P, s, entry, root):
    # !!! funkcja wywołuje się tylko jednorazowo
        allowed_chars = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=-_")
        # P - cala wartosc pola,   s - poprzednia wartosc pola
        if P == entry.placeholder:
            if s==placeholder or s=="":
                entry.delete(0, tk.END)
                entry.config(fg="black")
                return True
            else:
                root.focus_set()
                s = ""
                set_initial_entry(entry)
                var.ENCRYPTION_KEY.set("")
                return True
        elif len(P) <= 44 and all(char in allowed_chars for char in P):
            entry.config(fg="black")  # Czarny tekst dla poprawnych znaków
            var.ENCRYPTION_KEY.set(P)
            set_entry_green(entry)  # Zielone obramowanie
            return True
        else:
            set_entry_red(entry)
            return False
        
    reg = root.register(is_valid_base64_urlsafe_2)    
    
    entry.config(
        bg="white",
        highlightthickness=2,
        highlightbackground="black",
        highlightcolor="black",
        borderwidth=2,
        relief="flat",
        validate="key",
        validatecommand=(reg, '%P', '%s')
    )'''
