from tkinter import *
###Resloution###
win=Tk()
win.geometry("400x400+450+200")
win.configure(background="white")
win.title("YTL v0.0.1")
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
lbc=Label(win,text="FOLLOW ME ON INSTAGRAM @chouaibcher7",
          background="white",
          foreground="black",
          font=("arial",10)
          )
lbc.pack(side="bottom")


win.mainloop()

#Devlopped by @chouaibcher7

#YouTubeLand-v0.0.1
