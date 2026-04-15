import pygame, tkinter
from tkinter import filedialog
from Constantes import *

window = tkinter.Tk()
pygame.init()

#Variables
Music_Queue = []

paused = True
playing = False

def PlayMusic():
    pass

def StopMusic():
    pass

def CheckIfIsSongEnd(song:string) -> boolean:
    return True

def GettingSong() -> string:
    filepath = filedialog.askopenfilename(
    title="Choice you file",
    multiple=True,
    initialdir="/",
    filetypes=
    (("music files", ".mp3"),
    ("music files",".wav")))

    return filepath

def AddSongToQueue():
    filepath = GettingSong()
    
    for path in filepath:
        Music_Queue.append(path)
    
    print(Music_Queue)

def NextSong():
    pass

def PreviousSong():
    pass

window.geometry("500x500+100+100")

MusicControlFrame = tkinter.Frame(window)
MusicControlFrame.pack()

RewindButton = tkinter.Button(MusicControlFrame, text="Undo")
RewindButton.grid(row=0, column=0)

if paused:
    play = tkinter.Button(MusicControlFrame, text="Play")
    play.grid(row=0, column=1)
else:
    pause = tkinter.Button(MusicControlFrame, text="Pause")
    pause.grid(row=0, column=1)

NextButton = tkinter.Button(MusicControlFrame, text="Next")
NextButton.grid(row=0, column=2)

GetSongsButton = tkinter.Button(window, text="+", command=AddSongToQueue)
GetSongsButton.pack()

window.mainloop()