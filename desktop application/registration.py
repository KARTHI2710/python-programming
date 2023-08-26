#desktop application

import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
con=sqlite3.connect("patientdatabase.db")
# Create the "patient" table if it doesn't exist
create_table_query = '''
    CREATE TABLE IF NOT EXISTS patient1 (
        uid text,
        title TEXT,
        patientname TEXT,
        gender TEXT,
        email TEXT,
        phone TEXT,
        address TEXT,
        doctorname TEXT,
        treatment TEXT
    )
'''
con.execute(create_table_query)

qry="select count(*) from patient1"
result=con.execute(qry)
c=0
for row in result:
    c=row[0]
uuid='p'+f"{c+1:05}"
#print(uuid)
def insert():
    qry="insert into patient1 (uid,title,patientname,gender,email,phone,address,doctorname,treatment) values(?,?,?,?,?,?,?,?,?)"
   # print(uid)
   # print(pn)
    #print(gen)
    #print(email)
   # print(ph)
    #print(add)
    #print(title)
    con.execute(qry,(uid,title,pn,gen,email,ph,add,docname,treat))
    con.commit()
    print("patient details added")

def page3():
        root1.destroy()
        root2=tkinter.Tk()
        root2.geometry("500x500")
        l1=Label(root2,text="UID : "+uid,font=("times",11,"bold")).pack(padx=5,pady=5)
        l2=Label(root2,text="Patient name : "+pn,font=("times",11,"bold")).pack(padx=5,pady=5)
        l3=Label(root2,text="Gender : "+gen,font=("times",11,"bold")).pack(padx=5,pady=5)
        l4=Label(root2,text="Email : "+email,font=("times",11,"bold")).pack(padx=5,pady=5)
        l5=Label(root2,text="Phone no : "+ph,font=("times",11,"bold")).pack(padx=5,pady=5)
        l6=Label(root2,text="Address : "+add,font=("times",11,"bold")).pack(padx=5,pady=5)
        l7=Label(root2,text="Title : "+title,font=("times",11,"bold")).pack(padx=5,pady=5)
        l8=Label(root2,text="Doctor Name : "+docname,font=("times",11,"bold")).pack(padx=5,pady=5)
        l9=Label(root2,text="Treatment : "+treat,font=("times",11,"bold")).pack(padx=5,pady=5)
        insert()
        root1.mainloop()

def page2():
#def page2(uid,pn,gen,email,ph,add,title):
    def submit():
        if(docnametxt.get() != '' and treatmenttext.get() != ''):
            global docname,treat
            docname=docnametxt.get()
            treat=treatmenttext.get()
            page3()
        else:
            messagebox.showinfo("Message","please fill all the details")


        
    root.destroy()
   # print(uid)
    #print(pn)
    #print(gen)
    #print(email)
    #print(ph)
    #print(add)
    #print(title)
    global root1
    root1=tkinter.Tk()
    root1.geometry("500x500")
    l1=Label(root1,text="UID : "+uid,font=("times",11,"bold")).pack(padx=5,pady=5)
    l2=Label(root1,text="Patient name : "+pn,font=("times",11,"bold")).pack(padx=5,pady=5)
    l3=Label(root1,text="Gender : "+gen,font=("times",11,"bold")).pack(padx=5,pady=5)
    l4=Label(root1,text="Email : "+email,font=("times",11,"bold")).pack(padx=5,pady=5)
    l5=Label(root1,text="Phone no : "+ph,font=("times",11,"bold")).pack(padx=5,pady=5)
    l6=Label(root1,text="Address : "+add,font=("times",11,"bold")).pack(padx=5,pady=5)
    l7=Label(root1,text="Title : "+title,font=("times",11,"bold")).pack(padx=5,pady=5)
    docname=Label(root1,text="Doctor name : ",font=("times",11,"bold")).place(x=100,y=300)
    docnametxt=Entry(root1,font=("times",11,"bold"))
    docnametxt.place(x=200,y=300)
    treatment=Label(root1,text="Treatment : ",font=("times",11,"bold")).place(x=100,y=350)
    treatmenttext=Entry(root1,font=("times",11,"bold"))
    treatmenttext.place(x=200,y=350)
    btn2=Button(root1,text="save",width=10,font=("bold"),command=submit).place(x=350,y=400)
    root1.mainloop()


    
def save():
    if(uidtext.get() != ''  and pattext.get() != "" and gend.get() != ' ' and emailtext.get() != "" and titdrop.get() != "" and phnotext.get() != "" and len(addresstext.get("1.0",END)) > 1):
        
        #page2(uidtext.get(),pattext.get(),gen.get(),emailtext.get(),phnotext.get(),addresstext.get("1.0","end-1c"),titdrop.get())
        global uid,pn,gen,email,ph,add,title
        uid=uidtext.get()
        pn=pattext.get()
        gen=gend.get()
        email=emailtext.get()
        ph=phnotext.get()
        add=addresstext.get("1.0","end-1c")
        title=titdrop.get()
       
        page2()

       
    else:
        messagebox.showinfo("message","enter all the fields")
    
root=tkinter.Tk()
root.geometry("500x500")
root.title("registration form")
root.config(bg="pink")


    


title=Label(root,text="Registration form",font=("times",15,"bold"),bg="pink")
title.pack(padx=5,pady=5)

frame1=Frame(root,height="100",width="100",bg="red")
frame1.pack(fill=X)

uid=Label(frame1,text="UID : ",font=("times",11,"bold"),bg="pink").grid(row=0,column=0,padx=5,pady=5,sticky=E)
uidtext=Entry(frame1,font=("times",10,"bold"))
uidtext.insert(0,uuid)
uidtext.config(state='readonly')
uidtext.grid(row=0,column=1,padx=5,pady=5,columnspan=3)

tit=Label(frame1,text="Title : ",font=("times",12,"bold"),bg="pink").grid(row=1,column=0,padx=5,pady=5,sticky=E)
titdrop=ttk.Combobox(frame1,values=['Mr.','Mrs.'],state='readonly')
#titdrop['values']=('Mr.','Mrs.')
#titdrop.current()
titdrop.grid(row=1,column=1,padx=5,pady=5,columnspan=3)

patname=Label(frame1,text="Patient Name : ",font=("times",12,"bold"),bg="pink").grid(row=2,column=0,padx=5,pady=5,sticky=E)
pattext=Entry(frame1,font=("times",10,"bold"))
pattext.grid(row=2,column=1,padx=5,pady=5,columnspan=3)

gend=StringVar(value=' ')
gender=Label(frame1,text="Gender : ",font=("times",12,"bold"),bg="pink").grid(row=3,column=0,padx=5,pady=5,sticky=E)
gendermale=Radiobutton(frame1,text="Male",font=("times",12,"bold"),bg="pink",variable=gend,value="Male")
gendermale.grid(row=3,column=1,padx=5,pady=5)
genderfemale=Radiobutton(frame1,text="Female",font=("times",12,"bold"),bg="pink",variable=gend,value="Female")
genderfemale.grid(row=3,column=2,padx=5,pady=5)
genderother=Radiobutton(frame1,text="Others",font=("times",12,"bold"),bg="pink",variable=gend,value="Others")
genderother.grid(row=3,column=3,padx=5,pady=5)

email=Label(frame1,text="Email : ",font=("times",12,"bold"),bg="pink").grid(row=4,column=0,padx=5,pady=5,sticky=E)
emailtext=Entry(frame1,font=("times",10,"bold"))
emailtext.grid(row=4,column=1,padx=5,pady=5,columnspan=3)

phno=Label(frame1,text="Phone No : ",font=("times",12,"bold"),bg="pink").grid(row=5,column=0,padx=5,pady=5,sticky=E)
phnotext=Entry(frame1,font=("times",10,"bold"))
phnotext.grid(row=5,column=1,padx=5,pady=5,columnspan=3)


#yscrollbar=Scrollbar(frame1,orient=VERTICAL)
#xscrollbar=Scrollbar(frame1,orient=HORIZONTAL)
address=Label(frame1,text="Address : ",font=("times",12,"bold"),bg="pink").grid(row=6,column=0,padx=5,pady=5,sticky=E)
addresstext=Text(frame1,height="5",width='20')
addresstext.grid(row=6,column=1,padx=5,pady=5,columnspan=3)
#yscrollbar.grid(row=6,column=1,columnspan=3,sticky=E,fill=Y)

btn=Button(frame1,text="save",width=10,font=("bold"),command=save).grid(row=7,column=0,columnspan=4,padx=5,pady=5)
root.mainloop()
