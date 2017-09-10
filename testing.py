import piexif
from Tkinter import *
import tkFileDialog
import tkMessageBox
from Exif import *

def strip():
    global window8
    global DirectoryBar
    window8 = Tk()
    window8.title("JPEG Metadata Stripping")
    window8.geometry('668x195')
    window8.resizable(0,0)
    Label1 = Label(text="Directory:").place(x=105, y=70)
    DirectoryBar = Text()
    DirectoryBar.config(width=40, height=1, relief=GROOVE, borderwidth=2)
    DirectoryBar.place(x=190, y=68)
    create = Button(text="...",command=upload).place(x=500, y=67)
    Button1 = Button(text="Strip", command=extract).place(x=190, y=100)
    window8.mainloop()

def upload():
    global files
    files = tkFileDialog.askopenfilenames(parent=window8, title='Choose JPEG Image',
                                                 filetypes=[("Image Files", "*.JPEG;"),
                                                            ("Image", '*.JPG'),
                                                            ("Image", '*.JPEG'),
                                                            ('All', '*')])

    global cheese
    cheese =[]
    cheese.extend(files)
    DirectoryBar.insert(END, files)

def extract():
    try:
        while cheese !=0:
            filename = cheese[0]
            data = piexif.load(filename)
            piexif.remove(filename)
            empty = piexif.load(filename)
            print empty
            del cheese[0]
    except:
        tkMessageBox.showinfo("Extraction Status", "Metadata Removed!!!")
        window8.destroy()
        ImageGui()






