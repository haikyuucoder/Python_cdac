#Design a Calculator

from tkinter import *

class MyWindow():
    def __init__(self,master):
        self.frame1=Frame(master)
        self.frame1.pack(fill=BOTH)
        master.title("Calculator")
        self.frame2=Frame(self.frame1)
        self.frame2.grid(row=0,column=0,columnspan=50)
        self.frame3=Frame(self.frame2)
        self.frame3.pack(side=BOTTOM,fill=BOTH,expand=True)
        self.result = 0
        self.sign=None
        self.sign1=None

        self.create_widgets()

    '''def file_fun_inter(self,event):
        self.file.bind("<1>",file_fun_final)
        def file_fun(self,ev):
            if(self.var1.get()=='New'):
                print("Hello")
                self.new_win=Tk()
                self.new=MyWindow(root1)'''

    def create_widgets(self):
        '''self.var1=StringVar()

        self.file=OptionMenu(self.frame2,self.var1,"New","Exit")
        self.var1.set("File")
        self.file.bind('<Double-Button-1>',self.file_fun_inter)
        self.file.pack(side=LEFT)
        self.var2=StringVar()
        self.var2.set("About")
        self.about = OptionMenu(self.frame2,self.var2,"About")
        self.about.pack(side=LEFT)'''
        self.vara=Label(self.frame2,text="CALCULATOR",font=("bold",16),bg="lightgreen")
        self.vara.pack()
        self.var3=StringVar()
        self.entry=Entry(self.frame3,textvariable=self.var3,width=31,font="large_font",justify=RIGHT)
        self.entry.grid(row=0,column=1,padx=5,pady=5,ipady=7)

        self.l=[]
        for c in range(1, 19):
            x = Button(self.frame1, text=c, command=lambda j=c: self.num(j),width=6)
            if(c>=1 and c<=3):
                x.grid(row=1,column=c-1, padx=5, pady=5, ipadx=4, ipady=4)
            elif(c>=4 and c<=6):
                x.grid(row=2,column=c-4, padx=5, pady=5, ipadx=4, ipady=4)
            elif(c >= 7 and c <= 9):
                x.grid(row=3, column=c-7, padx=5, pady=5, ipadx=4, ipady=4)
            elif(c==11):
                x = Button(self.frame1, text=0, command=lambda j=0: self.num(j),width=6)
                x.grid(row=4, column=0, padx=5, pady=5, ipadx=4, ipady=4)
            elif (c == 12):
                x = Button(self.frame1, text='del', command=self.e_del,width=6)
                x.grid(row=4, column=1, padx=5, pady=5, ipadx=4, ipady=4)
            elif (c == 13):
                x = Button(self.frame1, text='C', command=self.clear,width=6)
                x.grid(row=4, column=2, padx=5, pady=5, ipadx=4, ipady=4)
            elif (c == 14):
                x = Button(self.frame1, text='+', command=lambda j='+':self.asmd(j),width=6)
                x.grid(row=1, column=3,columnspan=3, padx=5, pady=5, ipadx=4, ipady=4)
            elif (c == 15):
                x = Button(self.frame1, text='-', command=lambda j='-':self.asmd(j),width=6)
                x.grid(row=2, column=3, padx=5, pady=5, ipadx=4, ipady=4)
            elif (c == 16):
                x = Button(self.frame1, text='*', command=lambda j='*':self.asmd(j),width=6)
                x.grid(row=3, column=3,columnspan=3, padx=5, pady=5, ipadx=4, ipady=4)
            elif (c == 17):
                x = Button(self.frame1, text='/', command=lambda j='/':self.asmd(j),width=6)
                x.grid(row=4, column=3,columnspan=3, padx=5, pady=5, ipadx=4, ipady=4)
            elif (c == 18):
                x = Button(self.frame1, text='=', command=self.equal,width=26)
                x.grid(row=5, column=0,columnspan=6, padx=5, pady=5, ipadx=4, ipady=4)

            self.l.append(x)


        return
    def about_fun(self):
        return

    def num(self,c):
        print("num func")
        print("result= ",self.result)
        self.entry.insert(END,c)

        if(self.sign1==None):
            return
        else:
            self.work()

    def asmd(self,j):
        print("ammd func")
        if(self.sign==None and self.sign1==None):
            self.sign=j
            print(1)
            print("#1",self.var3.get())
            self.result = float(self.var3.get())
            self.entry.delete(0, END)
            #self.sign1=j
        else:
            print(2)
            self.sign1 = j
            self.work()
            self.entry.delete(0, END)


    def work(self):
        print("work func")
        if (self.sign == "+"):
            self.add()
        elif (self.sign == "-"):
            self.sub()
        elif (self.sign == "*"):
            self.mul()
        elif (self.sign == "/"):
            self.div()


    def add(self):
        print("add func ",self.var3.get())
        print("yo: ",self.var3.get())
        a=float(self.var3.get())
        self.result+=a
        self.entry.delete(0,END)
        #self.entry.insert(END, 5)
        print("result=",self.result)
        self.entry.insert(END,self.result)
        self.sign=self.sign1
        self.sign1=None
    def sub(self):
        print("sub func ",self.var3.get())
        print("yo sub: ",self.var3.get())
        a=float(self.var3.get())
        self.result-=a
        self.entry.delete(0,END)
        print("result=",self.result)
        self.entry.insert(END,self.result)
        self.sign=self.sign1
        self.sign1=None
    def mul(self):
        print("mul func")
        print("yo mul: ",self.var3.get())
        a=float(self.var3.get())
        self.result*=a
        self.entry.delete(0,END)
        print("result=",self.result)
        self.entry.insert(END,self.result)
        self.sign=self.sign1
        self.sign1=None
    def div(self):
        print("div func ",self.var3.get())
        print("yo div: ",self.var3.get())
        a=float(self.var3.get())
        self.result/=a
        self.entry.delete(0,END)
        print("result=",self.result)
        self.entry.insert(END,self.result)
        self.sign=self.sign1
        self.sign1=None
    def equal(self):
        self.work()
        self.sign = None
        self.sign1=None
        self.entry.delete(0, END)
        self.entry.insert(END,self.result)

    def e_del(self):
        self.entry.delete(len(self.var3.get())-1, END)
    def clear(self):
        self.result=0
        self.sign=None
        self.sign1=None
        self.entry.delete(0,END)

def main():
    root=Tk()
    root.geometry('300x330')
    root.wm_maxsize(300,330)
    root.wm_minsize(300,330)
    app=MyWindow(root)
    root.mainloop()

if __name__=='__main__':
    main()