from tkinter import *
from tkinter import messagebox, ttk
import os

class filesystem:
    
    def __init__(self):
        self.root=Tk()
        self.root.title("Criminal Record System")
        self.root.iconbitmap("Images/logo.ico")
        self.root.geometry("1110x630")
        self.root.config(background='#002447')
       
        self.c_id=StringVar()
        self.name=StringVar()
        self.age=StringVar()
        self.sex=StringVar()
        self.profession=StringVar()
        self.crime=StringVar()
        self.jailtime=StringVar()
        self.entrydate=StringVar()
        self.security=StringVar()
        self.offence=StringVar()
        self.search=StringVar()

        title = Label(self.root,text="Criminal Record System", bd=5,relief=GROOVE, bg='#002447',fg='yellow', pady=10,font=("times new roman",30,"bold")).grid(row=0,columnspan=2, sticky=E+W+S+N)

        Prisoner_Frame=Frame(self.root,bd=5,relief=GROOVE, bg='#002447')
        Prisoner_Frame.grid(row=1,column=0, sticky=E+W+S+N)
        
        stitle= Label(Prisoner_Frame,text="Convict Details",font=("times new roman",20,"bold"), bg='#002447',fg='white').grid(row=0,columnspan=2,padx=10,pady=20)


        txtsearch=Entry(Prisoner_Frame,textvariable=self.search,bd=3,relief=GROOVE,width=20,font="Arial 15 bold",bg='white',fg='Black').grid(row=0,column=2,padx=0,pady=10,sticky="e")
        btnsearch=Button(Prisoner_Frame,text="Search",font="arial 12 bold",bd=2,width=10,command=self.find,bg='light blue',fg='#002447').grid(row=0,column=3,padx=0,pady=10,sticky="w")
        
##  Column 1  ## 
        lblcid= Label(Prisoner_Frame,text="Convict ID",font=("times new roman",15,"bold"),bg='#002447',fg='peachpuff').grid(row=1,column=0,pady=20,padx=20,sticky="w")
        txtcid=Entry(Prisoner_Frame,textvariable=self.c_id,bd=3,relief=GROOVE,width=22,font="Arial 15 bold").grid(row=1,column=1,padx=10,pady=10)
        
        lblname= Label(Prisoner_Frame,text="Name",font=("times new roman",15,"bold"),bg='#002447',fg='peachpuff').grid(row=2,column=0,pady=20,padx=20,sticky="w")
        txtname=Entry(Prisoner_Frame,textvariable=self.name,bd=3,relief=GROOVE,width=22,font="Arial 15 bold").grid(row=2,column=1,padx=10,pady=10)
        
        lblage= Label(Prisoner_Frame,text="Age",font=("times new roman",15,"bold"),bg='#002447',fg='peachpuff').grid(row=3,column=0,pady=20,padx=20,sticky="w")
        txtage=Entry(Prisoner_Frame,textvariable=self.age,bd=3,relief=GROOVE,width=22,font="Arial 15 bold").grid(row=3,column=1,padx=10,pady=10)
        
        lblsex= Label(Prisoner_Frame,text="Sex",font=("times new roman",15,"bold"),bg='#002447',fg='peachpuff').grid(row=4,column=0,pady=20,padx=20,sticky="w")
        sexcombo=ttk.Combobox(Prisoner_Frame,textvariable=self.sex,width=20,state="readonly",font="arial 15 bold")
        sexcombo['values']=("Male","Female","Others")
        sexcombo.grid(row=4,column=1,padx=10,pady=10)
                 
        lblprofession= Label(Prisoner_Frame,text="Occupation",font=("times new roman",15,"bold"),bg='#002447',fg='peachpuff').grid(row=5,column=0,pady=20,padx=20,sticky="w")
        txtprofession=Entry(Prisoner_Frame,textvariable=self.profession,bd=3,relief=GROOVE,width=22,font="Arial 15 bold").grid(row=5,column=1,padx=10,pady=10)

##  Column 2  ##        
        lblcrime= Label(Prisoner_Frame,text="Crime",font=("times new roman",15,"bold"),bg='#002447',fg='peachpuff').grid(row=1,column=2,pady=20,padx=20,sticky="w")
        txtcrime=Entry(Prisoner_Frame,textvariable=self.crime,bd=3,relief=GROOVE,width=22,font="Arial 15 bold").grid(row=1,column=3,padx=10,pady=10)
        
        lbljailtime= Label(Prisoner_Frame,text="Jailtime",font=("times new roman",15,"bold"),bg='#002447',fg='peachpuff').grid(row=2,column=2,pady=20,padx=20,sticky="w")
        txtjailtime=Entry(Prisoner_Frame,textvariable=self.jailtime,bd=3,relief=GROOVE,width=22,font="Arial 15 bold").grid(row=2,column=3,padx=10,pady=10)
        
        lblentrydate= Label(Prisoner_Frame,text="Conviction Date",font=("times new roman",15,"bold"),bg='#002447',fg='peachpuff').grid(row=3,column=2,pady=20,padx=20,sticky="w")
        txtentrydate=Entry(Prisoner_Frame,textvariable=self.entrydate,bd=3,relief=GROOVE,width=22,font="Arial 15 bold").grid(row=3,column=3,padx=10,pady=10)
        
        lblsecurity= Label(Prisoner_Frame,text="Security Level",font=("times new roman",15,"bold"),bg='#002447',fg='peachpuff').grid(row=4,column=2,pady=20,padx=20,sticky="w")
        securitycombo=ttk.Combobox(Prisoner_Frame,textvariable=self.security,width=20,state="readonly",font="arial 15 bold")
        securitycombo['values']=("Low","Medium","High","Critical")
        securitycombo.grid(row=4,column=3,padx=10,pady=10)
        
        lbloffence= Label(Prisoner_Frame,text="Previous Offences",font=("times new roman",15,"bold"),bg='#002447',fg='peachpuff').grid(row=5,column=2,pady=20,padx=20,sticky="w")
        txtoffence=Entry(Prisoner_Frame,textvariable=self.offence,bd=3,relief=GROOVE,width=22,font="Arial 15 bold").grid(row=5,column=3,padx=10,pady=10)
        
        stitle= Label(Prisoner_Frame,text="", bg='#002447').grid(row=6,columnspan=4,pady=10)
        
        btnframe=Frame(self.root,bd=5,relief=GROOVE, bg='#002447')
        # btnframe.pack(side=BOTTOM,fill=X)
        btnframe.grid(row=2,columnspan=2,sticky=E+W+S+N)

        btnsave=Button(btnframe,text="Save",font="arial 15 bold",bd=5,width=15,command=self.save_data,bg='light blue',fg='#002447').grid(row=0,column=0,padx=12,pady=10)
        btndelete=Button(btnframe,text="Delete",font="arial 15 bold",bd=5,width=15,command=self.delete,bg='light blue',fg='#002447').grid(row=0,column=1,padx=12,pady=10)
        btnclear=Button(btnframe,text="Clear",font="arial 15 bold",bd=5,width=15,command=self.clear,bg='light blue',fg='#002447').grid(row=0,column=2,padx=12,pady=10)
        btnlog=Button(btnframe,text="Logout",font="arial 15 bold",bd=5,width=15,command=self.logout,bg='light blue',fg='#002447').grid(row=0,column=3,padx=12,pady=10)
        btnexit=Button(btnframe,text="Exit",font="arial 15 bold",bd=5,width=15,command=self.exit,bg='light blue',fg='#002447').grid(row=0,column=4,padx=12,pady=10)

        fileframe=Frame(self.root,bd=5,relief=GROOVE, bg='#002447')
        fileframe.grid(row=1,column=1,ipadx=10,ipady=10,sticky=E+W+S+N)

        ftitle=Label(fileframe,text="Logs",font=("times new roman",20,"bold"),bg='#002447',fg='white').pack(side=TOP,fill=X,pady=20)
        
        scrolly=Scrollbar(fileframe,orient=VERTICAL)
        self.filelist=Listbox(fileframe,yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.filelist.yview)
        self.filelist.pack(fill=BOTH,expand=1)
        self.filelist.bind("<ButtonRelease-1>",self.get_data)
        self.show_files()
        self.root.mainloop()
        
    def save_data(self):
        present="no"
        if self.c_id.get()=="":
            messagebox.showerror("Error","Convict's ID required.")
        else:
            f=os.listdir("files/")
            if len(f)>0:
                for i in f:
                    if i.split(".")[0]==self.c_id.get():
                        present="yes"

                if present=="yes":
                    ask=messagebox.askyesno("Update","File already Exists. \nDo you want to update?")
                    if ask>0:
                        self.save_file()
                        messagebox.showinfo("Update","Record has been update.")
                        self.show_files()
                else:
                    self.save_file()  
                    messagebox.showinfo("Saved","Record has been saved.")
                    self.show_files() 

            else:
                self.save_file()  
                messagebox.showinfo("Saved","Record has been saved.")
                self.show_files()      


    def save_file(self):
        f=open("files/"+str(self.c_id.get())+".txt","w")
        f.write(
            str(self.c_id.get())+","+
            str(self.name.get())+","+
            str(self.age.get())+","+
            str(self.sex.get())+","+
            str(self.profession.get())+","+
            str(self.crime.get())+","+
            str(self.jailtime.get())+","+
            str(self.entrydate.get())+","+
            str(self.security.get())+","+
            str(self.offence.get())
            )
        f.close()

    def show_files(self):
        files=os.listdir("files/")
        self.filelist.delete(0,END)
        if len(files)>0:
            for i in files:
                self.filelist.insert(END,i)
    
    def get_data(self,ev):
        get_cursor=self.filelist.curselection()
        f1=open("files/"+self.filelist.get(get_cursor))
        value=[]
        for f in f1:
            value=f.split(",")
        self.c_id.set(value[0])
        self.name.set(value[1])
        self.age.set(value[2])
        self.sex.set(value[3])
        self.profession.set(value[4])
        self.crime.set(value[5])
        self.jailtime.set(value[6])
        self.entrydate.set(value[7])
        self.security.set(value[8])
        self.offence.set(value[9])

    def clear(self):
        self.c_id.set("")
        self.name.set("")
        self.age.set("")
        self.sex.set("")
        self.profession.set("")
        self.crime.set("")
        self.jailtime.set("")
        self.entrydate.set("")
        self.security.set("")
        self.offence.set("")

    def delete(self):
        present="no"
        if self.c_id.get()=="":
            messagebox.showerror("Error","Convict's ID required.")
        else:
            f=os.listdir("files/")
            if len(f)>0:
                for i in f:
                    if i.split(".")[0]==self.c_id.get():
                        present="yes"
                if present=="yes":
                    ask=messagebox.askyesno("Delete","Do you want to delete?")
                    if ask>0:
                        os.remove("files/"+self.c_id.get()+".txt")
                        messagebox.showinfo("Success","Deleted Successfully")
                        self.show_files()
                else:
                    messagebox.showerror("Error","Files not Found")
                    
    def exit(self):
        ask=messagebox.askyesno("Exit","Do you want to exit?")
        if ask>0:
            self.root.destroy()

    def logout(self):
        self.root.destroy()
        import login

    def find(self):
        present="no"
        for i in os.listdir("files/"):
            if i.split('.')[0]==self.search.get():
                f1=open(f"files/{i}","r")
                value=[]
                for f in f1:
                    value=f.split(",")
                    self.c_id.set(value[0])
                    self.name.set(value[1])
                    self.age.set(value[2])
                    self.sex.set(value[3])
                    self.profession.set(value[4])
                    self.crime.set(value[5])
                    self.jailtime.set(value[6])
                    self.entrydate.set(value[7])
                    self.security.set(value[8])
                    self.offence.set(value[9])
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Not found.")

