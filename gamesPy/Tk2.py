from tkinter import *
window = Tk()

photo = PhotoImage(file='simp.PNG')
#label = an area widget that holds text  and/or an image within a window
#there r 2 ways for doing it either pack() function or place function 
label1 = Label(window,text="Hello World" ,font=('Arial',40,'bold'), fg='green', bg='black',
              relief= RAISED, bd=9, padx=20, pady=20, image=photo, compound= 'bottom')       #font for text fashion__
                                                                                             #fg-foreground:vchanges text color__
                                                                                             # bg-background:for background color of window__
                                                                                             #relief for border style around text(RAISED, SUNKEN,FLAT,GROOVE,etc)__
                                                                                             #bd to set width of border__
                                                                                             #padx add space between text and border on x-axis__
                                                                                             #pady add space above and below our text between text and border on y-axis
label1.pack()
label2 = Label(window,text="Asma World")
label2.place(x=0, y=0)       #x & y decide place of what we have written here___x=0 & y=0 place lable at left corner 
label3 = Label(window,text="Asma Dead")
label3.place(x=100, y=100)   #x=100 & y=100 place lable somewhere in between / at center

window.mainloop() 