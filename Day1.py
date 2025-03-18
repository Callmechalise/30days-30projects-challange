#this project will teach basic tkinter and properuse of eval function
#gui calculator
import customtkinter
from tkinter import END,messagebox
def clear():
    entryfield.delete(0,END)
def click(num):
    entryfield.insert(END,num)
def answer():
    try:
        expression=entryfield.get()
        ans=eval(expression)
        entryfield.delete(0,END)
        entryfield.insert(END,round(ans,2))
    except SyntaxError:
        messagebox.showerror('Error','Syntax mila na moraaa!')
    except ZeroDivisionError:
        messagebox.showerror('Harey','Infinity moraaa')
    except Exception as e:
        messagebox.showerror(e)
#gui part
win=customtkinter.CTk()
win.title("Calculator")
win.geometry("390x290")
win.config(bg="black")
cfont=("Arial", 16, "bold")
tcolor='white'
bgcolor='black'
entryfield=customtkinter.CTkEntry(win,font=cfont,text_color=tcolor,fg_color=bgcolor,
border_color='blue',width=390,height=50)
entryfield.grid(row=0,column=0,columnspan=4)

b7=customtkinter.CTkButton(win,text='7',font=cfont,bg_color=bgcolor,width=80,
cursor='hand2',command=lambda :click(7))
b7.grid(row=1,column=0,pady=5)
b8=customtkinter.CTkButton(win,text='8',font=cfont,bg_color=bgcolor,width=80,
cursor='hand2',command=lambda :click(8))
b8.grid(row=1,column=1)
b9=customtkinter.CTkButton(win,text='9',font=cfont,bg_color=bgcolor,width=80,
cursor='hand2',command=lambda :click(9))
b9.grid(row=1,column=2)
bplus=customtkinter.CTkButton(win,text='+',font=cfont,bg_color=bgcolor,width=80,
cursor='hand2',fg_color='green',hover_color='green3',command=lambda :click('+'))
bplus.grid(row=1,column=3)

b4=customtkinter.CTkButton(win,text='4',font=cfont,bg_color=bgcolor,width=80,
cursor='hand2',command=lambda :click(4))
b4.grid(row=2,column=0,pady=15)
b5=customtkinter.CTkButton(win,text='5',font=cfont,bg_color=bgcolor,width=80,
cursor='hand2',command=lambda :click(5))
b5.grid(row=2,column=1)
b6=customtkinter.CTkButton(win,text='6',font=cfont,bg_color=bgcolor,width=80,
cursor='hand2',command=lambda :click(6))
b6.grid(row=2,column=2)
bmul=customtkinter.CTkButton(win,text='*',font=cfont,bg_color=bgcolor,width=80,
cursor='hand2',fg_color='green',hover_color='green3',command=lambda :click('*'))
bmul.grid(row=2,column=3)

b1=customtkinter.CTkButton(win,text='1',font=cfont,bg_color=bgcolor,width=80,
cursor='hand2',command=lambda :click(1))
b1.grid(row=3,column=0)
b2=customtkinter.CTkButton(win,text='2',font=cfont,bg_color=bgcolor,width=80,
cursor='hand2',command=lambda :click(2))
b2.grid(row=3,column=1)
b3=customtkinter.CTkButton(win,text='3',font=cfont,bg_color=bgcolor,width=80,
cursor='hand2',command=lambda :click(3))
b3.grid(row=3,column=2)
bsub=customtkinter.CTkButton(win,text='-',font=cfont,bg_color=bgcolor,width=80,
cursor='hand2',fg_color='green',hover_color='green3',command=lambda :click('-'))
bsub.grid(row=3,column=3)

b0=customtkinter.CTkButton(win,text='0',font=cfont,bg_color=bgcolor,width=80,
cursor='hand2',command=lambda :click(0))
b0.grid(row=4,column=0,pady=15)
bdot=customtkinter.CTkButton(win,text='.',font=cfont,bg_color=bgcolor,width=80,
cursor='hand2',command=lambda :click('.'))
bdot.grid(row=4,column=1)
bclear=customtkinter.CTkButton(win,text='clear',font=cfont,fg_color="red",width=80,
cursor='hand2',hover_color='red3',command=clear)
bclear.grid(row=4,column=2)
bdiv=customtkinter.CTkButton(win,text='/',font=cfont,bg_color=bgcolor,width=80,
cursor='hand2',fg_color='green',hover_color='green3',command=lambda :click('/'))
bdiv.grid(row=4,column=3)

bequal=customtkinter.CTkButton(win,text='=',font=cfont,bg_color=bgcolor,width=380,
cursor='hand2',fg_color='green',hover_color='green3',command=answer)
bequal.grid(row=5,column=0,columnspan=4,pady=10)










win.mainloop()
