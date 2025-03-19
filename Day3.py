import string
import random
import customtkinter
from tkinter import END

def weak():
    s1 = string.ascii_lowercase  # small abcd 26
    s2 = string.ascii_uppercase  # Capital abcd 26
    s3 = string.digits  # 0 dekhi 9
    s4 = string.punctuation  # special characters
    s5 = string.whitespace
    lenp = 8
    s = []
    s.extend(list(s1))  # Extend le garda repeat hunna
    s.extend(list(s2))
    s.extend(list(s3))
    random.shuffle(s)
    entryfield.insert(END,"".join(s[0:lenp]))
def strong():
    s1 = string.ascii_lowercase  # small abcd 26
    s2 = string.ascii_uppercase  # Capital abcd 26
    s3 = string.digits  # 0 dekhi 9
    s4 = string.punctuation  # special characters
    s5 = string.whitespace
    lenp = 8
    s = []
    s.extend(list(s1))#Extend le garda repeat hunna
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    s.extend(list(s5))
    random.shuffle(s)
    entryfield.insert(END,"".join(s[0:lenp]))
def clear():
    entryfield.delete(0,END)
#GUI PART
win=customtkinter.CTk()
win.title("Password Generator")
win.config(bg="White")
win.geometry("320x160")
cfont=("Arial", 16, "bold")
tcolor='Black'
bgcolor='White'
entryfield=customtkinter.CTkEntry(win,font=cfont,text_color=tcolor,fg_color=bgcolor,
border_color='Black',width=300,height=50)
entryfield.grid(row=0,column=0,columnspan=3)


bstrong=customtkinter.CTkButton(win,text='Strong',font=cfont,bg_color=bgcolor,width=150,height=50,
cursor='hand2',hover_color='blue3',command=strong)
bstrong.grid(row=1,column=0,pady=5,padx=5)

bweak=customtkinter.CTkButton(win,text='Weak',font=cfont,bg_color=bgcolor,width=150,height=50,
cursor='hand2',hover_color='blue3',command=weak)
bweak.grid(row=1,column=1,pady=5,padx=5)

bclear=customtkinter.CTkButton(win,text='clear',font=cfont,fg_color="red",width=80,
cursor='hand2',hover_color='red3',command=clear)
bclear.grid(row=2,column=0,columnspan=2,pady=5,padx=5)

win.mainloop()