from tkinter import *
import pytube
import os
import subprocess

def download():
    video_url = url.get()
    i = rdiobtn.get()
    youtube = pytube.YouTube(video_url)
    title = youtube.streams[0].title
    if (i == 1):
        try:
            youtube.streams.filter(only_video=True, res="1080p", subtype='mp4').order_by('fps').first().download("D:\Downloads", filename='Video')
            youtube.streams.filter(only_audio=True, subtype='webm').order_by('abr').first().download("D:\Downloads",filename='Audio')
            os.chdir('D:\Downloads')
            subprocess.call('ffmpeg -i Video.mp4 -i Audio.webm -r 59.94 -c:v copy output.mp4', shell=True)
            if '\\' in title or '/' in title or ':' in title or '*' in title or '|' in title or '?' in title or '"' in title or '>' in title or '<' in title:
                subprocess.call('del Audio.webm Video.mp4',shell=True)
                os.rename("output.mp4","new_video.mp4")
            else:
                os.rename("output.mp4","%s.mp4" % title)
                subprocess.call('del Audio.webm Video.mp4',shell=True)
            notif.config(fg="green", text="Download complete!")
        except Exception as e:
            print(e)
            notif.config(fg="red", text="Video could not be downloaded")
    elif (i == 2):
        try:
            youtube.streams.filter(only_video=True, res="720p", subtype='mp4').order_by('fps').first().download("D:\Downloads", filename='Video')
            youtube.streams.filter(only_audio=True, subtype='webm').order_by('abr').first().download("D:\Downloads",filename='Audio')
            os.chdir('D:\Downloads')
            subprocess.call('ffmpeg -i Video.mp4 -i Audio.webm -r 60 -c:v copy output.mp4', shell=True)
            if '\\' in title or '/' in title or ':' in title or '*' in title or '|' in title or '?' in title or '"' in title or '>' in title or '<' in title:
                subprocess.call('del Audio.webm Video.mp4',shell=True)
                os.rename("output.mp4","new_video.mp4")
            else:
                os.rename("output.mp4","%s.mp4" % title)
                subprocess.call('del Audio.webm Video.mp4',shell=True)
            notif.config(fg="green", text="Download complete!")
        except Exception as e:
            print(e)
            notif.config(fg="red", text="Video could not be downloaded")
    elif(i == 3):
        try:
            youtube.streams.filter(only_video=True, res="480p", subtype='mp4').order_by('fps').first().download("D:\Downloads", filename='Video')
            youtube.streams.filter(only_audio=True, subtype='webm').order_by('abr').first().download("D:\Downloads",filename='Audio')
            os.chdir('D:\Downloads')
            subprocess.call('ffmpeg -i Video.mp4 -i Audio.webm -r 30 -c:v copy output.mp4', shell=True)
            if '\\' in title or '/' in title or ':' in title or '*' in title or '|' in title or '?' in title or '"' in title or '>' in title or '<' in title:
                subprocess.call('del Audio.webm Video.mp4',shell=True)
                os.rename("output.mp4","new_video.mp4")
            else:
                os.rename("output.mp4","%s.mp4" % title)
                subprocess.call('del Audio.webm Video.mp4',shell=True)
            notif.config(fg="green", text="Download complete!")
        except Exception as e:
            print(e)
            notif.config(fg="red", text="Video could not be downloaded")
    else:
        notif.config(fg="red", text="Choose Resolution")


master = Tk()
rdiobtn = IntVar()
master.title("Youtube Video Downloader")
master.configure(bg='#282828')
Label(master, text="Youtube Video Converter",bg='#282828', fg='#FAFAFA', font=("Calibri",15)).grid(sticky=N,padx=150,row=0)
Label(master, text="Please enter the link of the video below :",bg='#282828',fg='#b3b3b3', font=("Calibri",12)).grid(sticky=N,row=1,pady=15)
Radiobutton(master, value=1, variable=rdiobtn, text="1080p",bg='#282828',font=("Calibri",12)).grid(sticky=N,row=3,pady=10)
Radiobutton(master, value=2, variable=rdiobtn, text="720p",bg='#282828',font=("Calibri",12)).grid(sticky=N,row=4,pady=10)
Radiobutton(master, value=3, variable=rdiobtn, text="480p",bg='#282828',font=("Calibri",12)).grid(sticky=N,row=5,pady=10)
notif = Label(master,bg='#282828', font=("Calibri",12))
notif.grid(sticky=N, pady=1, row=7)
url = StringVar()
Entry(master, width=70,bg='#282828', textvariable=url,fg='#FAFAFA').grid(sticky=N, row=2)
Button(master, width=17, text="Download",bg='#282828',fg='#FAFAFA', font=("Calibri",15), command=download).grid(sticky=N, row=6,pady=15)

master.mainloop()