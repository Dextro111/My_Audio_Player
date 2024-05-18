from tkinter import filedialog      #   used for acessing files
from tkinter import *   #  Gui Library 
import pygame
import os

root = Tk()     #  This is the window for our player. initializing the app 
root.title("Music Player")     #  sets title
root.geometry("500x300")      #  Sets Size of windoow

pygame.mixer.init()             #   Initialize mixer to allow us play Audio

menubar = Menu(root)            #   Create the menu bar with the Menu Class
root.config(menu=menubar)       #   Adding our menubar to the root window

songs = []                      #  creates a song list
current_song = ""
paused = False

def load_music():
    """Load music into our vid_player"""
    global current_song
    root.directory = filedialog.askdirectory()          #   Brings up a pop-up to choose our folder

    for song in os.listdir(root.directory):             #   Iterating over files in the directory weve chosen and splitting up the
        name, ext = os.path.splitext(song)              #   file name into name and extension. if the extension is mp3 add to list
        if ext == ".mp3":
            songs.append(song)
    
    for song in songs:                                  #   the for loop iterates over each song and insert into songlist(box)
        songlist.insert("end", song)                    

    songlist.selection_set(0)                           #   Selects first song
    current_song = songs[songlist.curselection()[0]]    

def play_music():
    global current_song, paused

    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory, current_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused = False

def pause_music():
    global paused
    pygame.mixer.music.pause()
    paused = True
    
def next_music():
    global current_song, paused
    
    try:
        songlist.select_clear(0, END)
        songlist.selection_set(songs.index(current_song) + 1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass

def prev_music():
    global current_song, paused

    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(current_song) - 1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass

orgarnise_menu = Menu(menubar, tearoff=False)         #   Create orgarnise menu
orgarnise_menu.add_command(label="Select Folder", command=load_music )       #   Setting the command
menubar.add_cascade(label="Orgarnise", menu=orgarnise_menu)     #   Add orgarnise menu to the menu bar

songlist = Listbox(root, bg="black", fg="white", width=100, height=14)            #   Creates the list of songs box
songlist.pack()             #   Adds songlist box to the window

play_btn_image = PhotoImage(file="Images/play.png")     #   Import play btn img
next_btn_image = PhotoImage(file="Images/next.png")     #   Import next btn img
pause_btn_image = PhotoImage(file="Images/pause.png")     #   Import Pause btn img
prev_btn_image = PhotoImage(file="Images/previous.png")     #   Import Previous btn img

ctrl_frame = Frame(root)        #   Create A Frame next (Div). it allows us put widgets
ctrl_frame.pack()       #   Loads the frame to the player

play_btn = Button(ctrl_frame, image= play_btn_image, borderwidth=0, command=play_music)     #   Create the button on the frame and setting borders
next_btn = Button(ctrl_frame, image= next_btn_image, borderwidth=0, command=next_music)     #   Create the button on the frame and setting borders
pause_btn = Button(ctrl_frame, image= pause_btn_image, borderwidth=0, command=pause_music)     #   Create the button on the frame and setting borders
prev_btn = Button(ctrl_frame, image= prev_btn_image, borderwidth=0, command=prev_music)     #   Create the button on the frame and setting borders

play_btn.grid(row=0, column=1, padx=7, pady=10)     #   We'll use grid to have them on the same line but on diff columns
next_btn.grid(row=0, column=3, padx=7, pady=10)     #   We'll use grid to have them on the same line but on diff columns
pause_btn.grid(row=0, column=2, padx=7, pady=10)     #   We'll use grid to have them on the same line but on diff columns
prev_btn.grid(row=0, column=0, padx=7, pady=10)     #   We'll use grid to have them on the same line but on diff columns


root.mainloop()     #   This runs the Player
