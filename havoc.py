import cv2
import numpy as npy
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import datetime

import os

root = Tk()
root.geometry('800x600')

#root.configure(background='black')

frpickimg = Frame(root)
frpickimg.pack()

title = Label(frpickimg,text="NOT SO GREAT INTERFACE,  HA PATA HAI!")
title.config(font=("Roboto",20))
title.grid(row=0)


text = StringVar()
text.set('Default Image')

root.fileName = "D:\dmz\sow.jpg"
errfl = "D:\dmz\ "

img = Image.open(root.fileName)
img = img.resize((100, 100), Image.ANTIALIAS)
fimg = ImageTk.PhotoImage(img)
panel = Label(frpickimg, image=fimg)
panel.grid(row=1, column=0)
files = []

def chooser():
    root.fileName = filedialog.askopenfilename(filetypes=(("Image Files(jpg)", "*.jpg"), ("All files", "*.*")))
    img2 = Image.open(root.fileName)
    img2 = img2.resize((100, 100), Image.ANTIALIAS)
    fimg2 = ImageTk.PhotoImage(img2)
    panel.configure(image=fimg2)
    panel.image = fimg2
    files.append(root.fileName)



def picker():
    root.fileName = filedialog.askopenfilename(filetypes=(("Image Files(jpg)", "*.jpg"), ("All files", "*.*")))
    imglist.insert(1,os.path.basename(root.fileName))
    files.append(root.fileName)
    btncmp.grid(row=4, column=1)
    logcte.grid(row=4, column=0)



def cmp():
    if var.get()==1:
        undefect = cv2.imread("D:\dmz\sow.jpg")
        arrlen = len(files)
        file = open("logs.txt", "w")
        for i in range(arrlen):
            defect = cv2.imread(files[i])
            diff = cv2.subtract(undefect, defect)
            fnaming = errfl + "d" +os.path.basename(files[i])
            print("-------------")
            print(fnaming)
            file.write( datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "  ")
            file.write(fnaming + "--> ")
            cv2.imwrite(fnaming, diff)
            i = i + 1
            status = npy.any(diff)
            if status == 1:
                print("Error is detected")
                file.write("Error is detected")
            else:
                print("No error is detected")
                file.write("No error is detected")
            file.write("\n")
        file.close()

    elif var.get()==0:
        undefect = cv2.imread("D:\dmz\sow.jpg")
        arrlen = len(files)
        for i in range(arrlen):
            defect = cv2.imread(files[i])
            diff = cv2.subtract(undefect, defect)
            fnaming = errfl + "d" + os.path.basename(files[i])
            print("-------------")
            print(fnaming)
            i = i + 1
            status = npy.any(diff)
            if status == 1:
                print("Error is detected")
            else:
                print("No error is detected")



def createlog():
    file = open("logs.txt","w")


title = Label(frpickimg,textvariable=text)
title.grid(row=2,column=0)

btnpimg = Button(frpickimg, text="Pick image", command=chooser)
btnpimg.grid(row=3,column=0)

btnpkr = Button(frpickimg, text="Pick to compare", command=picker)

btncmp= Button(frpickimg, text="Compare", command=cmp)

var = IntVar()

logcte = Checkbutton(frpickimg,text="Create Log & images",variable=var)

print(var.get())

imglist = Listbox(frpickimg)

imglist.grid(row=2, column=1)
btnpkr.grid(row=3, column=1)

root.mainloop()
