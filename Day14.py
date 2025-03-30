import sys

import PyPDF2
from PyPDF2 import PdfWriter
import tkinter as tk
from tkinter import filedialog,Label
#Basic merge

def select_file():
        filepaths=filedialog.askopenfilenames(title="Select a File")
        if filepaths:
            label.config(text=f"File selected:\n"+"\n".join(filepaths))
            return filepaths


root = tk.Tk()
root.title("File Selector")
btn = tk.Button(root, text="Browse Files", command=select_file)
btn.pack(pady=10)
label = tk.Label(root, text="No file selected", wraplength=400)
label.pack(pady=10)



merger=PdfWriter()
list=select_file()
for pdf in list:
    merger.append(pdf)
merger.write('Mergedpdf')
merger.close()
sys.exit()
root.mainloop()
