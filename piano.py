from tkinter import*
import time
import pygame
pygame.init()
root=Tk()
Time=time.strftime('%H : %M : %S :%p')
root.title("MY OWN PIANO")
root.minsize(1800,1200)
root.maxsize(1800,1200)
root.configure(background="#0FE9A7")
"""def c(a):
      E1.delete(0,"end")
      E1.insert(0,a)
def click(a):
      E2.delete(0,"end")
      E2.insert(0,a)"""
#==========music==================
#==========light music===============
def B1():
      E1.delete(0,"end")
      E1.insert(0,"C#")
      sound=pygame.mixer.Sound("music/C_s.wav")
      sound.play()
      
def B2():
      E1.delete(0,"end")
      E1.insert(0,"C#")
      sound=pygame.mixer.Sound("music/D_s.wav")
      sound.play()
def B3():
      E1.delete(0,"end")
      E1.insert(0,"F#")
      sound=pygame.mixer.Sound("music/F_s.wav")
      sound.play()
def B4():
      E1.delete(0,"end")
      E1.insert(0,"G#")
      sound=pygame.mixer.Sound("music/G_s.wav")
      sound.play()
def B5():
      E1.delete(0,"end")
      E1.insert(0,"Bb")
      sound=pygame.mixer.Sound("music/Bb.wav")
      sound.play()
def B6():
      E1.delete(0,"end")
      E1.insert(0,"C#1")
      sound=pygame.mixer.Sound("music/C_s1.wav")
      sound.play()
def B7():
      E1.delete(0,"end")
      E1.insert(0,"D#1")
      sound=pygame.mixer.Sound("music/D_s1.wav")
      sound.play()
#===========loudmusic===================
def b1():
      E2.delete(0,"end")
      E2.insert(0,"C")
      sound=pygame.mixer.Sound("music/C.wav")
      sound.play()
def b2():
      E2.delete(0,"end")
      E2.insert(0,"D")
      sound=pygame.mixer.Sound("music/D.wav")
      sound.play()
def b3():
      E2.delete(0,"end")
      E2.insert(0,"E")
      sound=pygame.mixer.Sound("music/E.wav")
      sound.play()
def b4():
      E2.delete(0,"end")
      E2.insert(0,"F")
      sound=pygame.mixer.Sound("music/F.wav")
      sound.play()
def b5():
      E2.delete(0,"end")
      E2.insert(0,"G")
      sound=pygame.mixer.Sound("music/G.wav")
      sound.play()
def b6():
      E2.delete(0,"end")
      E2.insert(0,"A")
      sound=pygame.mixer.Sound("music/A.wav")
      sound.play()
def b7():
      E2.delete(0,"end")
      E2.insert(0,"B")
      sound=pygame.mixer.Sound("music/B.wav")
      sound.play()
def b8():
      E2.delete(0,"end")
      E2.insert(0,"C1")
      sound=pygame.mixer.Sound("music/C1.wav")
      sound.play()

def b9():
      E2.delete(0,"end")
      E2.insert(0,"D1")
      sound=pygame.mixer.Sound("music/D1.wav")
      sound.play()
def b10():
      E2.delete(0,"end")
      E2.insert(0,"E1")
      sound=pygame.mixer.Sound("music/E1.wav")
      sound.play()
def b11():
      E2.delete(0,"end")
      E2.insert(0,"F1")
      sound=pygame.mixer.Sound("music/F1.wav")
      sound.play()


def b2():
      E2.delete(0,"end")
      E2.insert(0,"D")
      sound=pygame.mixer.Sound("music/D.wav")
      sound.play()
def b2():
      E2.delete(0,"end")
      E2.insert(0,"D")
      sound=pygame.mixer.Sound("music/D.wav")
      sound.play()
      
                        
#=========================
l=Label(root,bg="black",text="MY PIYANO LET'S PLAY YO............",fg="white",font=("Time New Roman",35,"bold"))
l.pack(side=TOP,fill=X)
frame0=Frame(root,height=0,width=0)
frame0.place(x=230,y=65)
E=Entry(frame0,font=("Time New Roman",23,"bold"),fg="#0FE9A7",bg="white" ,width=25,bd=10)
E.grid(row=0,column=1)
E.insert(0,Time)
E1=Entry(frame0,font=("Time New Roman",23,"bold"),fg="#0FE9A7",bg="white" ,width=26,bd=10)
E1.grid(row=0,column=2)
E2=Entry(frame0,font=("Time New Roman",23,"bold"),fg="#0FE9A7",bg="white" ,width=25,bd=10)
E2.grid(row=0,column=3)
#==============================
frame1=Frame(root,height=0,width=0,bg="#0FE9A7")
frame1.place(x=530,y=150)
B1=Button(frame1,text="C#",font=("Time New Roman",30,"bold"),fg="white",bg="black" ,activebackground="green",activeforeground="red", height=6,width=3,bd=15,command=B1)

B1.grid(row=0,column=0,padx=5,pady=5)

B2=Button(frame1,text="D#",font=("Time New Roman",30,"bold"),fg="white",bg="black" ,activebackground="green",activeforeground="red",height=6,width=3,bd=15,command=B2)
B2.grid(row=0,column=2,padx=5,pady=5)
B3=Button(frame1,text="F#",font=("Time New Roman",30,"bold"),fg="white",bg="black" ,activebackground="green",activeforeground="red",height=6,width=3,bd=15,command=B3)
B3.grid(row=0,column=4,padx=5,pady=5)
B4=Button(frame1,text="G#",font=("Time New Roman",30,"bold"),fg="white",bg="black" ,activebackground="green",activeforeground="red",height=6,width=3,bd=15,command=B4)
B4.grid(row=0,column=5,padx=5,pady=5)
B5=Button(frame1,text="Bb",font=("Time New Roman",30,"bold"),fg="white",bg="black" ,activebackground="green",activeforeground="red",height=6,width=3,bd=15,command=B5)
B5.grid(row=0,column=6,padx=5,pady=5)
B6=Button(frame1,text="C#1",font=("Time New Roman",30,"bold"),fg="white",bg="black" ,activebackground="green",activeforeground="red",height=6,width=3,bd=15,command=B6)
B6.grid(row=0,column=8,padx=5,pady=5)
B7=Button(frame1,text="D#1",font=("Time New Roman",30,"bold"),fg="white",bg="black" ,activebackground="green",activeforeground="red",height=6,width=3,bd=15,command=B7)
B7.grid(row=0,column=9,padx=5,pady=5)

#========================================
frame2=Frame(root,height=0,width=0,bg="#0FE9A7")
frame2.place(x=70,y=500)
b1=Button(frame2,text="C",font=("Time New Roman",35,"bold"),fg="#0FE9A7",bg="white" ,activebackground="black",activeforeground="white",height=7,width=2,bd=15,padx=25,pady=30,command=b1)
b1.grid(row=1,column=0,padx=5)
b2=Button(frame2,text="D",font=("Time New Roman",35,"bold"),fg="#0FE9A7",bg="white" ,activebackground="black",activeforeground="white",height=7,width=2,bd=15,padx=25,pady=30,command=b2)
b2.grid(row=1,column=1,padx=5)
b3=Button(frame2,text="E",font=("Time New Roman",35,"bold"),fg="#0FE9A7",bg="white" ,activebackground="black",activeforeground="white",height=7,width=2,bd=15,padx=25,pady=30,command=b3)
b3.grid(row=1,column=2,padx=5)
b4=Button(frame2,text="F",font=("Time New Roman",35,"bold"),fg="#0FE9A7",bg="white" ,activebackground="black",activeforeground="white",height=7,width=2,bd=15,padx=25,pady=30,command=b4)
b4.grid(row=1,column=3,padx=5)
b5=Button(frame2,text="G",font=("Time New Roman",35,"bold"),fg="#0FE9A7",bg="white" ,activebackground="black",activeforeground="white",height=7,width=2,bd=15,padx=25,pady=30,command=b5)
b5.grid(row=1,column=4,padx=5)
b6=Button(frame2,text="A",font=("Time New Roman",35,"bold"),fg="#0FE9A7",bg="white" ,activebackground="black",activeforeground="white",height=7,width=2,bd=15,padx=25,pady=30,command=b6)
b6.grid(row=1,column=5,padx=5)
b7=Button(frame2,text="B",font=("Time New Roman",35,"bold"),fg="#0FE9A7",bg="white" ,activebackground="black",activeforeground="white",height=7,width=2,bd=15,padx=25,pady=30,command=b7)
b7.grid(row=1,column=6,padx=5)
b8=Button(frame2,text="C1",font=("Time New Roman",35,"bold"),fg="#0FE9A7",bg="white" ,activebackground="black",activeforeground="white",height=7,width=2,bd=15,padx=25,pady=30,command=b8)
b8.grid(row=1,column=7,padx=5)
b9=Button(frame2,text="D1",font=("Time New Roman",35,"bold"),fg="#0FE9A7",bg="white" ,activebackground="black",activeforeground="white",height=7,width=2,bd=15,padx=25,pady=30,command=b9)
b9.grid(row=1,column=8,padx=5)
b10=Button(frame2,text="E1",font=("Time New Roman",35,"bold"),fg="#0FE9A7",bg="white" ,activebackground="black",activeforeground="white",height=7,width=2,bd=15,padx=25,pady=30,command=b10)
b10.grid(row=1,column=9,padx=5)
b11=Button(frame2,text="F1",font=("Time New Roman",35,"bold"),fg="#0FE9A7",bg="white" ,activebackground="black",activeforeground="white",height=7,width=2,bd=15,padx=25,pady=30,command=b11)
b11.grid(row=1,column=10,padx=5)
root.mainloop()
