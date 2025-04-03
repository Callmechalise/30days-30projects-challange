import tkinter as tk
from tkinter.filedialog import askopenfilename,asksaveasfilename
from tkinter import END



def openf():
    filepath=askopenfilename(
        filetypes=[('Text Files','*.txt'),('All Files','*.*')]
    )
    if not filepath:
        return
    txtwin.delete(1.0,END)
    with open(filepath,"r") as file:
        text=file.read()
        txtwin.insert(END,text)
    win.title(f"Notepad-{filepath}")

def save():
    filepath=asksaveasfilename(
        defaultextension="txt",
        filetypes=[('Text Files','*.txt'),('All Files','*.*')]

    )
    if not filepath:
        return
    with open(filepath,"w") as file:
        text=txtwin.get(1.0,END)
        file.write(text)
    win.title(f"Notepad-{filepath}")

win=tk.Tk()
win.title("Notepad")
win.rowconfigure(0,minsize=600,weight=1)
win.columnconfigure(1,minsize=800,weight=1)

txtwin=tk.Text(win)
frame=tk.Frame(win,relief=tk.RAISED,bd=2)
button_open=tk.Button(frame,relief=tk.SOLID,text="Open",command=openf)
button_save=tk.Button(frame,relief=tk.SOLID,text="Save As",command=save)

button_open.grid(row=0,column=0,sticky='ew',padx=10,pady=10)
button_save.grid(row=1,column=0,sticky='ew',padx=10,pady=10)
frame.grid(row=0,column=0,sticky="ns")
txtwin.grid(row=0,column=1,sticky="nsew")
win.mainloop()