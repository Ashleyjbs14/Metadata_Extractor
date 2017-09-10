from Tkinter import *
import tkFileDialog
import os
import datetime
import tkMessageBox
from Exif import *
from PDF import *
import OpenOffice
from testing import *
import OnlineVideo

if __name__=="__main__":

    class MenuGui(object):
        def __init__(self, master):
            global DirectoryBar
            self.master = master
            master.title("Multimedia Metadata Extractor")
            master.geometry("500x250")
            self.Label1 = Label(master, text="Directory:").place(x=50, y=52)
            self.DirectoryBar = Text()
            self.DirectoryBar.config(width=32, height=1, relief=GROOVE, borderwidth=2)
            self.DirectoryBar.place(x=130, y=50)
            self.create = Button(text="...", command=self.create).place(x=380, y=49)
            self.gen = Button(text="Create", command=self.generate).place(x=130, y=205)
            global var
            var = IntVar()
            self.Images = Radiobutton(text="Image Extraction", variable=var, value=1).place(x=130, y=100)
            self.Document = Radiobutton(text="Document Extraction", variable=var, value=2).place(x=130, y=120)
            self.Office = Radiobutton(text="Open Office Docx,Pptx,Xlsb", variable=var, value=3).place(x=130, y=140)
            self.Video = Radiobutton(text="Online Video Metadata Extraction", variable=var, value=4).place(x=130, y=160)
            self.MetaStrip = Radiobutton(text="Strip Metadata", variable=var, value=5).place(x=130, y=180)
            menu = Menu(root)
            root.config(menu=menu)
            filemenu = Menu(menu)
            menu.add_cascade(label="File", menu=filemenu)
            filemenu.add_command(label="New")
            filemenu.add_command(label="Open...",command = self.openproject)
            filemenu.add_separator()
            filemenu.add_command(label="Exit", command=quit)
            root.resizable(0, 0)

        def generate(self):
            radio = var.get()
            if radio == 1:
                save_path = saves
                os.mkdir(save_path, 0755)
                os.mkdir(save_path + "/satellite Images", 0755)
                os.mkdir(save_path + "/Generated Reports", 0755)
                os.mkdir(save_path + "/Extracted Images", 0755)
                completeName = os.path.join(save_path, "Images Readme.txt")
                file1 = open(completeName, "w")
                toFile = "# Python Image MetaData Extraction \n#"
                now = datetime.datetime.now()
                game = str(now)
                file1.write(toFile)
                file1.write(game)
                file1.close()
                tkMessageBox.showinfo("Project Created", "Project Sucessfully Created!!!")
                ImageGui()

            elif radio == 2:
                save_path = saves
                os.mkdir(save_path, 0755)
                os.mkdir(save_path + "/Generated Reports", 0755)
                os.mkdir(save_path + "/Extracted Documents", 0755)
                os.mkdir(save_path + "/Downloaded Documents", 0755)
                completeName1 = os.path.join(save_path, "PDF Document Readme.txt")
                file2 = open(completeName1,"w")
                toFile2 = "# Python PDF MetaData Extraction\n#"
                now2 = datetime.datetime.now()
                game2 = str(now2)
                file2.write(toFile2)
                file2.write(game2)
                file2.close()
                tkMessageBox.showinfo("PDF Project Created","Project Successfully Created!!!")
                DocumentGui()
            elif radio == 3:
                save_path = saves
                os.mkdir(save_path, 0755)
                os.mkdir(save_path + "/Generated Reports", 0755)
                os.mkdir(save_path + "/Extracted Documents", 0755)
                completeName2 = os.path.join(save_path, "Open Office Readme.txt")
                file3 = open(completeName2,'w')
                toFile3 = "# Python Open Office MetaData Extraction \n#"
                now3 = datetime.datetime.now()
                game3 = str(now3)
                file3.write(toFile3)
                file3.write(game3)
                file3.close()
                tkMessageBox.showinfo("Open Office Created", "Project Successfully Created!!!")
                OpenOffice.openGui()
            elif radio == 5:
                root.destroy()
                strip()
            elif radio ==4:
                save_path = saves
                os.mkdir(save_path, 0755)
                os.mkdir(save_path + "/Generated Reports", 0755)
                os.mkdir(save_path + "/Url Links", 0755)
                completeName3 = os.path.join(save_path, "Url Video Readme.txt")
                file4 = open(completeName3, 'w')
                toFile4 = "# Pyhon Online Video Metadata Extraction"
                now4 = datetime.datetime.now()
                game4 = str(now4)
                file4.write(toFile4)
                file4.write(game4)
                file4.close()
                tkMessageBox.showinfo("Online Video Created", "Project Successfully Created!!! ")
                OnlineVideo.vidgui()

        def create(self):
            global saves
            saves = tkFileDialog.asksaveasfilename(parent=root, title='Choose a file',
                                                   filetypes=[("Document Files", "*.PDF;"),
                                                              ("PDF", '*.PDF'),
                                                              ('All', '*')])
            self.DirectoryBar.insert(END, saves)
            pie.append(saves)
            array.append(saves)
            OpenOffice.secondArray.append(saves)
            OnlineVideo.thridarray.append(saves)

        def openproject(self):
            root.withdraw()
            global window4
            global DirectoryBar2
            window4 = Tk()
            window4.title("Load Project")
            window4.geometry('500x150')
            Label1 = Label(window4,text="Directory:").place(x=50, y=52)
            DirectoryBar2 = Text(window4)
            DirectoryBar2.config(width=32, height=1, relief=GROOVE, borderwidth=2)
            DirectoryBar2.place(x=130, y=50)
            create = Button(window4,text="...", command=self.saving).place(x=380, y=49)
            gen = Button(window4,text="Open", command=self.compare).place(x=130, y=100)
            window4.resizable(0,0)
            menu = Menu(window4)
            window4.config(menu=menu)
            filemenu = Menu(menu)
            menu.add_cascade(label="File", menu=filemenu)
            filemenu.add_command(label="New",command=self.bringbk)
            filemenu.add_command(label="Open...")
            filemenu.add_separator()
            filemenu.add_command(label="Exit", command=quit)
            window4.mainloop()

        def saving(self):
            global saving
            saving = tkFileDialog.askdirectory()
            DirectoryBar2.insert(END, saving)
            pie.append(saving)
            array.append(saving)
            OpenOffice.secondArray.append(saving)
            OnlineVideo.thridarray.append(saving)

        def compare(self):
            imagepro = os.path.exists(saving+'/Images Readme.txt')
            imagepro2 = os.path.exists(saving+'/PDF Document Readme.txt')
            imagespro3 = os.path.exists(saving+'/Open Office Readme.txt')
            vidurl = os.path.exists(saving + "/Url Video Readme.txt")

            if imagepro == True:
                window4.destroy()
                root.destroy()
                ImageGui()
            elif imagepro2 == True:
                window4.destroy()
                root.destroy()
                DocumentGui()
            elif imagespro3 == True:
                window4.destroy()
                root.destroy()
                OpenOffice.openGui()
            elif vidurl == True:
                window4.destroy()
                root.destroy()
                OnlineVideo.vidgui()

        def bringbk(self):
            root.deiconify()
            window4.destroy()

    root = Tk()
    my_gui = MenuGui(root)
    root.mainloop()

