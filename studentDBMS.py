from tkinter import *
import tkinter.messagebox
import stdDataBase_BackEnd


class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Database Management System")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="cadet blue")

        stdId = StringVar()
        firstName = StringVar()
        surname = StringVar()
        dob = StringVar()
        age = StringVar()
        gender = StringVar()
        address = StringVar()
        mobile = StringVar()

        # ==========================FUNCTION========================== #

        def iExit():
            iExit = tkinter.messagebox.askyesno("Students Database Management Systems",
                                                "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def clearData():
            self.txtstdID.delete(0, END)
            self.txtfname.delete(0, END)
            self.txtsname.delete(0, END)
            self.txtdob.delete(0, END)
            self.txtage.delete(0, END)
            self.txtgender.delete(0, END)
            self.txtaddress.delete(0, END)
            self.txtmobile.delete(0, END)

        def addData():
            if len(stdId.get()) != 0:
                stdDataBase_BackEnd.addStdRec(stdId.get(), firstName.get(), surname.get(), dob.get(), age.get(),
                                              gender.get(), address.get(), mobile.get())
                studentList.delete(0, END)
                studentList.insert(END, (stdId.get(), firstName.get(), surname.get(), dob.get(), age.get(),
                                         gender.get(), address.get(), mobile.get()))

        def displayData():
            studentList.delete(0, END)
            for row in stdDataBase_BackEnd.viewData():
                studentList.insert(END, row, str(""))

        def studentRec(event):
            global sd
            searchStd = studentList.curselection()[0]
            sd = studentList.get(searchStd)

            self.txtstdID.delete(0, END)
            self.txtstdID.insert(END, sd[1])
            self.txtfname.delete(0, END)
            self.txtfname.insert(END, sd[2])
            self.txtsname.delete(0, END)
            self.txtsname.insert(END, sd[3])
            self.txtdob.delete(0, END)
            self.txtdob.insert(END, sd[4])
            self.txtage.delete(0, END)
            self.txtage.insert(END, sd[5])
            self.txtgender.delete(0, END)
            self.txtgender.insert(END, sd[6])
            self.txtaddress.delete(0, END)
            self.txtaddress.insert(END, sd[7])
            self.txtmobile.delete(0, END)
            self.txtmobile.insert(END, sd[8])

        def deleteData():
            if len(stdId.get()) != 0:
                stdDataBase_BackEnd.deleteRec(sd[0])
                clearData()
                displayData()

        def searchDatabase():
            studentList.delete(0, END)
            for row in stdDataBase_BackEnd.searchData(stdId.get(), firstName.get(), surname.get(), dob.get(), age.get(),
                                                      gender.get(), address.get(), mobile.get()):
                studentList.insert(END, row, str(""))

        def updateData():
            if len(stdId.get()) != 0:
                stdDataBase_BackEnd.deleteRec(sd[0])
            if len(stdId.get()) != 0:
                stdDataBase_BackEnd.addStdRec(stdId.get(), firstName.get(), surname.get(), dob.get(), age.get(),
                                              gender.get(), address.get(), mobile.get())
                studentList.delete(0, END)
                studentList.insert(END, (stdId.get(), firstName.get(), surname.get(), dob.get(), age.get(),
                                         gender.get(), address.get(), mobile.get()))

        # ==========================FRAMES========================== #
        MainFrame = Frame(self.root, bg="cadet blue")
        MainFrame.grid()

        TitFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="ghost white", relief=RIDGE)
        TitFrame.pack(side=TOP)

        self.IblTitle = Label(TitFrame,
                              font=('arial', 47, 'bold'),
                              text="Student Database Management System",
                              bg="ghost white")
        self.IblTitle.grid()

        ButtonFrame = Frame(MainFrame, bd=2,
                            width=1350, height=70,
                            padx=18, pady=10, bg="ghost white",
                            relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=1,
                          width=1300, height=400,
                          padx=20, pady=20, bg="cadet blue",
                          relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLeft = LabelFrame(DataFrame, bd=1,
                                   width=1000, height=600,
                                   padx=20, bg="ghost white",
                                   font=('arial', 20, 'bold'), text="Student Info\n",
                                   relief=RIDGE)
        DataFrameLeft.pack(side=LEFT)

        DataFrameRight = LabelFrame(DataFrame, bd=1,
                                    width=450, height=300,
                                    padx=31, pady=3, bg="ghost white",
                                    font=('arial', 20, 'bold'), text="Student Details\n",
                                    relief=RIDGE)
        DataFrameRight.pack(side=RIGHT)

        # ==========================LABELS & Entry Widget========================== #

        # student ID
        self.IblstdID = Label(DataFrameLeft,
                              font=('arial', 20, 'bold'),
                              text="Student ID",
                              padx=2, pady=2, bg="ghost white")
        self.IblstdID.grid(row=0, column=0, sticky=W)
        self.txtstdID = Entry(DataFrameLeft,
                              font=('arial', 20, 'bold'),
                              textvariable=stdId,
                              width=39)
        self.txtstdID.grid(row=0, column=1)

        # student firstname
        self.Iblfname = Label(DataFrameLeft,
                              font=('arial', 20, 'bold'),
                              text="First Name",
                              padx=2, pady=2, bg="ghost white")
        self.Iblfname.grid(row=1, column=0, sticky=W)
        self.txtfname = Entry(DataFrameLeft,
                              font=('arial', 20, 'bold'),
                              textvariable=firstName,
                              width=39)
        self.txtfname.grid(row=1, column=1)

        # student surname
        self.Iblsname = Label(DataFrameLeft,
                              font=('arial', 20, 'bold'),
                              text="Surname",
                              padx=2, pady=2, bg="ghost white")
        self.Iblsname.grid(row=2, column=0, sticky=W)
        self.txtsname = Entry(DataFrameLeft,
                              font=('arial', 20, 'bold'),
                              textvariable=surname,
                              width=39)
        self.txtsname.grid(row=2, column=1)

        # student dob
        self.Ibldob = Label(DataFrameLeft,
                            font=('arial', 20, 'bold'),
                            text="Date Of Birth",
                            padx=2, pady=2, bg="ghost white")
        self.Ibldob.grid(row=3, column=0, sticky=W)
        self.txtdob = Entry(DataFrameLeft,
                            font=('arial', 20, 'bold'),
                            textvariable=dob,
                            width=39)
        self.txtdob.grid(row=3, column=1)

        # student age
        self.Iblage = Label(DataFrameLeft,
                            font=('arial', 20, 'bold'),
                            text="Age",
                            padx=2, pady=2, bg="ghost white")
        self.Iblage.grid(row=4, column=0, sticky=W)
        self.txtage = Entry(DataFrameLeft,
                            font=('arial', 20, 'bold'),
                            textvariable=age,
                            width=39)
        self.txtage.grid(row=4, column=1)

        # student gender
        self.Iblgender = Label(DataFrameLeft,
                               font=('arial', 20, 'bold'),
                               text="Gender",
                               padx=2, pady=2, bg="ghost white")
        self.Iblgender.grid(row=5, column=0, sticky=W)
        self.txtgender = Entry(DataFrameLeft,
                               font=('arial', 20, 'bold'),
                               textvariable=gender,
                               width=39)
        self.txtgender.grid(row=5, column=1)

        # student address
        self.Ibladdress = Label(DataFrameLeft,
                                font=('arial', 20, 'bold'),
                                text="Address",
                                padx=2, pady=2, bg="ghost white")
        self.Ibladdress.grid(row=6, column=0, sticky=W)
        self.txtaddress = Entry(DataFrameLeft,
                                font=('arial', 20, 'bold'),
                                textvariable=address,
                                width=39)
        self.txtaddress.grid(row=6, column=1)

        # student mobile
        self.Iblmobile = Label(DataFrameLeft,
                               font=('arial', 20, 'bold'),
                               text="Mobile Number",
                               padx=2, pady=2, bg="ghost white")
        self.Iblmobile.grid(row=7, column=0, sticky=W)
        self.txtmobile = Entry(DataFrameLeft,
                               font=('arial', 20, 'bold'),
                               textvariable=mobile,
                               width=39)
        self.txtmobile.grid(row=7, column=1)

        # ==========================ListBox & ScrollBar Widget========================== #

        scrollbar = Scrollbar(DataFrameRight)
        scrollbar.grid(row=0, column=1, sticky='ns')

        studentList = Listbox(DataFrameRight,
                              width=42, height=16,
                              font=('arial', 12, 'bold'),
                              yscrollcommand=scrollbar.set)
        studentList.bind('<<ListboxSelect>>', studentRec)
        studentList.grid(row=0, column=0, padx=8)
        scrollbar.config(command=studentList.yview)

        # ==========================Button Widget========================== #

        self.btnAddData = Button(ButtonFrame, text="Add New",
                                 width=10, height=1, bd=4,
                                 font=('arial', 20, 'bold'),
                                 command=addData)
        self.btnAddData.grid(row=0, column=0)

        self.btnDisplayData = Button(ButtonFrame, text="Display",
                                     width=10, height=1, bd=4,
                                     font=('arial', 20, 'bold'),
                                     command=displayData)
        self.btnDisplayData.grid(row=0, column=1)

        self.btnClearData = Button(ButtonFrame, text="Clear",
                                   width=10, height=1, bd=4,
                                   font=('arial', 20, 'bold'),
                                   command=clearData)
        self.btnClearData.grid(row=0, column=2)

        self.btnDeleteData = Button(ButtonFrame, text="Delete",
                                    width=10, height=1, bd=4,
                                    font=('arial', 20, 'bold'),
                                    command=deleteData)
        self.btnDeleteData.grid(row=0, column=3)

        self.btnSearchData = Button(ButtonFrame, text="Search",
                                    width=10, height=1, bd=4,
                                    font=('arial', 20, 'bold'),
                                    command=searchDatabase)
        self.btnSearchData.grid(row=0, column=4)

        self.btnUpdateData = Button(ButtonFrame, text="Update",
                                 width=10, height=1, bd=4,
                                 font=('arial', 20, 'bold'),
                                 command=updateData)
        self.btnUpdateData.grid(row=0, column=5)

        self.btnExit = Button(ButtonFrame, text="Exit",
                                 width=10, height=1, bd=4,
                                 font=('arial', 20, 'bold'),
                                 command=iExit)
        self.btnExit.grid(row=0, column=6)


if __name__ == '__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()
