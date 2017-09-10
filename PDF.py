from Tkinter import *
import tkFileDialog
import pyPdf
from pyPdf import PdfFileReader
import os
import shutil
import tkMessageBox
import urllib2
import easygui
from fpdf import FPDF



array = []

def DocumentGui():
    global window5
    global DirectoryBar
    global output
    global UrlBar
    window5 = Tk()
    window5.title("PDF File Extraction")
    window5.geometry('685x610')
    Label1 = Label(window5, text="Directory:").place(x=110, y=70)
    Label2 = Label(window5, text="All data").place(x=320, y=100)
    Label3 =Label(window5, text="Forensic Data").place(x=715, y=100)
    Label4 = Label(window5, text="Url:").place(x=150,y=40)
    DirectoryBar = Text(window5)
    DirectoryBar.config(width=40, height=1, relief=GROOVE, borderwidth=2)
    DirectoryBar.place(x=190, y=68)
    UrlBar = Text(window5)
    UrlBar.config(width=40, height=1, relief=GROOVE, borderwidth=2)
    UrlBar.place(x=190, y=40)
    create = Button(window5, text="...",command=uploadpdf).place(x=500, y=67)
    output = Text(window5)
    output.config(width=60, height=25, relief=GROOVE, borderwidth=2)
    output.place(x=125, y=130)
    gen = Button(window5, text="Extract", width=5,command=extractedpdf).place(x=125, y=530)
    save = Button(window5, text="Report", width=5,command=report).place(x=230, y=530)
    clear = Button(window5, text="Clear", width=5, command=remove).place(x=375, y=530)
    Exit = Button(window5, text="Exit", width=5, command=window5.withdraw).place(x=480, y=530)
    Search = Button(window5, text="Get", command=Address).place(x=500, y=40)
    window5.resizable(0, 0)
    window5.mainloop()


def uploadpdf():
    pdf = tkFileDialog.askopenfilenames(parent=window5, title='Choose a file',
                                               filetypes=[("Document Files", "*.PDF;"),
                                                          ("PDF", '*.PDF'),
                                                          ('All', '.')])
    DirectoryBar.insert(END, pdf)
    print pdf
    pies = list(pdf)
    global pdfarray
    pdfarray =[]
    pdfarray.extend(pies)
    global pdfarray2
    pdfarray2 = []
    pdfarray2.extend(pies)
    global count
    count = str(len(pdfarray2)) + " Files Extracted Sucessfully!!!"

def Address():
    global filez
    Address1 = UrlBar.get("1.0", "end-1c")
    Address = (Address1)
    Add = (Address1)
    filename = Address1
    response = urllib2.urlopen(Address)
    filez = array[0] + "/Downloaded Documents/" + filename.rsplit('/',1)[1]
    file = open(filez,'w')
    file.write(response.read())
    file.close()
    urlExtraction()

def urlExtraction():
    try:
        while filez !=0:
            pdfFile = PdfFileReader(file(filez))
            docinfo = pdfFile.getDocumentInfo()
            output.insert(END, '\n\n[*] Document MetaData For:' + str(filez))
            for metaItem in docinfo:
                output.insert(END, '\n[+]' + metaItem, ':', docinfo[metaItem])
            del pdfarray[0]
            if pdfarray == 0:
                print("Done")
    except:
        output.insert(END, '\n[*] End of Extraction [*]')


def extractedpdf():
    copypdf()
    try:
        while pdfarray != 0:
            pdfFile = PdfFileReader(file(pdfarray[0]))
            docinfo = pdfFile.getDocumentInfo()
            output.insert(END, '\n\n[*] Document MetaData For:' + str(pdfarray[0]))
            for metaItem in docinfo:
                output.insert(END, '\n[+]' + metaItem, ':', docinfo[metaItem])
            del pdfarray[0]
            if pdfarray == 0:
                print("Done")
    except:
        output.insert(END, '\n[*] End of Extraction [*]')


def copypdf():
    try:
        while pdfarray2 !=0:
            piez = []
            piez.extend(pdfarray2)
            base = os.path.basename(piez[0])
            shutil.copyfile(pdfarray2[0], array[0]+'/Extracted Documents/'+base)
            del pdfarray2[0]
    except:
        print "Done"


def remove():
    output.delete(1.0, END)


def report():

    imput = easygui.enterbox(msg = "Save PDF Report as?",
                             title="Forensic report ",
                             strip = True,
                             default="...")
    content = output.get("1.0", "end-1c")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(w=195, h=9, txt="[+] PDF Document Extraction Report [+]", border=0, ln=1, align='C', fill=0)
    pdf.cell(w=195, h=9, txt="[+] CONFIDENTIAL [+]", border=0, ln=1, align='C', fill=0)
    pdf.cell(w=195, h=9, txt="Forensic Data: ",border=5, ln=1, align='B', fill=0)
    pdf.multi_cell(w=0, h=5, txt=content)
    pdf.output(array[0]+'/Generated Reports/'+imput+'.pdf', 'F')
