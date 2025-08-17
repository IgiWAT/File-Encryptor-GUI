import tkinter as tk

PATH_1_var = None
PATH_2_var = None
PATH_3_var = None
ENCRYPTION_KEY = None

def init_variables(root):
    global PATH_1_var, PATH_2_var, PATH_3_var, ENCRYPTION_KEY

    PATH_1_var = tk.StringVar(root, value="")
    PATH_2_var = tk.StringVar(root, value="")
    PATH_3_var = tk.StringVar(root, value="")
    ENCRYPTION_KEY = tk.StringVar(root, value="")

COLUMN_WIDTH = 100
COLUMNS = 10
ROW_HEIGHT = 50
ROWS = 12
COLOR = "#E9EEF5"

img1 = r"File-Encryptor-GUI\images\icon.png"
img2 = r"File-Encryptor-GUI\images\padlock.png"
img3 = r"File-Encryptor-GUI\images\open.png"