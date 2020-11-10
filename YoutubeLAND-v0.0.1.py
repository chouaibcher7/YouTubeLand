from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
###Resloution###
win=Tk()
win.geometry("400x400+450+200")
win.configure(background="white")
win.title(" YOUTUBE DOWNLOADER")
win.resizable(0,0)
################
lb=Label(win,text="YOUTUBE DOWNLOADER",
         font=("arial",15,"bold"),
         background="white",
         fg="red"
         )
lb.pack()
###
entry=Entry(win)
entry.pack(ipadx=100,ipady=5)
###functions###
def downloadtube():
    try :
        import youtube_dl
    except :
        print("install youtube_dl before use")
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
bt.pack(ipadx="70")
###
lbc=Label(win,text="Devlopped by chouaibcher")
lbc.pack(side="bottom",font=(arial,18),)


win.mainloop()

#Devlopped by @chouaibcher7
