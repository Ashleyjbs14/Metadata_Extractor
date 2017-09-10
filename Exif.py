from Tkinter import *
import tkFileDialog
from reportlab.pdfgen import canvas
import urllib2
import os
from PIL import Image, ImageTk
from PIL.ExifTags import TAGS, GPSTAGS
import PIL
from fpdf import FPDF
import urllib
import datetime
import tkMessageBox
import gpsimage
import test3
import shutil
from fpdf import FPDF
import easygui
from geopy.geocoders import Nominatim

pie = []


def ImageGui():
    global window
    global DirectoryBar
    global output
    global output2
    global output3
    window = Tk()
    window.title("Image File Extraction")
    Label1 = Label(window,text="Directory:").place(x=105, y=70)
    Label(window,text="All data").place(x=300, y=100)
    Label(window,text="Forensic Data").place(x=715, y=100)
    Label(window,text="GPS").place(x=740, y=325)
    DirectoryBar = Text(window)
    DirectoryBar.config(width=40, height=1, relief=GROOVE, borderwidth=2)
    DirectoryBar.place(x=190, y=68)
    create = Button(window, text="...",command=upload).place(x=500, y=67)
    window.attributes("-fullscreen", True)
    output = Text(window)
    output.config(width=60, height=25, relief=GROOVE, borderwidth=2)
    output.place(x=110, y=130)
    output2 = Text(window)
    output2.config(width=60, height=12, relief=GROOVE, borderwidth=2)
    output2.place(x=550, y=130)
    output3 = Text(window)
    output3.config(width=60, height=10, relief=GROOVE, borderwidth=2)
    output3.place(x=550, y=355)
    gen = Button(window, text="Extract", command=extract).place(x=110, y=530)
    save = Button(window,text="Report",command=report).place(x=200, y=530)
    gps = Button(window, text="GPS", command=maps).place(x=290, y=530)
    clear = Button(window,text="Clear", command=remove).place(x=360, y=530)
    Exit = Button(window, text="Exit", command=window.withdraw).place(x=440, y=530)
    window.resizable(0, 0)
    window.mainloop()




def upload():
    window.files = tkFileDialog.askopenfilenames(parent=window, title='Choose JPEG Image',
                                                 filetypes=[("Image Files", "*.JPEG;"),
                                                            ("Image", '*.JPG'),
                                                            ("Image", '*.JPEG'),
                                                            ('All', '*')])
    DirectoryBar.insert(END, window.files)
    images = list(window.files)
    images1 = list(window.files)
    images2 = list(window.files)
    images3 = list(window.files)
    global  arrayFiles
    arrayFiles = []
    arrayFiles.extend(images1)
    global fileArray
    fileArray = []
    fileArray.extend(images)
    global gpsArray
    gpsArray = []
    gpsArray.extend(images2)
    global copyimages
    copyimages= []
    copyimages.extend(images3)
    global count
    count = str(len(fileArray)) + " Files Extracted Sucessfully!!!"

def extract():
    refine()
    gps()
    copyfiles()
    try:
        while fileArray != 0:
            metaData = {}
            imgFile = Image.open(fileArray[0])
            output.insert(END, '\n\n[*] Image MetaData For:' + str(fileArray[0]))
            info = imgFile._getexif()
            if info:
                output.insert(END, '\n[+] Found MetaData [+]\n')
                for (tag, value) in info.items():
                    tagname = TAGS.get(tag, tag)
                    metaData[tagname] = value
                    output.insert(END, str(tagname) + '\t' + str(value) + '\n')
                del fileArray[0]
    except:
        tkMessageBox.showinfo("Extraction Status", count)
        output.insert(END, "\n[*] End of Extraction [*]")



def gps():
    try:
        while gpsArray != 0:
            img = gpsimage.open(gpsArray[0])
            float = img.lat
            if img.lat and img.lng !=None:
                output3.insert(END,gpsArray[0]+'\n')
                output3.insert(END,img.lat)
                output3.insert(END, ", ")
                output3.insert(END,img.lng)
                output3.insert(END, '\n\n')
                del gpsArray[0]
            else:
                print gpsArray[0], "-- nothing here"
                del gpsArray[0]
    except:
        print "End of extraction"


def refine():
    try:
        while arrayFiles != 0:
            img = PIL.Image.open(arrayFiles[0])
            exif_data = img._getexif()
            if 36868 not in exif_data:
                exif_data[36868] = "N/A"
                output2.insert(END,arrayFiles[0] + '\n')
                output2.insert(END,"\nDate and Time: " + exif_data[36868])
            else:
                output2.insert(END,arrayFiles[0])
                print output2.insert(END,"\nDate and Time: " + exif_data[36868])

            if 271 not in exif_data:
                exif_data[271] = "N/A"
                output2.insert(END,"\nMake:" + exif_data[271])
            else:
                output2.insert(END,"\nMake:" + exif_data[271])

            if 272 not in exif_data:
                exif_data[272] = "N/A"
                output2.insert(END, "\nModel:" + exif_data[272])
            else:
                output2.insert(END, "\nModel:" + exif_data[272])

            if 305 not in exif_data:
                exif_data[305] = "N/A"
                output2.insert(END,"\nSoftware:" + exif_data[305])
            else:
                output2.insert(END,"\nSoftware:" + exif_data[305])

            if 33432 not in exif_data:
                exif_data[33432] = 'N/A'
                output2.insert(END,"\nCopyright: " + exif_data[33432])
            else:
                output2.insert(END,"\nCopyright: " + exif_data[33432])

            if 315 not in exif_data:
                exif_data[315] = "N/A"
                output2.insert(END, "\nArtist: " + exif_data[315] + '\n\n')
            else:
                output2.insert(END,"\nArtist: " + exif_data[315] +'\n\n')

            del arrayFiles[0]
    except:
        print '[+] End of Extraction [+]'

def remove():
    output.delete(1.0, END)
    output2.delete(1.0, END)
    output3.delete(1.0, END)



def maps():
    global window2
    global gpsbox
    global  geolocation
    window2 = Tk()
    window2.geometry('500x500')
    window2.title("Maps")
    gpslabel = Label(window2, text="GPS Coordinates").place(x=190, y=70)
    gpsbox = Entry(window2)
    gpsbox.place(x=150,y=100)
    find = Button(window2, text="Search", command=google).place(x=350, y=100)
    geolocation = Text(window2)
    geolocation.config(width=50, height=10, relief=GROOVE, borderwidth=2)
    geolocation.place(x=65, y=150)
    window2.resizable(0, 0)
    window2.mainloop()


def copyfiles():
    try:
        while copyimages !=0:
            pies = []
            pies.extend(copyimages)
            base = os.path.basename(pies[0])
            shutil.copyfile(copyimages[0], pie[0]+'/Extracted Images/'+base)
            del copyimages[0]
    except:
        print "Done"



def google():
    ham = gpsbox.get()
    marker_list =[]
    marker_list.append("markers=size:big|label:B|color:red|51.44346130003542, 0.08092060000362103|")
    test3.get_static_google_map(pie[0]+"/satellite Images/"+ham, center=ham, imgsize=(640, 640),
                          zoom=18, imgformat="png", markers=marker_list)
    image = Image.open(pie[0]+'/satellite Images/'+ham+'.png')
    photo = ImageTk.PhotoImage(image)
    image.show()
    geolocator = Nominatim()
    location = geolocator.reverse(ham)
    geolocation.insert(END,location)



def report():

    imput = easygui.enterbox(msg = "Save PDF Report as?",
                             title="Forensic report ",
                             strip = True,
                             default="...")
    content = output2.get("1.0", "end-1c")
    content2 = output3.get("1.0", "end-1c")
    content3 = output.get("1.0", "end-1c")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(w=195, h=9, txt="[+] Image Document Extraction Report [+]", border=0, ln=1, align='C', fill=0)
    pdf.cell(w=195, h=9, txt="[+] CONFIDENTIAL [+]", border=0, ln=1, align='C', fill=0)
    pdf.cell(w=195, h=9, txt="Forensic Data: ",border=5, ln=1, align='B', fill=0)
    pdf.multi_cell(w=0, h=5, txt=content)
    pdf.cell(w=195, h=9, txt="Gps Data:", border=5, ln=1, align='B', fill=0)
    pdf.multi_cell(w=0, h=5, txt=content2)
    pdf.cell(w=195, h=9, txt="All Data:", border=5, ln=1, align='B', fill=0)
    pdf.multi_cell(w=0, h=5, txt=content3)
    pdf.output(pie[0]+'/Generated Reports/'+imput+'.pdf', 'F')








