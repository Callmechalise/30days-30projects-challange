from tkinter import *
from tkinter import filedialog
import pygame as pg
import os

# Initialize main window
win = Tk()
win.title("Music Player")
win.geometry("500x290")

# Initialize pygame mixer
pg.mixer.init()

# Initialize variables
songs = []
currentsong = ""
paused = False

# Function to load songs from a selected folder
def load():
    global currentsong, songs
    win.directory = filedialog.askdirectory()
    if not win.directory:
        return  # If no folder is selected, do nothing

    songs.clear()
    songlist.delete(0, END)  # Clear previous song list

    for song in os.listdir(win.directory):
        if song.endswith(".mp3"):  # Only add MP3 files
            songs.append(song)

    if songs:
        for song in songs:
            songlist.insert(END, song)  # Add songs to listbox
        songlist.select_set(0)  # Select first song by default
        currentsong = songs[0]  # Set first song as current

# Function to play the selected song
def play():
    global currentsong, paused
    if not songs:  # If no songs are loaded
        return

    if not paused:
        currentsong = songs[songlist.curselection()[0]]  # Get selected song
        pg.mixer.music.load(os.path.join(win.directory, currentsong))
        pg.mixer.music.play()
    else:
        pg.mixer.music.unpause()
        paused = False

# Function to pause the song
def pause():
    global paused
    pg.mixer.music.pause()
    paused = True

# Function to play the next song
def next():
    global currentsong, paused
    if not songs:  # If no songs are loaded
        return

    current_index = songs.index(currentsong)
    if current_index < len(songs) - 1:  # Check if not last song
        songlist.selection_clear(0, END)
        songlist.select_set(current_index + 1)
        currentsong = songs[current_index + 1]
        pg.mixer.music.load(os.path.join(win.directory, currentsong))
        pg.mixer.music.play()

# Function to play the previous song
def previous():
    global currentsong, paused
    if not songs:  # If no songs are loaded
        return

    current_index = songs.index(currentsong)
    if current_index > 0:  # Check if not first song
        songlist.selection_clear(0, END)
        songlist.select_set(current_index - 1)
        currentsong = songs[current_index - 1]
        pg.mixer.music.load(os.path.join(win.directory, currentsong))
        pg.mixer.music.play()

# Create menu
menubar = Menu(win)
win.config(menu=menubar)

organisemenu = Menu(menubar, tearoff=0)
organisemenu.add_command(label="Select folder", command=load)
menubar.add_cascade(label="Organize", menu=organisemenu)

# Song list
songlist = Listbox(win, bg="black", fg="white", width=150, height=15)
songlist.pack()

# Load button images
playbtnimg = PhotoImage(file='play.png')
pausebtnimg = PhotoImage(file='pause.png')
previousbtnimg = PhotoImage(file='previous.png')
nextbtnimg = PhotoImage(file='next.png')

# Button frame
buttonsframe = Frame(win)
buttonsframe.pack()

# Buttons
playbutton = Button(buttonsframe, image=playbtnimg, cursor="hand2", command=play)
pausebutton = Button(buttonsframe, image=pausebtnimg, cursor="hand2", command=pause)
nextbutton = Button(buttonsframe, image=nextbtnimg, cursor="hand2", command=next)
previousbutton = Button(buttonsframe, image=previousbtnimg, cursor="hand2", command=previous)

# Arrange buttons
nextbutton.grid(row=0, column=0, padx=5, pady=5)
playbutton.grid(row=0, column=1, padx=5, pady=5)
pausebutton.grid(row=0, column=2, padx=5, pady=5)
previousbutton.grid(row=0, column=3, padx=5, pady=5)

# Run the application
win.mainloop()
