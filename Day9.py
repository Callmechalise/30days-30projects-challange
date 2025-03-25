import tkinter as tk
import requests
import customtkinter
from tkinter import END


def search():
    try:
        word=entryfield.get()
        response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
        response.raise_for_status()
        response = response.json()
        meanings = response[0]["meanings"]
        meaning = meanings[0]

        output = []
        output.append(f"Part of Speech: {meaning['partOfSpeech']}\n")
        for definition in meaning["definitions"]:
            output.append(f"Definition: {definition['definition']}")
            if 'example' in definition:
                output.append(f"Example: {definition['example']}\n")
        text_box.delete(1.0,END)
        text_box.insert(tk.END, '\n'.join(output))
    except:
        text_box.delete(1.0,END)
        text_box.insert(tk.END, 'Oops Error')

win=tk.Tk()
win.title("DICTIONARY")
win.geometry("500x300")
entryfield=customtkinter.CTkEntry(win,font=("arial",16,"bold"),text_color="black",fg_color="white",
border_color='black',width=350,height=50)
entryfield.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

bsearch=customtkinter.CTkButton(win,text='Find',font=("arial",16,"bold"),bg_color="white",width=100,
cursor='hand2',height=50,fg_color="green",hover_color="green4",command=search)
bsearch.grid(row=0,column=4,pady=5)



text_box = tk.Text(win, height=12, width=45,bg='lightyellow')
text_box.grid(row=2, column=0, columnspan=4, pady=10, padx=10)


win.mainloop()
