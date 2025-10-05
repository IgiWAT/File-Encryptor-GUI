import tkinter as tk
import os

origin_file_path = None
encryption_key_file_path = None
ENCRYPTION_KEY = None
INITIAL_DIRECTORY = None

def init_variables(root):
    global origin_file_path, encryption_key_file_path, ENCRYPTION_KEY, INITIAL_DIRECTORY

    origin_file_path = tk.StringVar(root, value="")
    encryption_key_file_path = tk.StringVar(root, value="")
    ENCRYPTION_KEY = tk.StringVar(root, value="")
    INITIAL_DIRECTORY = tk.StringVar(root, value="")

COLUMN_WIDTH = 100
COLUMNS = 10
ROW_HEIGHT = 50
ROWS = 12
COLOR = "#E9EEF5"

img1 = os.path.join(*["images", "icon.png"]) # * -rozpakowywuje liste na oddzielne argumenty
img2 = os.path.join(*["images", "padlock.png"])
img3 = os.path.join(*["images", "open.png"])