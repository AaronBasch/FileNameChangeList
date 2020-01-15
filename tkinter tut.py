import tkinter
from tkinter import filedialog
from tkinter import *
import os

window = tkinter.Tk()
window.title('GUI')
window.geometry('350x200')


def clicked():
    root = Tk()
    root.withdraw()
    parentFolder = filedialog.askdirectory()
    text = open("fileNameChanges.txt", "w")
    lst = []
    os.chdir(parentFolder)
    for folder in os.listdir(path='.'):
        lst.append(folder)
    for folderName in lst:
        if folderName != '.DS_Store':
            os.chdir(parentFolder + "/" + folderName)
            for file in os.listdir(path='.'):
                text.write(folderName + "   ---->   " + file + "\n")
    text.close()

label = tkinter.Label(window,
                      text = 'here is your\nfucking gui',
                      font=("Times New Roman",50))

button = tkinter.Button(window, text="choose your\ndamnfolder",command=clicked)

label.pack()
button.pack()


window.mainloop()
