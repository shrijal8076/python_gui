root.maxsize(1200,800)
root.title("Password Genrator")
Heading = Label(root,text="Welcome to our App",font="comicsansms 25 bold",fg="white",bg="blue",width=60).grid(row=0,column=1)
#=========================================
def selection():
      selection=choice.get()
      
#===============================
Label(root,bg="orange",fg="white",width=15,padx=50,font=("arial",25,"bold"),text="Strength").place(x=300,y=200)

choice=IntVar()

l1=Radiobutton(root,bg="yellow",fg="red",activebackground="yellow",font=("arial",25,"bold"),text="POOR",variable=choice,value=1,command=selection)
l2=Radiobutton(root,bg="yellow",fg="red",activebackground="yellow",font=("arial",25,"bold"),text="AVERAGE",variable=choice,value=2,command=selection)
l3=Radiobutton(root,bg="yellow",fg="red",activebackground="yellow",font=("arial",25,"bold"),text="ADVANCED",variable=choice,value=3,command=selection)
l1.place(x=300,y=300)
l2.place(x=300,y=350)
l3.place(x=300,y=400)
labelchoice=Label(root)
labelchoice.place(x=300,y=450)


Label(root,bg="orange",fg="white",width=15,padx=50,font=("arial",25,"bold"),text="Length").place(x=300,y=500)


#========================
val =IntVar()
spinlength = Spinbox(root,from_=8,to_=24,textvariable=val,width=13,fg="red",font=("arial",25,"bold")).place(x=300,y=580)


def callback():
      Label(root,bg="blue",fg="white",width=55,padx=50,font=("arial",25,"bold"),text="Your genrated Password Is :-  " + passgen()).place(x=2,y=70)
      
      Label(root,bg="blue",fg="white",width=35,padx=50,font=("arial",25,"bold"),text="Thanks For Use Our App").place(x=300,y=720)
      
     

passwordgenButton=Button(root,text="Genrate password",bd=5 ,height=2,command=callback,pady=3)
passwordgenButton.place(x=300,y=650)
password=str(callback)


#logic

poor=string.ascii_uppercase+string.ascii_lowercase#to gentrate password by crypto....
average=string.ascii_uppercase+string.ascii_lowercase+string.digits
advanced=poor+average+string.punctuation


def  passgen():
      if choice.get() == 1:
            return "".join(random.sample(poor,val.get()))
      elif choice.get() == 2:
            return "".join(random.sample(average,val.get()))
      elif choice.get() == 3:
            return "".join(random.sample(advanced,val.get()))



root.mainloop()# to hold gui logic ,make intarctive
