from cProfile import label
from logging import root
from msilib.schema import ListBox
from tkinter import *
from tkinter import ttk
from pandas import DataFrame


class libsystm:
    def __init__(self,root):
            self.root=root
            self.root.title("Library Management System")
            self.root.geometry("1550x800+0+0")
#Title
            libtitle=Label(self.root,text="LIBRARAY MANAGEMENT SYSTEM",bg="powder blue",bd=15,fg="red",relief=RIDGE,font=("times new roman",40,"bold"),padx=2,pady=6)
            libtitle.pack(side=TOP,fill=X)

            frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
            frame.place(x=0,y=100,width=1535,height=400)
#Left Frame
            DataFrameLeft=LabelFrame(frame,text="Library member Information",bg="powder blue",fg="red",bd=10,relief=RIDGE,font=("times new roman",12,"bold"),padx=2,pady=6)
            DataFrameLeft.grid(row=0,column=0,sticky=W)

            lgbmem=Label(DataFrameLeft,bg="powder blue",text="Member Type:-",font=("times new roman",12,"bold"),padx=2,pady=6)
            lgbmem.grid(row=0,column=0,sticky=W)
            commem=ttk.Combobox(DataFrameLeft,state="readonly",font=("arial",12),width=27)
            commem['value']=("Admin","Teacher","Student")
            commem.current(0)
            commem.grid(row=0,column=1)
            
            
            lgbln=Label(DataFrameLeft,bg="powder blue",text="Lib No:-",font=("times new roman",12,"bold"),padx=2,pady=6)
            lgbln.grid(row=1,column=0,sticky=W)
            textln=Entry(DataFrameLeft,font=("arial",12),width=27)
            textln.grid(row=1,column=1)

            lgbregno=Label(DataFrameLeft,bg="powder blue",text="Reg No:-",font=("times new roman",12,"bold"),padx=2,pady=6)
            lgbregno.grid(row=2,column=0,sticky=W)
            textregno=Entry(DataFrameLeft,font=("arial",12),width=27)
            textregno.grid(row=2,column=1)

            lgbfn=Label(DataFrameLeft,bg="powder blue",text="First Name:-",font=("times new roman",12,"bold"),padx=2,pady=6)
            lgbfn.grid(row=3,column=0,sticky=W)
            textfn=Entry(DataFrameLeft,font=("arial",12),width=27)
            textfn.grid(row=3,column=1)

            lgblm=Label(DataFrameLeft,bg="powder blue",text="Last Name:-",font=("times new roman",12,"bold"),padx=2,pady=6)
            lgblm.grid(row=4,column=0,sticky=W)
            textlm=Entry(DataFrameLeft,font=("arial",12),width=27)
            textlm.grid(row=4,column=1)

            lgba2=Label(DataFrameLeft,bg="powder blue",text="Address 1:-",font=("times new roman",12,"bold"),padx=2,pady=6)
            lgba2.grid(row=5,column=0,sticky=W)
            texta2=Entry(DataFrameLeft,font=("arial",12),width=27)
            texta2.grid(row=5,column=1)

            lgba2=Label(DataFrameLeft,bg="powder blue",text="Address 2:-",font=("times new roman",12,"bold"),padx=2,pady=6)
            lgba2.grid(row=6,column=0,sticky=W)
            texta2=Entry(DataFrameLeft,font=("arial",12),width=27)
            texta2.grid(row=6,column=1)

            lgbpc=Label(DataFrameLeft,bg="powder blue",text="Pincode:-",font=("times new roman",12,"bold"),padx=2,pady=6)
            lgbpc.grid(row=7,column=0,sticky=W)
            textpc=Entry(DataFrameLeft,font=("arial",12),width=27)
            textpc.grid(row=7,column=1)

            lgbmn=Label(DataFrameLeft,bg="powder blue",text="Mobile No:-",font=("times new roman",12,"bold"),padx=2,pady=6)
            lgbmn.grid(row=8,column=0,sticky=W)
            textmn=Entry(DataFrameLeft,font=("arial",12),width=27)
            textmn.grid(row=8,column=1)

            lgbbi=Label(DataFrameLeft,bg="powder blue",text="Book ID:-",font=("times new roman",12,"bold"),padx=2,pady=6)
            lgbbi.grid(row=0,column=2,sticky=W)
            textbi=Entry(DataFrameLeft,font=("arial",12),width=27)
            textbi.grid(row=0,column=3)

            lgbbt=Label(DataFrameLeft,bg="powder blue",text="Book Title:-",font=("times new roman",12,"bold"),padx=2,pady=6)
            lgbbt.grid(row=1,column=2,sticky=W)
            textbt=Entry(DataFrameLeft,font=("arial",12),width=27)
            textbt.grid(row=1,column=3)

            lgban=Label(DataFrameLeft,bg="powder blue",text="Author Name:-",font=("times new roman",12,"bold"),padx=2,pady=6)
            lgban.grid(row=2,column=2,sticky=W)
            textan=Entry(DataFrameLeft,font=("arial",12),width=27)
            textan.grid(row=2,column=3)

            lgbid=Label(DataFrameLeft,bg="powder blue",text="Issued Date:-",font=("times new roman",12,"bold"),padx=2,pady=6)
            lgbid.grid(row=3,column=2,sticky=W)
            textid=Entry(DataFrameLeft,font=("arial",12),width=27)
            textid.grid(row=3,column=3)

            lgbdd=Label(DataFrameLeft,bg="powder blue",text="Due Date:-",font=("times new roman",12,"bold"),padx=2,pady=6)
            lgbdd.grid(row=4,column=2,sticky=W)
            textdd=Entry(DataFrameLeft,font=("arial",12),width=27)
            textdd.grid(row=4,column=3)

            lgbdob=Label(DataFrameLeft,bg="powder blue",text="Days on Book:-",font=("times new roman",12,"bold"),padx=2,pady=6)
            lgbdob.grid(row=5,column=2,sticky=W)
            textdob=Entry(DataFrameLeft,font=("arial",12),width=27)
            textdob.grid(row=5,column=3)

            lgblrf=Label(DataFrameLeft,bg="powder blue",text="Late Return Fine:-",font=("times new roman",12,"bold"),padx=2,pady=6)
            lgblrf.grid(row=6,column=2,sticky=W)
            textlrf=Entry(DataFrameLeft,font=("arial",12),width=27)
            textlrf.grid(row=6,column=3)

            lgbdod=Label(DataFrameLeft,bg="powder blue",text="Date Over Due:-",font=("times new roman",12,"bold"),padx=2,pady=6)
            lgbdod.grid(row=7,column=2,sticky=W)
            textdod=Entry(DataFrameLeft,font=("arial",12),width=27)
            textdod.grid(row=7,column=3)

            lgbac=Label(DataFrameLeft,bg="powder blue",text="Actual Price:-",font=("times new roman",12,"bold"),padx=2,pady=6)
            lgbac.grid(row=8,column=2,sticky=W)
            textac=Entry(DataFrameLeft,font=("arial",12),width=27)
            textac.grid(row=8,column=3)



        #Rightframe
            DataFrameRig=LabelFrame(frame,text="BOOK DETAILS",bg="powder blue",bd=12,fg="black",relief=RIDGE,font=("times new roman",12,"bold"))
            DataFrameRig.place(x=910,y=5,width=570,height=360)

            self.textBox=Text(DataFrameRig,font=("times new roman",12,"bold"),width=32,padx=2,pady=6,height=16)
            self.textBox.grid(row=0,column=2)

            listscrool=Scrollbar(DataFrameRig)
            listscrool.grid(row=0,column=1,sticky="ns")

            listBooks=["Python Programming","C Programming","C++ Programming","Java Programming"] 
            booklist=Listbox(DataFrameRig,width=20,height=16,font=("arial",12,"bold"))
            booklist.bind("<<ListBoxSelect>>")
            booklist.grid(row=0,column=0,padx=4)
            listscrool.config(command=booklist.yview)

            for items in listBooks:
                    booklist.insert(END,items)
            


        #Buttons
            framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
            framebutton.place(x=0,y=500,width=1540,height=70)

            buadd=Button(framebutton,text="ADD DATA",font=("arial",12,"bold"),width=23,height=2,bg="black",fg="white")
            buadd.grid(row=0,column=0,padx=2)

            bushwd=Button(framebutton,text="SHOW DATA",font=("arial",12,"bold"),width=23,height=2,bg="black",fg="white")
            bushwd.grid(row=0,column=1,padx=2)

            buup=Button(framebutton,text="UPDATE",font=("arial",12,"bold"),width=23,height=2,bg="black",fg="white")
            buup.grid(row=0,column=2,padx=2)

            budel=Button(framebutton,text="DELETE",font=("arial",12,"bold"),width=23,height=2,bg="black",fg="white")
            budel.grid(row=0,column=3,padx=2)

            bures=Button(framebutton,text="RESET",font=("arial",12,"bold"),width=23,height=2,bg="black",fg="white")
            bures.grid(row=0,column=4,padx=2)

            buexi=Button(framebutton,text="EXIT",font=("arial",12,"bold"),width=23,height=2,bg="black",fg="white")
            buexi.grid(row=0,column=5,padx=2)
        #Info
            frameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
            frameDetails.place(x=0,y=570,width=1540,height=230)

            Table_frame=Frame(frameDetails,bd=6,relief=RIDGE,bg="powder blue")
            Table_frame.place(x=0,y=2,width=1470,height=205)

            self.library_table=ttk.Treeview(Table_frame,column=("lib no","reg no","first name","last Name",
                                                                "address1","address2","pincode","mobile No",
                                                                "book id","book Title","author Name","issued Date",
                                                                "due Date","days On Book","late Return Fine",
                                                                "date over Due","final Price"))

            self.library_table.heading("lib no",text="Lib no")
            self.library_table.heading("reg no",text="Reg no")
            self.library_table.heading("first Name",text="First Name")
            self.library_table.heading("last Name",text="Last Name")
            self.library_table.heading("address1",text="Address1")
            self.library_table.heading("address2",text="Address2")
            self.library_table.heading("pincode",text="Pincode")
            self.library_table.heading("mobile No",text="Mobile No")
            self.library_table.heading("book id",text="Book id")
            self.library_table.heading("book Title",text="Book Title")
            self.library_table.heading("author Name",text="Author Name")
            self.library_table.heading("issued Date",text="Issued Date")
            self.library_table.heading("due Date",text="Due Date")
            self.library_table.heading("days On Book",text="Days On Book")
            self.library_table.heading("late Return Fine",text="Late Return Fine")
            self.library_table.heading("date over Due",text="Date over Due")
            self.library_table.heading("final Price",text="Final Price")

            self.library_table["show"]="headings"
            self.library_table.pack(fill=BOTH,expand=1)

                


if __name__=="__main__":
    root=Tk()
    obj=libsystm(root)
    root.mainloop()