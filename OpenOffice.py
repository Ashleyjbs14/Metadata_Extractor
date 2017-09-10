from Tkinter import *
import tkFileDialog
import openxmllib
import os
import shutil
import easygui
from fpdf import FPDF

secondArray = []

def openGui():
    global window6
    global DirectoryBar1
    global output
    window6 = Tk()
    window6.title("Open Office Metadata Extraction")
    window6.geometry('655x600')
    Label1 = Label(window6, text="Directory:").place(x=105, y=70)
    DirectoryBar1 = Text(window6)
    DirectoryBar1.config(width=40, height=1, relief=GROOVE, borderwidth=2)
    DirectoryBar1.place(x=190, y=68)
    create = Button(window6, text="...", command=open).place(x=500, y=67)
    output = Text(window6)
    output.config(width=60, height=25, relief=GROOVE, borderwidth=2)
    output.place(x=110, y=130)
    Extract = Button(window6, text="Extract", width=5, command=officeExt).place(x=110, y=520)
    Report = Button(window6, text="Report", width=5, command=report).place(x=210, y=520)
    Clear  = Button(window6, text="Clear", width=5, command=clear).place(x=360, y=520)
    Exit = Button(window6, text="Exit", width=5,command=window6.withdraw).place(x=465, y=520)
    window6.resizable(0,0)
    window6.mainloop()

def open():
    global office
    global OfficeX
    OfficeX = []
    office = tkFileDialog.askopenfilename(parent=window6, title='Choose JPEG Image',
                                           filetypes=(("Word", "*.docx"),
                                                      ('PowerPoint', '*.pptx'),
                                                      ('Excel', "*.xlsx"),
                                                      ("all files", "*.*")))

    global copyimages
    copyimages = []
    copyimages.insert(0,office)
    DirectoryBar1.insert(END, office)
    OfficeX.insert(0,office)


def officeExt():
    copyfiles()
    try:
        while OfficeX !=0:
            doc = openxmllib.openXmlDocument(OfficeX[0])
            if not doc.coreProperties['created']:
                doc.coreProperties['created']='N/A'
                output.insert(END, '\n\n'+OfficeX[0]+'\n\n')
                output.insert(END,"Created: " + doc.coreProperties['created']+'\n')
            else:
                output.insert(END,'\n\n'+ OfficeX[0]+'\n\n')
                output.insert(END, "Created: "+doc.coreProperties['created']+'\n')

            if not doc.coreProperties['creator']:
                doc.coreProperties['creator'] = 'N/A'
                output.insert(END,"Creator: " + doc.coreProperties['creator']+'\n')
            else:
                output.insert(END,"Creator: " + doc.coreProperties['creator']+'\n')
            if not doc.coreProperties['modified']:
                doc.coreProperties['modified'] = 'N/A'
                output.insert(END,'Date and Time Modified: ' + doc.coreProperties['modified']+'\n')
            else:
                output.insert(END, 'Date and Time Modified: ' + doc.coreProperties['modified']+'\n')
            if not doc.coreProperties['lastModifiedBy']:
                doc.coreProperties['lastModifiedBy'] = 'N/A'
                output.insert(END, "Last modified by: " + doc.coreProperties['lastModifiedBy'] + '\n')
            else:
                output.insert(END, "Last modified by: " + doc.coreProperties['lastModifiedBy'] + '\n')
            if not doc.coreProperties['title']:
                doc.coreProperties['title'] = 'N/A'
                output.insert(END, "Title: " + doc.coreProperties['title'] + '\n')
            else:
                output.insert(END, "Title: " + doc.coreProperties['title'] + '\n')
            if not doc.coreProperties['revision']:
                doc.coreProperties['revision'] = 'N/A'
                output.insert(END, "Revision: " + doc.coreProperties['revision'] + '\n')
            else:
                output.insert(END, "Revision: " + doc.coreProperties['revision'] + '\n\n')

            if not doc.extendedProperties['Company']:
                doc.extendedProperties['Company'] = 'N/A'
                output.insert(END, "Company: " + doc.extendedProperties['Company'] + '\n')
            else:
                output.insert(END, "Company: " + doc.extendedProperties['Company'] + '\n')
            if not doc.extendedProperties['Application']:
                doc.extendedProperties['Application'] = 'N/A'
                output.insert(END, "Application: " + doc.extendedProperties['Application'] + '\n')
            else:
                output.insert(END, "Application: " + doc.extendedProperties['Application'] + '\n')
    except:
        print "done"
        del OfficeX[0]


def copyfiles():
    try:
        while copyimages !=0:
            pies = []
            pies.extend(copyimages)
            base = os.path.basename(pies[0])
            shutil.copyfile(copyimages[0], secondArray[0]+'/Extracted Documents/'+base)
            del copyimages[0]
    except:
        print "Done"


def clear():
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
    pdf.cell(w=195, h=9, txt="[+] Office Document Extraction Report [+]", border=0, ln=1, align='C', fill=0)
    pdf.cell(w=195, h=9, txt="[+] CONFIDENTIAL [+]", border=0, ln=1, align='C', fill=0)
    pdf.cell(w=195, h=9, txt="Forensic Data: ",border=5, ln=1, align='B', fill=0)
    pdf.multi_cell(w=0, h=5, txt=content)
    pdf.output(secondArray[0]+'/Generated Reports/'+imput+'.pdf', 'F')
