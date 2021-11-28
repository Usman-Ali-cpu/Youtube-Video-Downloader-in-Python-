from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

filename = ""
def openLocation():
    global filename
    filename = filedialog.askdirectory()
    

def videoDownload():
    choice = videochoices.get()
    url = entry.get()
    if (len(url) > 1):
        # ytError.config(text="Error")
        yt = YouTube(url)

        if (choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()
        if (choice == choices[1]):
            select = yt.streams.filter(progressive=True, file_extension="mp4").last()
        if (choice == choice[3]):
            select = yt.streams.filter(only_audio=True).first()

    select.Download(filename)


root = Tk()
root.title("Youtube video downloader")
root.geometry('300x300')

root.columnconfigure(0, weight=1)
formLabel = Label(root, text="Enter url of video: ")
formLabel.grid()

entryVar = StringVar()
entry = Entry(root, width=50, textvariable=entryVar)
entry.grid()

errorLabel = Label(root, text="Wrong Url ", fg='red')
errorLabel.grid()

errorLabel = Label(root, text="Save the video file ", fg='blue')
errorLabel.grid()

saveButton = Button(root, text="Choose Path", bg='red', fg='white', width=10, command=openLocation)
saveButton.grid()

pathErrorLabel = Label(root, text="Error in Path ", fg='red')
pathErrorLabel.grid()

selectQualityLabel = Label(root, text="Select quality of video ", fg='blue' ,padx=20, pady=20)
errorLabel.grid()

choices = ["720p", "360p","144p", "Audio"]
videochoices = ttk.Combobox(root, values=choices)
videochoices.grid()

downloadButton = Button(root, text="Download", bg='blue', fg='white', width=10, command = videoDownload)
downloadButton.grid()

developLabel = Label(root, text="Developed by osman ", fg='blue', font=('arial', 20))
developLabel.grid()
root.mainloop()