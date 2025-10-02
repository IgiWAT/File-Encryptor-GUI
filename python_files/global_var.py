import tkinter as tk

origin_file_path = None
encryption_key_file_path = None
generated_encryption_key_file_path = None
ENCRYPTION_KEY = None

def init_variables(root):
    global origin_file_path, encryption_key_file_path, generated_encryption_key_file_path, ENCRYPTION_KEY

    origin_file_path = tk.StringVar(root, value="")
    encryption_key_file_path = tk.StringVar(root, value="")
    generated_encryption_key_file_path = tk.StringVar(root, value="")
    ENCRYPTION_KEY = tk.StringVar(root, value="")

COLUMN_WIDTH = 100
COLUMNS = 10
ROW_HEIGHT = 50
ROWS = 12
COLOR = "#E9EEF5"

img1 = "images\\icon.png"
img2 = "images\\padlock.png"
img3 = "images\\open.png"