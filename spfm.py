# OpenAI ChatGPT generatd various portions of the code below.

import tkinter as tk
import tkinter.filedialog
import os
import shutil
import tkinter.ttk

def choose_src_dir():
    src_dir = tkinter.filedialog.askdirectory(title="Select Source Directory")
    src_entry.insert(0, src_dir)

def choose_dst_dir():
    dst_dir = tkinter.filedialog.askdirectory(title="Select Destination Directory")
    dst_entry.insert(0, dst_dir)

def move_files():
    src = src_entry.get()
    dst = dst_entry.get()
    progress_bar["maximum"] = 100
    for i, filename in enumerate(os.listdir(src)):
        src_file = os.path.join(src, filename)
        dst_file = os.path.join(dst, filename)
        shutil.move(src_file, dst_file)
        progress = int((i + 1) * 100 / len(os.listdir(src)))
        progress_bar["value"] = progress
        root.update()

root = tk.Tk()
root.geometry("500x200")
root.title("File Mover")

src_label = tk.Label(root, text="Source Directory:")
src_label.grid(row=0, column=0, padx=5, pady=5)

src_entry = tk.Entry(root)
src_entry.grid(row=0, column=1, padx=5, pady=5)

src_button = tk.Button(root, text="Choose", command=choose_src_dir)
src_button.grid(row=0, column=2, padx=5, pady=5)

dst_label = tk.Label(root, text="Destination Directory:")
dst_label.grid(row=1, column=0, padx=5, pady=5)

dst_entry = tk.Entry(root)
dst_entry.grid(row=1, column=1, padx=5, pady=5)

dst_button = tk.Button(root, text="Choose", command=choose_dst_dir)
dst_button.grid(row=1, column=2, padx=5, pady=5)

progress_bar = tkinter.ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
progress_bar.grid(row=2, column=1, padx=5, pady=5)

move_button = tk.Button(root, text="Move Files", command=move_files)
move_button.grid(row=3, column=1, padx=5, pady=5)

root.mainloop()
