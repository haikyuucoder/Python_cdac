#Design a Login and Register Screen

from tkinter import *

class MyWindow():
    def __init__(self,master):
        self.frame1=Frame(master=master)
        master.title("Window 1")
        self.master=master
        self.create_widgets()
        self.frame1.pack()

    def create_widgets(self):
        self.registered=0
        self.label=Label(self.frame1,text="LOGIN",bg="lightgreen",font=("bold",16))
        self.label.grid(row=0,column=0,columnspan=10)
        self.l_user=Label(self.frame1,text="User ID",bg='Yellow',height=2,width=20)
        self.l_user.grid(row=1,column=4,pady=1)
        self.e_user=Entry(self.frame1,width=18)
        self.e_user.grid(row=1, column=5,columnspan=2)
        self.l_pass=Label(self.frame1,text="Password",bg='Yellow',height=2,width=20)
        self.l_pass.grid(row=2, column=4,pady=1)
        self.e_pass = Entry(self.frame1,show="*",width=18)
        self.e_pass.grid(row=2,column=5,columnspan=2)

        self.login=Button(self.frame1,text="Login")
        self.login.bind('<Button-1>',self.login_show)
        self.login.grid(row=6,column=4,padx=2,pady=2)
        self.register=Button(self.frame1,text="Register")
        self.register.bind('<Button-1>',self.register_show)
        self.register.grid(row=6,column=6,padx=2,pady=2)

        self.list=Label(self.frame1,text="Level in Programming:")
        self.list.grid(row=4,column=4)
        self.l=['Beginner','Intermediate','Expert']
        self.listbox=Listbox(self.frame1,height=3)
        for i in self.l:
            self.listbox.insert(END,i)
        self.listbox.grid(row=4,column=6)

        self.city=Label(self.frame1,text="City")
        self.city.grid(row=5,column=4)
        self.var1=StringVar()
        self.var1.set("Choose..")
        self.options=OptionMenu(self.frame1,self.var1,"Chandigarh","Mohali","Panchkula")
        self.options.grid(row=5,column=6)

        self.var=StringVar()
        self.radiomale=Radiobutton(self.frame1,text="Male",variable=self.var,value='Male')
        self.radiofemale=Radiobutton(self.frame1,text="Female",variable=self.var,value='Female')
        self.gender=Label(self.frame1,text="Gender: ")
        self.gender.grid(row=3,column=4)
        self.radiomale.grid(row=3,column=5)
        self.radiofemale.grid(row=3,column=6)

    def login_show(self,event):
        self.w_login = Tk()
        self.w_login.geometry("200x50")
        if(self.registered==1):
            self.w_login.title("Succesful")
            label=Label(self.w_login,text="Login is Success.")
            label.pack()
        else:
            self.w_login.title("Not Registered!")
            label = Label(self.w_login, text="Kindly Register first.")
            label.pack()

    def register_show(self,event):
        print("Registered")
        print("Username: ",self.e_user.get())
        print("Password: ",self.e_pass.get())
        print("Gender: ", self.var.get())
        print("Level of Programming: ", self.listbox.get(ACTIVE))
        print("City: ", self.var1.get())
        self.registered=1

def main():
    root1=Tk()
    app=MyWindow(root1)
    root1.mainloop()

if(__name__=='__main__'):
    main()