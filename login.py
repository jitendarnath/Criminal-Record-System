from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Criminal Record System")
root.iconbitmap("Images/logo.ico")
root.geometry("1000x600")
root.config(background='#002447')

class login:
    def __init__(self,root):

        self.root=root
        self.user=StringVar()
        self.password=StringVar()

        F1=Frame(self.root,bg='#002447')
        F1.pack(expand=YES)

        
        self.img = PhotoImage(file="Images/handcuffs.png").zoom(20).subsample(32)
        canvas = Canvas(F1, width=400, height=400, bg='#002447', bd=0, highlightthickness=0)
        canvas.create_image(400/2,400/2,image=self.img)
        canvas.grid(row=0,column=0,sticky=W)

        right_frame = Frame(F1, bg='#002447',bd=5,highlightthickness=0)        
        right_frame.grid(row=0, column=1,sticky=W,padx=30)

        title=Label(right_frame,text="Admin Authorization", bd=3, relief=GROOVE, pady=10, font=("Helvetica",27,'bold'),bg='#002447',fg='Yellow')
        title.grid(row=0,columnspan=4,pady=20,sticky='we')

        userlabel=Label(right_frame,text="Username :",font=("Helvetica",20,'bold'),bg='#002447',fg='light blue')
        userlabel.grid(row=1,column=0,pady=10,padx=10)

        userentry=Entry(right_frame,textvariable=self.user,width=15,font="Helvetica 18 bold",bg='#324f6b',fg='peachpuff')
        userentry.grid(row=1,column=1,pady=10,padx=10)
        
        passlabel=Label(right_frame,text="Password :",font=("Helvetica",20,'bold'),bg='#002447',fg='light blue')
        passlabel.grid(row=2,column=0,pady=10,padx=10)

        passentry=Entry(right_frame,textvariable=self.password,show="*",width=15,font="Helvetica 18 bold",bg='#324f6b',fg='peachpuff')
        passentry.grid(row=2,column=1,pady=10,padx=10)

        btnlog=Button(right_frame,text="Login",font=("Helvetica",20,'bold'),bg='light blue',fg='#002447',command=self.login)
        btnlog.grid(row=4,column=0,columnspan=4,pady=20,sticky="we")

        footer_title = Label(self.root,text="2020 | Jitendar Nath | VIT", font="Sanseriff 10",bg='#002447',fg='grey',borderwidth=1,relief=RIDGE,pady=5)
        footer_title.pack(side=BOTTOM,fill=X)

    def login(self):
        if self.user.get()=="admin" and self.password.get()=="admin":
            # messagebox.showinfo("Info",f"Authorization Granted.")
            self.root.destroy()
            import main
            main.filesystem()
        else:
            self.user.set("")
            self.password.set("")
            messagebox.showerror("Error","Authorization Revoked.")

ob=login(root)
root.mainloop()