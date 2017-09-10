from Tkinter import *
import pafy
import easygui
from fpdf import FPDF

thridarray = []

def vidgui():
    global window9
    global DirectoryBar1
    global output
    window9 = Tk()
    window9.title("Online Video Extraction")
    window9.geometry('655x600')
    Label1 = Label(window9, text="Url:").place(x=105, y=70)
    DirectoryBar1 = Text(window9)
    DirectoryBar1.config(width=40, height=1, relief=GROOVE, borderwidth=2)
    DirectoryBar1.place(x=190, y=68)
    create = Button(window9, text="Search", command=upload).place(x=500, y=67)
    output = Text(window9)
    output.config(width=60, height=25, relief=GROOVE, borderwidth=2)
    output.place(x=110, y=130)
    Report = Button(window9, text="Report", width=5, command=report).place(x=110, y=520)
    Clear = Button(window9, text="Clear", width=5, command=remove).place(x=210, y=520)
    Exit  = Button(window9, text="Exit", width=5,command=exit).place(x=320, y=520)
    window9.resizable(0,0)
    window9.mainloop()

def upload():
    Address1 = DirectoryBar1.get("1.0", "end-1c")
    Address =  (Address1)
    print Address
    video = pafy.new(Address1)
    path = thridarray[0]+ "/Url Links/"+ "TestedUrls.txt"
    f = open(path, 'w')
    f.write(Address1)
    f.write('\n')
    f.close()
    output.insert(END, Address1, '\n')
    output.insert(END,"\nTitle: " + video.title, '\n')
    output.insert(END, "\nDuration: " + video.duration, '\n')
    output.insert(END, "\nAuthor: " + video.author, '\n')
    output.insert(END, "\nDescription" + video.description, '\n')

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
    pdf.cell(w=195, h=9, txt="[+] Video Document Extraction Report [+]", border=0, ln=1, align='C', fill=0)
    pdf.cell(w=195, h=9, txt="[+] CONFIDENTIAL [+]", border=0, ln=1, align='C', fill=0)
    pdf.cell(w=195, h=9, txt="Forensic Data: ",border=5, ln=1, align='B', fill=0)
    pdf.multi_cell(w=0, h=5, txt=content)
    pdf.output(thridarray[0]+'/Generated Reports/'+imput+'.pdf', 'F')






