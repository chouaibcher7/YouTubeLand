from tkinter import *
from pygame import *
###Resloution###

win=Tk()
win.geometry("400x400+450+200")
win.configure(background="#ff3030")
win.title("YTL v0.0.1")
win.resizable(0,0)
icon=PhotoImage(file="youtube.png")
win.iconphoto(0, icon)

################
IMPORTANT='''
> ONLY AUDIO FORMAT
'''


lt8=Label(win,text=IMPORTANT,bg='red',fg='white')
lt8.pack()

lb=Label(win,text="YOUTUBE DOWNLOADER",
         font=("arial",15,"bold"),
         background="white",
         fg="red",
         )
lb.place(x=75,y=150)
###
entry=Entry(win,width=40)
entry.place(x=38,y=190)
###functions###
def downloadtube():
    try :
        import youtube_dl
    except :
        print("install youtube_dl")
    ydl_opts = {
        'format': 'bestaudio/best',
        }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([entry.get()])


###############
bt=Button(win,text="DOWNLOAD",command=downloadtube,
           background="white",
           activebackground="red",
           activeforeground="white",
           bd=5,
           relief="raised"
          )
bt.place(x=150,y=220)
###song###################
def play():
    mixer.init()
    mixer.music.load("output.ogg")
    mixer.music.play()
    
play()

def runson():
    mixer.music.unpause()
def stopson():
    mixer.music.pause()


bts=Button(win,text="pause",command=stopson)
bts.place(x=340,y=280)

bts1=Button(win,text="unpause",command=runson)
bts1.place(x=325,y=310)

bts1=Button(win,text="repeat",command=play)
bts1.place(x=340,y=340)

#######################3
lbc=Label(win,text="FOLLOW ME ON INSTAGRAM @chouaibcher7",
          background="white",
          foreground="black",
          font=("arial",10)
          )
lbc.pack(side="bottom")


win.mainloop()

#Devlopped by @chouaibcher7
