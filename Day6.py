import threading
import customtkinter
from datetime import datetime
import winsound
import time as t
from customtkinter import CTkButton
from tkinter import messagebox,END
from plyer import notification
#Logic
def set_alarm():
    hour=entryfield1.get()
    min=entryfield2.get()
    sec=entryfield3.get()
    timex=f"{hour}:{min}:{sec}"
    #messagebox.showinfo("done",f"Alarm for {time} is set.")#Its irritating for me
    print("done", f"Alarm for {timex} is set.")
    entryfield1.delete(0,END)
    entryfield2.delete(0, END)
    entryfield3.delete(0, END)
    def play_alarm():
        while True:
            now=datetime.now().strftime("%H:%M:%S")
            if(timex==now):
                notification.notify(
                    title='Heyyyy wake-----uppp',
                    message='uth',
                    timeout=8
                )
                messagebox.showerror('Error', 'Uth muji uthh!!!!!!!!!!')
                winsound.Beep(2000, 10000) #Use pygame instead
                break
            else:
                print(now)
                t.sleep(10)

    alarm_thread = threading.Thread(target=play_alarm, daemon=True)
    alarm_thread.start()

#Gui
win=customtkinter.CTk()
win.title("Alarm clock")
#win.iconbitmap("icon_path.ico")
win.geometry("250x200")

hourtext=customtkinter.CTkLabel(win,text="Hour:",font=("Arial", 18))
hourtext.grid(row=0,column=0,padx=5,pady=5)
entryfield1=customtkinter.CTkEntry(win,text_color="Black",fg_color="white",
border_color='blue')
entryfield1.grid(row=0,column=1)

mintext=customtkinter.CTkLabel(win,text="Min:",font=("Arial", 18))
mintext.grid(row=1,column=0,padx=5,pady=5)
entryfield2=customtkinter.CTkEntry(win,text_color="Black",fg_color="white",
border_color='blue')
entryfield2.grid(row=1,column=1)

sectext=customtkinter.CTkLabel(win,text="Sec:",font=("Arial", 18))
sectext.grid(row=2,column=0,padx=5,pady=5)
entryfield3=customtkinter.CTkEntry(win,text_color="Black",fg_color="white",
border_color='blue')
entryfield3.grid(row=2,column=1)

button=CTkButton(win,text="Set",fg_color="Green",bg_color="Black",hover_color="Green3",cursor="hand2",
                 command=set_alarm)
button.grid(row=3,column=1,padx=10,pady=20)
win.mainloop()