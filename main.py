import tkinter
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        ytLink = link.get()
        ytobject = YouTube(ytLink)
        video = ytobject.streams.get_highest_resolution()
        video.download()
        print("Success!")
    except:
        print("Invalid link.")
        

# system settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

# frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Simple YouTube Downloader")

# elements
title = customtkinter.CTkLabel(app, text="YouTube Link:")
title.pack(padx=20, pady=20)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

downloadBtn = customtkinter.CTkButton(app, text="Download", command=startDownload)

app.mainloop()