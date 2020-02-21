from mysql.connector import connection
from mysql.connector import Error
try:
    # Design a Login and Register Screen
    db=connection.MySQLConnection(host="localhost",user="root",password="root",charset="utf8")
    c=db.cursor()
    s="create database if not exists student"
    c.execute(s)
    c.execute("use student")
    s="create table if not exists login(username varchar(15) primary key not null,password varchar(9),e_name varchar(25),gender varchar(10),level_prog varchar(15),city varchar(15))"
    c.execute(s)

    from tkinter import *
    from tkinter import messagebox


    class MyWindow():
        def __init__(self, master):
            self.frame1 = Frame(master=master,bg="#d4d4dc")
            master.title("Register")
            master.configure(background="#d4d4dc")
            master.geometry("300x300")
            self.master = master
            self.create_widgets()
            self.frame1.pack()

        def create_widgets(self):
            # c2b490
            self.registered = 0
            self.label = Label(self.frame1, text="REGISTER",bg="green",fg="white", font=("bold", 16))
            self.label.grid(row=0, column=0, columnspan=10,sticky="nsew")
            self.l_user = Label(self.frame1, text="User ID",bg="#d4d4dc")
            self.l_user.grid(row=1, column=4, pady=1)
            self.e_user = Entry(self.frame1, width=18)
            self.e_user.grid(row=1, column=5, columnspan=2)
            self.l_pass = Label(self.frame1, text="Password",bg="#d4d4dc")
            self.l_pass.grid(row=2, column=4, pady=1)
            self.e_pass = Entry(self.frame1, show="*", width=18)
            self.e_pass.grid(row=2, column=5, columnspan=2)
            self.l_name=Label(self.frame1,text="Name",bg="#d4d4dc")
            self.l_name.grid(row=3,column=4)
            self.e_name=Entry(self.frame1,width=18)
            self.e_name.grid(row=3, column=5, columnspan=2)

            self.aau=Label(self.frame1,text="If already a user:",bg="#d4d4dc")
            self.aau.grid(row=8,column=4,columnspan=2,pady=3)
            self.login = Button(self.frame1, text="Login")
            self.login.bind('<Button-1>', self.login_show)
            self.login.grid(row=8, column=5,sticky="e", pady=3)

            self.register = Button(self.frame1, text="Register",font=("bold",16))
            self.register.bind('<Button-1>', self.register_show)
            self.register.grid(row=7, column=4,columnspan=3, padx=3, pady=3)

            self.list = Label(self.frame1, text="Level in Programming:",bg="#d4d4dc")
            self.list.grid(row=5, column=4,sticky="e")
            self.l = ['Beginner', 'Intermediate', 'Expert']
            self.listbox = Listbox(self.frame1, height=3,bg="#d4d4dc")
            for i in self.l:
                self.listbox.insert(END, i)
            self.listbox.grid(row=5, column=5,columnspan=2)

            self.city = Label(self.frame1, text="City",bg="#d4d4dc")
            self.city.grid(row=6, column=4)
            self.var1 = StringVar()
            self.var1.set("Choose..")
            self.options = OptionMenu(self.frame1, self.var1, "Chandigarh", "Mohali", "Panchkula")
            self.options["menu"].config(bg="#d4d4dc")
            self.options.grid(row=6, column=5,columnspan=2)

            self.var = StringVar()
            self.var.set(None)
            self.radiomale = Radiobutton(self.frame1, text="Male", variable=self.var, value='Male',bg="#d4d4dc",selectcolor="#d4d4dc")
            self.radiofemale = Radiobutton(self.frame1, text="Female", variable=self.var, value='Female',bg="#d4d4dc",selectcolor="#d4d4dc")
            self.gender = Label(self.frame1, text="Gender: ",bg="#d4d4dc")
            self.gender.grid(row=4, column=4)
            self.radiomale.grid(row=4, column=5)
            self.radiofemale.grid(row=4, column=6)

        def login_show(self, event):
            self.frame1.destroy()
            obj=login_win(self.master)

        def register_show(self, event):
            if(self.e_user.get()=='' or self.e_pass.get()=='' or self.var.get()=='' or self.listbox.get(ACTIVE)=='' or self.var1.get()=="Choose.."):
                self.mb=messagebox.showwarning(title="Warning",message="Please Enter all fields Correctly")

            else:
                s = "select username from login"
                c.execute(s)
                e = 0
                results = c.fetchall()
                for row in results:
                    if (self.e_user.get() == row[0]):
                        self.mb1 = messagebox.showerror(title="Username Taken", message="Username already exists.")
                        e = 1
                        break;
                if (e != 1):
                    statement = "insert into login values(%s,%s,%s,%s,%s,%s)"
                    rec = (
                    self.e_user.get(), self.e_pass.get(), self.e_name.get(), self.var.get(), self.listbox.get(ACTIVE),
                    self.var1.get())
                    c.execute(statement, rec)
                    db.commit()
                    win = Tk()
                    win.title("Welcome")
                    win.geometry("300x100")
                    l = Label(win, text="Succesfully Registered!!", font=("bold", 20), bg="green",fg="white")
                    l.pack(fill=BOTH, expand=True)
                    print("Registered")
                    print("Username: ", self.e_user.get())
                    print("Password: ", self.e_pass.get())
                    print("Name: ",self.e_name.get())
                    print("Gender: ", self.var.get())
                    print("Level of Programming: ", self.listbox.get(ACTIVE))
                    print("City: ", self.var1.get())



    class login_win():
        def __init__(self,master):
            self.frame1=Frame(master=master,bg="#d4d4dc")
            master.title("Login")
            self.master=master
            self.frame1.pack()
            self.create_widgets()

        def create_widgets(self):
            self.registered = 0
            self.label = Label(self.frame1, text="LOGIN", bg="green",fg="white", font=("bold", 16))
            self.label.grid(row=0, column=0, columnspan=10,sticky="nsew")
            self.l_user = Label(self.frame1, text="User ID", bg="#d4d4dc", height=2, width=20)
            self.l_user.grid(row=1, column=4, pady=1)
            self.e_user = Entry(self.frame1, width=18)
            self.e_user.grid(row=1, column=5, columnspan=2,padx=8)
            self.l_pass = Label(self.frame1, text="Password", bg="#d4d4dc", height=2, width=20)
            self.l_pass.grid(row=2, column=4, pady=1)
            self.e_pass = Entry(self.frame1, show="*", width=18)
            self.e_pass.grid(row=2, column=5, columnspan=2,padx=8)

            self.login = Button(self.frame1, text="Login")
            self.login.bind('<Button-1>', self.login_show)
            self.login.grid(row=6, column=4, padx=2, pady=2)
            self.register = Button(self.frame1, text="Register")
            self.register.bind('<Button-1>', self.register_show)
            self.register.grid(row=6, column=6, padx=2, pady=2)


        def login_show(self,event):
            s="select username,password,e_name from login"
            c.execute(s)
            e=0
            results=c.fetchall()
            for row in results:
                if(self.e_user.get()==row[0] and self.e_pass.get()==row[1]):
                    name=row[2]
                    win = Tk()
                    win.title("Welcome")
                    win.geometry("300x100")
                    l = Label(win, text="Welcome "+name, font=("bold", 20), bg="tomato",fg="white")
                    l.pack(fill=BOTH, expand=True)
                    #self.mb1=messagebox.showinfo(title="Success!!",message="Login Succesful.")
                    e=1
                    break;
            if(e!=1):
                self.win1=Tk()
                self.win1.title("Error")
                lb=Label(self.win1,text="Either Username or password is incorrect",fg="red")
                lb3=Label(self.win1,text="or you haven't registered yet!",fg="red")
                lb.grid(row=0,column=0,columnspan=10)
                lb3.grid(row=1,column=0,columnspan=10)

                lb1=Button(self.win1,text="OK",command=self.closing)
                lb1.grid(row=3,column=4,padx=10,pady=10)
                lb2=Button(self.win1,text="REGISTER")
                lb2.grid(row=3,column=6,padx=10,pady=10)
                lb2.bind("<1>",self.register_show)
        def closing(self):
            self.win1.destroy()
        def register_show(self,event):
            self.frame1.destroy()
            obj=MyWindow(self.master)

    def main():
        root1 = Tk()
        app = MyWindow(root1)
        root1.mainloop()


    if (__name__ == '__main__'):
        main()

except Error as e:
    print(e)
finally:
    db.close()