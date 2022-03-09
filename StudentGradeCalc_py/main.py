from tkinter import *
from tkinter import messagebox,ttk,font
import logger
d={}
m1={}
m2={}
m3={}
d=logger.d1
m1=logger.m11
m2=logger.m22
m3=logger.m33

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
def main():
    def admin():
        new=Tk()
        new.title("")
        new.maxsize(width=400,height=300)
        new.minsize(width=400,height=300)
        new.configure(bg='navajo white')
        
        Label(new,text="Select from the following",font=20,bg='navajo white').grid(row=0,column=0)
        Label(new,text=" ",bg='navajo white').grid(row=1,column=0)
        
        Label(new,text="Add students:",font=20,bg='navajo white').grid(row=21,column=0)
        Label(new,text=" ",bg='navajo white').grid(row=22,column=0)
        
        Label(new,text="Upload Result:",font=20,bg='navajo white').grid(row=56,column=0)
        Label(new,text=" ",bg='navajo white').grid(row=57,column=0)
        
        Label(new,text="Change Password:",font=20,bg='navajo white').grid(row=78,column=0)
        Label(new,text=" ",bg='navajo white').grid(row=79,column=0)
        
        Label(new,text="Search Students:",font=20,bg='navajo white').grid(row=102,column=0)
        Label(new,text=" ",bg='navajo white').grid(row=103,column=0)
        
        
        def addstudents():
            new.destroy()
            new1=Tk()
            new1.title("Add students")
            new1.maxsize(width=400,height=250)
            new1.minsize(width=400,height=250)
            new1.configure(bg='DarkOliveGreen1')

            Label(new1,text=" ",bg='DarkOliveGreen1').grid(row=0,column=0)
            
            Label(new1,text="Enter the name of the student",font=20,bg='DarkOliveGreen1').grid(row=1,column=0)
            Label(new1,text=" ",bg='DarkOliveGreen1').grid(row=2,column=0)

            
            Label(new1,text="Enter the SRN",font=20,bg='DarkOliveGreen1').grid(row=3,column=0)
            Label(new1,text=" ",bg='DarkOliveGreen1').grid(row=4,column=0)


            Label(new1,text="Enter the Section",font=20,bg='DarkOliveGreen1').grid(row=5,column=0)
            Label(new1,text=" ",bg='DarkOliveGreen1').grid(row=6,column=0)
            
            eb=Entry(new1,width=30)
            eb.grid(row=1,column=1)
            
            eb1=Entry(new1,width=30)
            eb1.grid(row=3,column=1)
            
            eb2=Entry(new1,width=30)
            eb2.grid(row=5,column=1)
            
            def enter():
                srn=eb1.get().upper()
                name=eb.get().upper()
                section=eb2.get().upper()
                c=0
                for i in range(1,len(d)):
                     if list(d.keys())[i][:8]==srn[:8] and list(d.values())[i][1]==section:
                            c+=1
                if name=='' or srn=='' or section=='':
                        messagebox.showwarning("Caution","No fields can remain empty")
                elif len(srn)!=13 or srn[:8] not in['PES1UG20','PES2UG20'] or srn[8:10] not in ['CS','EC','EE','BT','ME','CV']:
                     messagebox.showwarning("Caution","Invalid SRN")
                elif len(section)!=1 or not(65<=ord(section[0])<=97):
                    messagebox.showwarning("Caution","Invalid Section")
                elif name in list(d.values())[0] or srn in d.keys():
                     messagebox.showwarning("Caution","SRN/Name already exists")
                elif c>70:
                     messagebox.showwarning("Caution","Maximum strength of section",section,"reached")
                else:
                    d[srn]=[]
                    d[srn].append(name)
                    d[srn].append(section)
                    eb.delete(0,END)
                    eb1.delete(0,END)
                    eb2.delete(0,END)
                    messagebox.showinfo("message","Added")
                
            def destr():
                new1.destroy()
                admin()
            Button(new1,text="Add",command=enter,padx=10,bg="yellow2").grid(row=42,column=1)
            Button(new1,text="Back",command=destr,padx=10,bg="yellow2").grid(row=42,column=0)
            
        def upload():
            count=0
            new1=Toplevel()
            new1.title("UPLOAD")
            new1.configure(bg="LightBlue2")
            new1.minsize(width=500,height=75)
            Label(new1,text= " ",bg="LightBlue2").grid(row=0,column=0)
            Label(new1,text="Enter the SRN of the student:",font=('Calibri',20),bg="LightBlue2").grid(row=1,column=0)
            Label(new1,text= " ",bg="LightBlue2").grid(row=2,column=0)
            eb=Entry(new1,width=25)
            eb.grid(row=1,column=1)
            def profile(srn):
                nonlocal count
                count+=1
                if count==1:
                    new1.destroy()
                print(srn)
                print(list(d.keys()))
                if srn in d.keys():
                    root=Toplevel()
                    root.title("Student Profile")
                    root.minsize(width=600,height=100)
                    r=IntVar()
                    f=Frame(root)
                    f1=Frame(root)
                    f2=Frame(root)
                    f3=Frame(root)
                    f.pack()
                    f1.pack()
                    f2.pack()
                    f3.pack()
                    Label(f,text="Enter the SRN of the student:",font=('Calibri',20)).grid(row=0,column=0)
                    eb0=Entry(f,width=20)
                    eb0.insert(0,srn)
                    eb0.grid(row=0,column=1)
                    def destr():
                            s=eb0.get().upper()
                            root.destroy()
                            profile(s)    
                    Button(f,text="Search",command=destr,padx=10,bg="orange").grid(row=3,column=1)
                    Label(f,text=" ").grid(row=4,column=1)
                    Label(f1,text="   Select the assessment:-",fg="blue",font=('Calibri',20)).grid(row=0,column=0,columnspan=3)
                    
                    def isa1(n):
                        if n!=3:
                            nonlocal f3
                            f3.destroy()
                            f3=Frame(root)
                            f3.pack()
                        print("in isa1",n)
                        ma=0;mb=0;m={}
                        if n==1:
                            m=m1
                            ma=60
                            mb=45
                        elif n==2:
                            m=m2
                            ma=40
                            mb=45
                        else:
                            m=m3
                            ma=100
                            mb=100
                        Label(f2,text="Engineering Chemistry                                                   ",font=15).grid(row=0,column=0)
                        Label(f2,text="Python for Computational Problem Solving                      ",font=15).grid(row=1,column=0)
                        Label(f2,text="Engineering Mechanics-Statics                                       ",font=15).grid(row=2,column=0)
                        Label(f2,text="Engineering Mathematics-1                                            ",font=15).grid(row=3,column=0)
                        Label(f2,text="Electronic Principles and Devices                                   ",font=15).grid(row=4,column=0)
                        Label(f2,text="Constituitional law,Personal ethics,Cyber Crime              ",font=15).grid(row=5,column=0)
                        eb1=Entry(f2,width=10)
                        eb2=Entry(f2,width=10)
                        eb3=Entry(f2,width=10)
                        eb4=Entry(f2,width=10)
                        eb5=Entry(f2,width=10)
                        eb6=Entry(f2,width=10)
                        eb7=Entry(f3,width=10)
                        eb8=Entry(f3,width=10)
                        eb7.insert(0,"0")
                        eb8.insert(0,"0")
                        if n==3:
                            eb7.delete(0,END)
                            eb8.delete(0,END)
                            Label(f3,text="Engineering Chemistry Laboratory                                    ",font=15).grid(row=0,column=0)
                            Label(f3,text="Python Laboratory                                                   ",font=15).grid(row=1,column=0)
                            eb7.grid(row=0,column=1)
                            eb8.grid(row=1,column=1)
                            if srn in m.keys():
                                eb7.insert(0,m[srn][6])
                                eb8.insert(0,m[srn][7])
                            else:
                                eb7.delete(0,END)
                                eb8.delete(0,END)
                        eb1.grid(row=0,column=1)
                        eb2.grid(row=1,column=1)
                        eb3.grid(row=2,column=1)
                        eb4.grid(row=3,column=1)
                        eb5.grid(row=4,column=1)
                        eb6.grid(row=5,column=1)
                        if srn in m.keys():
                            eb1.insert(0,m[srn][0])
                            eb2.insert(0,m[srn][1])
                            eb3.insert(0,m[srn][2])
                            eb4.insert(0,m[srn][3])
                            eb5.insert(0,m[srn][4])
                            eb6.insert(0,m[srn][5])
                        def add():
                            if eb1.get()!='' and eb2.get()!='' and eb3.get()!='' and eb4.get()!='' and eb5.get()!='' and eb6.get()!='' and eb7.get()!='' and eb8.get()!='':
                                try:
                                    l=[int(eb1.get()),int(eb2.get()),int(eb3.get()),int(eb4.get()),int(eb5.get()),int(eb6.get()),int(eb7.get()),int(eb8.get())]
                                    l1=[int(eb1.get()),int(eb2.get()),int(eb3.get()),int(eb4.get()),int(eb5.get()),int(eb7.get()),int(eb8.get())]
                                    if max(l1)<=ma and int(eb6.get())<=mb:
                                        if min(l)>=0 and int(eb6.get())>=0:
                                            m[srn]=l
                                            messagebox.showinfo("message","Uploaded")
                                        else:
                                            print(l,eb6.get())
                                            messagebox.showwarning("message","Negative numbers not allowed")
                                    else:
                                        messagebox.showwarning("Alert","Maximum marks should be "+str(ma)+" ("+str(mb)+" for Constitution)")
                                except ValueError:
                                    messagebox.showerror("ERROR","MARKS MUST BE POSITIVE INTEGERS ONLY")
                            else:
                                messagebox.showwarning("Alert","No Fields can remain empty")
                        Button(f3,text="Add",command=add,padx=10,bg="sky blue").grid(row=168,column=1)
                    def check():
                        if r.get()==1:
                            isa1(1)
                        elif r.get()==2:
                            isa1(2)
                        elif r.get()==3:
                            isa1(3)
                    rb1=Radiobutton(f1,text="ISA-1",variable=r,value=1,command=check,bg="sky blue")
                    rb1.grid(row=1,column=0)
                    rb2=Radiobutton(f1,text="ISA-2",variable=r,value=2,command=check,bg="sky blue")
                    rb2.grid(row=1,column=1)
                    rb3=Radiobutton(f1,text="ESA",variable=r,value=3,command=check,bg="sky blue")
                    rb3.grid(row=1,column=2)
                    root.mainloop()
                else:
                    resp=messagebox.askyesno("","SRN Doesnot exist!\nDo you want to add the student")
                    if resp==1:
                        addstudents()
                    else:
                        upload()
            
            Button(new1,text="Upload",command=lambda : profile(eb.get().upper()),padx=10,bg="tan1").grid(row=3,column=0,columnspan=2)
            Label(new1,text=" ",bg='LightBlue2').grid(row=4,column=1)
            new1.mainloop()
            
        def changepassword():
            new1=Toplevel()
            new1.maxsize(width=350,height=150)
            new1.minsize(width=350,height=150)
            new1.configure(bg='gold')
            Label(new1,text= " ",bg='gold').grid(row=0,column=0)
            Label(new1,text= " ",bg='gold').grid(row=0,column=1)
            Label(new1,text="New Password   :",font=20,bg='gold').grid(row=1,column=0)
            Label(new1,text= " ",bg='gold').grid(row=2,column=0)
            Label(new1,text="Confirm Password:",font=20,bg='gold').grid(row=21,column=0)
            eb1=Entry(new1,width=20,show='*')
            eb2=Entry(new1,width=20,show='*')
            eb1.grid(row=1,column=1)
            eb2.grid(row=21,column=1)
            Label(new1,text= " ",bg='gold').grid(row=22,column=0)
            def enter():
                if eb1.get()==eb2.get():
                    messagebox.showinfo("Message","Password Change Succesful")
                    d["Administrator"]=eb1.get()
                    new1.destroy()
                else:
                    messagebox.showwarning("Message","Passwords donot match")
                    eb2.delete(0,END)
            Button(new1,text="Change",command=enter,padx=10,bg='khaki').grid(row=42,column=1)
            Label(new1,text= " ",bg='gold').grid(row=42,column=0)
        def back():
            response=messagebox.askyesno("Confirmation","Do you want to logout")
            if response==1:
                new.destroy()
                main()
        def search():
            newb=Toplevel()
            newb.minsize(width=250,height=100)
            newb.title("Search Students")
            newb.configure(bg='orange red')
            f=Frame(newb)
            f.pack(fill="both",expand='yes')
            f.configure(bg='coral1')
            eb=Entry(f,width=39)
            Label(f,text=" ",bg='coral1').grid(row=0,column=0)
            Label(f,text="Enter the name/srn of the student:",font=20,bg='coral1').grid(row=1,column=0)
            Label(f,text=" ",bg='coral1').grid(row=2,column=0)
            eb.grid(row=1,column=1)
            def enter():
                sd={}
                l1=list(d.keys())
                l2=list(d.values())
                ref=(eb.get()).upper()
                for i in range(1,len(d)):
                    if ref in l1[i]:
                        sd[l1[i]]=d[l1[i]][0]
                    elif ref in l2[i][0]:
                        sd[l1[i]]=l2[i][0]

                if sd:
                        newb.destroy()
                        new=Tk()
                        new.title("Search Results")
                        new.geometry("425x300")
                        new.resizable(False,False)
                        new.configure(bg='coral1')
                        f1=Frame(new)
                        #f1.configure(bg='corall')
                        mycanvas=Canvas(f1)
                        mycanvas.pack(side=LEFT,fill="both")
                        yscroll=ttk.Scrollbar(f1,orient="vertical",command=mycanvas.yview)
                        yscroll.pack(side=RIGHT,fill="y")
                        mycanvas.configure(yscrollcommand=yscroll.set)
                        mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox('all')))
                        xscroll=ttk.Scrollbar(f1,orient="horizontal",command=mycanvas.xview)
                        xscroll.pack(side=BOTTOM,fill="x")
                        mycanvas.configure(xscrollcommand=xscroll.set,bg='coral1')
                        mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox('all')))
                        f2=Frame(mycanvas)
                        f2.configure(bg='coral1')
                        mycanvas.create_window((0,0),window=f2,anchor='nw')
                        f1.pack(fill='both')
                        Label(f2,text="Sl.no.",font=20,bg='coral1').grid(row=3,column=0)
                        Label(f2,text=":",font=20,bg='coral1').grid(row=3,column=1)
                        Label(f2,text="Name",font=20,bg='coral1').grid(row=3,column=2)
                        Label(f2,text=":",font=20,bg='coral1').grid(row=3,column=3)
                        Label(f2,text="SRN",font=20,bg='coral1').grid(row=3,column=4)
                        i=0
                        n=4
                        while i<len(sd):
                            Label(f2,text=str(i+1),font=20,bg='coral1').grid(row=n,column=0)
                            Label(f2,text=":",font=20,bg='coral1').grid(row=n,column=1)
                            Label(f2,text=(list(sd.values()))[i],font=10,bg='coral1').grid(row=n,column=2)
                            Label(f2,text=":",font=10,bg='coral1').grid(row=n,column=3)
                            Label(f2,text=(list(sd.keys()))[i],font=10,bg='coral1').grid(row=n,column=4)
                            n=n+1
                            i=i+1
                        def destr():
                            new.destroy()
                            search()
                        Button(new,text="Back",command=destr,bg='sky blue',padx=10).pack()
                else:
                    messagebox.showinfo("message","No results found")

                    
            Button(f,text="Search",command=enter,padx=10,bg="gold").grid(row=3,column=0)            
        Button(new,text="Select",command=addstudents,padx=30,bg="DarkOliveGreen1").grid(row=21,column=1)
        Label(new,text=" ",bg='navajo white').grid(row=22,column=0)

        Button(new,text="Select",command=upload,padx=30,bg="LightBlue2").grid(row=56,column=1)
        Label(new,text=" ",bg='navajo white').grid(row=57,column=0)

        Button(new,text="Select",command=changepassword,padx=30,bg="gold").grid(row=78,column=1)
        Label(new,text=" ",bg='navajo white').grid(row=79,column=0)

        Button(new,text="Select",command=search,padx=30,bg='coral1').grid(row=102,column=1)
        Label(new,text=" ",bg='navajo white').grid(row=103,column=0)
        
        Button(new,text="Logout",command=back,padx=10,bg="snow").grid(row=118,column=0)

    #---------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
    def adminlogin():
        new=Toplevel()
        new.title("Admin Login")
        new.configure(bg='lemon chiffon')
        new.maxsize(width=500,height=200)
        new.minsize(width=500,height=200)

        Label(new,text="  ",font=13,bg='lemon chiffon').grid(row=0,column=0)

        Label(new,text=format("Enter Password",'<30'),font=20,fg="Black",bg='lemon chiffon').grid(row=10,column=1)
        Label(new,text="  ",font=13,bg='lemon chiffon').grid(row=25,column=0)

        Label(new,text="  Password:  ",font=13,bg='lemon chiffon').grid(row=31,column=0)
        eb=Entry(new,width=25,show='*',bg='snow',fg='black')
        eb.grid(row=31,column=1)
        def click():
            password=d["Administrator"]
            passw=eb.get()
            if passw==password:
                    new.destroy()
                    root.destroy()
                    admin()
            else:
                messagebox.showerror("Caution","Incorrect Password")
                eb.delete(0,END)
        Label(new,text="  ",font=13,bg='lemon chiffon').grid(row=80,column=0)
        Button(new,text="Login",command=click,padx=30,pady=5,bg="azure2").grid(row=100,column=1)
        root.mainloop()

    #---------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def calculator(n,srn):
        m={}
        gr={}
        if n==1:
            m[srn]=list(m3[srn])
            l1=[]
            for i in range(len(m3[srn])):
                if m[srn][i]>90:
                    l1.append('S')
                elif m[srn][i] in range(80,90):
                    l1.append('A')
                elif m[srn][i] in range(70,80):
                    l1.append('B')
                elif m[srn][i] in range(60,70):
                    l1.append('C')
                elif m[srn][i] in range(50,60):
                    l1.append('D')
                elif m[srn][i] in range(40,50):
                    l1.append('E')
                else:
                    l1.append('F')
            gr[srn]=l1
            s=0
            for i in m[srn]:
               s+=i
            m[srn].append(s)
            return m,gr
        elif n==2:
            l=[]
            for i in range(len(m3[srn])):
                if i==len(m3[srn])-3:
                    l.append(m3[srn][i]*0.7+m1[srn][i]/1.5)
                elif i==len(m3[srn])-2 or i==len(m3[srn])-1:
                    l.append(float(m3[srn][i]))
                else:
                    l.append(m3[srn][i]*0.7+m1[srn][i]*0.5)
            m[srn]=l
            l1=[]
            for i in range(len(m3[srn])):
                if m[srn][i]>90:
                    l1.append('S')
                elif m[srn][i] in range(80,90):
                    l1.append('A')
                elif m[srn][i] in range(70,80):
                    l1.append('B')
                elif m[srn][i] in range(60,70):
                    l1.append('C')
                elif m[srn][i] in range(50,60):
                    l1.append('D')
                elif m[srn][i] in range(40,50):
                    l1.append('E')
                else:
                    l1.append('F')
            gr[srn]=l1
            s=0
            for i in m[srn]:
               s+=i
            m[srn].append(s)
            print(m)
            return m,gr
        else:
            l=[]
            for i in range(len(m3[srn])):
                if i==len(m3[srn])-3:
                    l.append(m3[srn][i]*0.5+m1[srn][i]/1.8+m2[srn][i]/1.8)
                elif i==len(m3[srn])-2 or i==len(m3[srn])-1:
                    l.append(m3[srn][i])
                else:
                    l.append(m3[srn][i]*0.5+m1[srn][i]*0.5+m2[srn][i]*0.5)
            m[srn]=l
            l1=[]
            for i in range(len(m3[srn])):
                if m[srn][i]>90:
                    l1.append('S')
                elif m[srn][i] in range(80,90):
                    l1.append('A')
                elif m[srn][i] in range(70,80):
                    l1.append('B')
                elif m[srn][i] in range(60,70):
                    l1.append('C')
                elif m[srn][i] in range(50,60):
                    l1.append('D')
                elif m[srn][i] in range(40,50):
                    l1.append('E')
                else:
                    l1.append('F')
            gr[srn]=l1
            s=0
            for i in m[srn]:
               s+=i
            m[srn].append(s)
            return m,gr
        
    #---------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def student():
        new=Tk()
        new.title("Result Portal")
        new.maxsize(width=500,height=300)
        new.minsize(width=500,height=300)
        new.configure(bg='snow')

        Label(new,text="  ",font=26,bg='snow').grid(row=0,column=1)
        
        Label(new,text="Student Result Portal",font=40,bg='snow').grid(row=1,column=2)
        Label(new,text=" ",font=26,bg='snow').grid(row=2,column=0)
        
        Label(new,text="Enter your name:",font=11,bg='snow').grid(row=27,column=1)
        
        eb1=Entry(new,width=30,bg='light cyan')
        eb1.grid(row=27,column=2)

        Label(new,text=" ",font=26,bg='snow').grid(row=30,column=1)
        

        
        Label(new,text="Enter your SRN:",font=11,bg='snow').grid(row=39,column=1)
        eb2=Entry(new,width=30,bg='thistle')
        eb2.grid(row=39,column=2)
        
        def printer(m,gr,srn):
            new=Tk()
            new.title("Score Card")
            new.configure(bg='snow')
            f=Frame(new)
            f.grid(row=0,column=0)
            f.configure(bg='snow')
            f1=Frame(new)
            f1.grid(row=1,column=0)
            f1.configure(bg='snow')
            Label(f,text="Name : "+d[srn][0],font=20,bg='snow').grid(row=0,column=0)
            Label(f,text="SRN : "+srn,font=20,bg='snow').grid(row=1,column=0)
            Label(f1,text=" ",bg='snow').grid(row=0,column=0)
            Label(f1,text="Subject",font=15,bg='snow').grid(row=1,column=0)
            Label(f1,text="Marks",font=15,bg='snow').grid(row=1,column=1)
            Label(f1,text="Grade",font=15,bg='snow').grid(row=1,column=2)
            
            Label(f1,text="               Engineering  Chemistry                                                    ",font=("Courier", 15),bg='thistle').grid(row=2,column=0)
            Label(f1,text="               Python for Computational Problem Solving                                  ",font=("Courier", 15),bg='light cyan').grid(row=3,column=0)
            Label(f1,text="            Engineering Mechanics-Statics                                               ",font=("Courier", 15),bg='thistle').grid(row=4,column=0)
            Label(f1,text="              Engineering  Mathematics- 1                                               ",font=("Courier", 15),bg='light cyan').grid(row=5,column=0)
            Label(f1,text="               Electronic Principles and  Devices                                       ",font=("Courier", 15),bg='thistle').grid(row=6,column=0)
            Label(f1,text="            Constituitional law,Personal ethics,Cyber Crime                               ",font=("Courier", 15),bg='light cyan').grid(row=7,column=0)
            n=2
            i=0
            while n<=168 and i<=5:
                if n%2==0:
                    Label(f1,text=str(m[srn][i]),padx=11,font=("Courier", 15),bg='thistle').grid(row=n,column=1)
                    Label(f1,text=gr[srn][i],padx=11,font=("Courier", 15),bg='thistle').grid(row=n,column=2)
                else :
                    Label(f1,text=str(m[srn][i]),padx=11,font=("Courier", 15),bg='light cyan').grid(row=n,column=1)
                    Label(f1,text=gr[srn][i],padx=11,font=("Courier", 15),bg='light cyan').grid(row=n,column=2)
                n+=1
                i+=1

            Label(f1,text=" ",font=15,bg='snow').grid(row=8,column=0)
            Label(f1,text=" ",font=15,bg='snow').grid(row=9,column=0)
            def destr():
                new.destroy()
                menu(srn)
            f2=Frame(new)
            f2.configure(bg='snow')
            Label(f2,text="Total Score                                                ",font=15,bg='snow').grid(row=0,column=0)
            Label(f2,text=format(m[srn][8],'.2f'),font=15,bg='snow').grid(row=0,column=0)
            Label(f2,text=" ",font=15,bg='snow').grid(row=1,column=0)
            Button(f2,text="Back to Menu",command=destr,bg="orange").grid(row=2,column=0)
            f2.grid(row=2,column=0)
        def menu(srn):
            new=Tk()
            new.maxsize(width=150,height=100)
            new.minsize(width=150,height=100)
            new.title("Menu")
            new.configure(bg='azure')
            r=IntVar()
            def destr(r):
                new.destroy()
                if r==1:
                    m=calculator(1,srn)
                    printer(m[0],m[1],srn)
                elif r==2:
                    m13=calculator(2,srn)
                    printer(m13[0],m13[1],srn)
                elif r==3:
                    m123=calculator(3,srn)
                    printer(m123[0],m123[1],srn)
                else:
                    student()
            Radiobutton(new,text="ESA                            ",command=lambda:destr(r.get()),variable=r,value=1,bg="azure").grid(row=0,column=0)
            Radiobutton(new,text="ESA+ISA-1                ",command=lambda:destr(r.get()),variable=r,value=2,bg="azure").grid(row=1,column=0)
            Radiobutton(new,text="ESA+ISA-1+ISA-2     ",command=lambda:destr(r.get()),variable=r,value=3,bg="azure").grid(row=2,column=0)
            Radiobutton(new,text="Back to result portal",command=lambda:destr(r.get()),variable=r,value=4,bg="azure").grid(row=3,column=0)
        def validate():
            name=eb1.get().upper()
            srn=(eb2.get()).upper()
            if srn in d.keys():
                if d[srn][0]==name:
                    new.destroy()
                    menu(srn)
                else:
                   messagebox.showwarning("","Name and SRN donot match\nMake sure to enter the name as on your ID card") 
            else:
                messagebox.showwarning("","Invalid SRN")
        backbtn=PhotoImage(file='back.png')
        def destr():
            new.destroy()
            main()
        Button(new,image=backbtn,command=destr,bg='snow').grid(row=0,column=0)
        Label(new,text=" ",bg='snow').grid(row=69,column=0)
        Button(new,text="View Result",command=validate,font=8,bg='tan1',fg='white').grid(row=70,column=2)
        Label(new,text=" ",bg='snow').grid(row=71,column=0)
        Label(new,text="  ALL THE BEST!  ",font=20,bg='snow').grid(row=80,column=2)
        new.mainloop()


    '''def ex():
        root.destroy()'''
    #---------------------------------------------------------------------------------------------------------------------------------------------------------------------

    root=Tk()
    root.title("HOME PAGE")
    root.maxsize(width=1340,height=900)
    root.minsize(width=1340,height=900)


    img=PhotoImage(file="final.png")

    Label(root,image=img,height=0,width=0,border=0).place(x=0,y=0)
    myFont = font.Font(family='Helvetica')
    def destr():
        root.destroy()
        student()

    B2=Button(root,text="ADMIN LOGIN",command=adminlogin,bg='sienna1',width=30,height=1,font=("Courier", 20)).place(x=600,y=500)

    B1=Button(root,text="STUDENT LOGIN",command=destr,bg='sienna1',width=30,height=1,font=("Courier", 20)).place(x=600,y=350)

    #E=Button(root,text=" QUIT " ,command=ex,bg='PaleGreen1',width=10,height=1,font=("Times New Roman",8)).place(x=800,y=600)
     
    root.mainloop()
main()
print(d)
f=open("logger.py",'w')
print('d1=',d,'\nm11=',m1,'\nm22=',m2,'\nm33=',m3,file=f)
f.close()
    



