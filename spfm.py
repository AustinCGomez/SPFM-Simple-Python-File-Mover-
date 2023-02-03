# OpenAI ChatGPT generated the initial version of this code. 

import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
import shutil

def select_src_folder():
    src_folder = tk.filedialog.askdirectory(title='Select Source Folder')
    src_folder_label.config(text=src_folder)

def select_dest_folder():
    dest_folder = tk.filedialog.askdirectory(title='Select Destination Folder')
    dest_folder_label.config(text=dest_folder)

def move_files():
    src_folder = src_folder_label['text']
    dest_folder = dest_folder_label['text']

    if src_folder == 'No folder selected' or dest_folder == 'No folder selected':
        tk.messagebox.showerror('Error', 'Please select both source and destination folders')
        return

    files = tk.filedialog.askopenfilenames(title='Select files', initialdir=src_folder)
    for file in files:
        shutil.move(file, dest_folder)
    tk.messagebox.showinfo('Success', 'Files moved successfully')

app = tk.Tk()
app.title('File Mover')

src_folder_label = tk.Label(text='No folder selected', width=30)
src_folder_label.grid(row=0, column=0, padx=10, pady=10)

select_src_folder_button = tk.Button(text='Select Source Folder', command=select_src_folder)
select_src_folder_button.grid(row=0, column=1, padx=10, pady=10)

dest_folder_label = tk.Label(text='No folder selected', width=30)
dest_folder_label.grid(row=1, column=0, padx=10, pady=10)

select_dest_folder_button = tk.Button(text='Select Destination Folder', command=select_dest_folder)
select_dest_folder_button.grid(row=1, column=1, padx=10, pady=10)

move_files_button = tk.Button(text='Move Files', command=move_files)
move_files_button.grid(row=2, column=0, columnspan=2, pady=10)

app.mainloop()
