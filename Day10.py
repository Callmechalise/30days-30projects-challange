import tkinter,customtkinter
import pygame
from tkinter import Label,Button
from PIL import Image,ImageTk
from random import randint
pygame.mixer.init()
#Window not perfectly sized cause got bored for collecting scratch files
cfont=("Arial", 16, "bold")
tcolor='white'
bgcolor='black'

win=tkinter.Tk()
win.title("RSP")
win.config(bg="light blue")

rockpng=ImageTk.PhotoImage(Image.open("rock.png"))
rocklabel=Label(win,image=rockpng,bg="lightblue",fg="lightblue")


scissorpng=ImageTk.PhotoImage(Image.open("scissors.png"))
scissorlabel=Label(win,image=scissorpng,bg="lightblue",fg="lightblue")


paperpng=ImageTk.PhotoImage(Image.open("papers.png"))
paperlabel=Label(win,image=paperpng,bg="lightblue",fg="lightblue")


comp_rockpng=ImageTk.PhotoImage(Image.open("rock.png"))
comp_rocklabel=Label(win,image=rockpng,bg="lightblue",fg="lightblue")


comp_scissorpng=ImageTk.PhotoImage(Image.open("scissors.png"))
comp_scissorlabel=Label(win,image=scissorpng,bg="lightblue",fg="lightblue")


comp_paperpng=ImageTk.PhotoImage(Image.open("papers.png"))
comp_paperlabel=Label(win,image=paperpng,bg="lightblue",fg="lightblue")

userlabel=Label(win,image=paperpng,bg="light blue")
userlabel.grid(row=1,column=4)
complabel=Label(win,image=comp_paperpng,bg="light blue")
complabel.grid(row=1,column=0)
#score
playerscore=Label(win,text=0,font=100,bg="lightblue",fg="Green")
compscore=Label(win,text=0,font=100,bg="lightblue",fg="red")

compscore.grid(row=1,column=1)
playerscore.grid(row=1,column=3)


#Button
rock=Button(win,width=20,height=2,text="Rock",bg="light green",fg="white",cursor='hand2',
            command=lambda :updatechoice("rock")).grid(row=2,column=1)
paper=Button(win,width=20,height=2,text="paper",bg="red",
fg="white",cursor='hand2',command=lambda :updatechoice("paper")).grid(row=2,column=2)
scissor=Button(win,width=20,height=2,text="scissor",bg="pink",
fg="white",command=lambda :updatechoice("scissor"),cursor='hand2').grid(row=2,column=3)

#player indicator
user_indicator=Label(win,font=cfont,text="User",bg="light blue").grid(row=0,column=3)
user_indicator=Label(win,font=cfont,text="Computer",bg="light blue").grid(row=0,column=1)

#message
msg=Label(win,font=cfont,bg="lightblue",fg="Red")
msg.grid(row=1,column=2)

def checkwin(player,computer):
    if player==computer:
        updatemsg('Drawww')
    elif player=="rock":
        if computer=="paper":
            updatemsg("youlose")
            updatecompscore()
            sound = pygame.mixer.Sound("gameover.wav")
            sound.play()
        else:
            updatemsg("You won!!")
            updateuserscore()
            sound = pygame.mixer.Sound("win.wav")
            sound.play()

    elif player =="paper":
        if computer=="scissor":
            updatemsg("youlose")
            updatecompscore()
            sound = pygame.mixer.Sound("gameover.wav")
            sound.play()
        else:
            updatemsg("You won!!")
            updateuserscore()
            sound = pygame.mixer.Sound("win.wav")
            sound.play()
    elif player=="scissor":
        if computer=="rock":
            updatemsg("youlose")
            updatecompscore()
            sound = pygame.mixer.Sound("gameover.wav")
            sound.play()
        else:
            updatemsg("You won!!")
            updateuserscore()
            sound = pygame.mixer.Sound("win.wav")
            sound.play()
    else:
        pass

choice = ["rock", "paper", "scissor"]
def updatechoice(x):
    #comp choice
    y=randint(0,2)
    choicey=choice[y]
    if choicey=="paper":
        complabel.configure(image=comp_paperpng)
    elif choicey=="rock":
        complabel.configure(image=comp_rockpng)
    else:
        complabel.configure(image=comp_scissorpng)

    if x=="rock":
        userlabel.configure(image=rockpng)
    elif x=="paper":
        userlabel.configure(image=paperpng)
    else:
        userlabel.configure(image=scissorpng)
    checkwin(x,choicey)
def updatemsg(x):
    msg['text']=x

def updateuserscore():
    score=int(playerscore['text'])
    score+=1
    playerscore["text"]=score
def updatecompscore():
    score=int(compscore['text'])
    score+=1
    compscore["text"]=score

win.mainloop()