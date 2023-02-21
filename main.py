# Name: Jenil Patel
# Email: jenilp110@gmail.com


from tkinter import *
from pytube import YouTube
from tkinter import filedialog
import shutil

def video_path():
    path= filedialog.askdirectory()
    path_label.config(text=path)

def download_video():
    get_link = link_field.get()
    user_path = path_label.cget("text")
    screen.title('Downloading...')
    video = YouTube(get_link).streams.get_lowest_resolution().download()

    shutil.move(video, user_path)

    screen.title('Download Completed !!')


screen = Tk()
title = screen.title("YouTube Video Downloder")
canvas = Canvas(screen, width=400, height=600)
canvas.pack()

img_icon = PhotoImage(file='images/IconYouTube.png')
img_icon = img_icon.subsample(2,2)
canvas.create_image(200, 70, image=img_icon)

link_field = Entry(screen, width=40, font=('Arial', 16) )
link_label = Label(screen, text="Enter Youtube Link Below: ", font=('Arial', 16))

path_label = Label(screen, text="Choose Path For Download", font=('Arial', 16))
btn_select = Button(screen, text="Select Path", bg='crimson', padx='20',pady='5', font=('Arial', 16), command=video_path)

canvas.create_window(220, 280, window=path_label)
canvas.create_window(220, 320, window=btn_select)

canvas.create_window(200, 220, window=link_field)
canvas.create_window(200, 160, window=link_label)

btn_download = Button(screen, text="Download Video", bg="green", padx='22', pady='5', font=('Arial', 16), command=download_video)
canvas.create_window(220, 380, window=btn_download)

screen.mainloop()
