import tkinter as tk
from tkinter import filedialog
import shutil

def choose_src_folder():
    global src_folder
    src_folder = filedialog.askdirectory()

def choose_dst_folder():
    global dst_folder
    dst_folder = filedialog.askdirectory()

def move_files():
    shutil.move(src_folder, dst_folder)

root = tk.Tk()
root.geometry("800x800")
root.title("File Mover")

src_folder = ""
dst_folder = ""

src_label = tk.Label(root, text="From:")
src_label.pack()

src_entry = tk.Entry(root, textvariable=src_folder)
src_entry.pack()

src_button = tk.Button(root, text="Choose Source Folder", command=choose_src_folder)
src_button.pack()

dst_label = tk.Label(root, text="To:")
dst_label.pack()

dst_entry = tk.Entry(root, textvariable=dst_folder)
dst_entry.pack()

dst_button = tk.Button(root, text="Choose Destination Folder", command=choose_dst_folder)
dst_button.pack()

move_button = tk.Button(root, text="Move Files", command=move_files)
move_button.pack()

root.mainloop()
