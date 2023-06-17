from tkinter import*


root = Tk()
root.title("Project Python")
root.geometry("560x400-0+0")

frame1 = Frame(root)
frame2 = Frame(root,bg="white")
frame3 = Frame(root)
frame4 = LabelFrame(root,bg="white")

frame1.pack(pady=20)
frame2.pack()
frame3.pack(fill=BOTH)
frame4.pack(pady=20)

font = ("Arial",20)
font2 = ("Arial",15)


def option_insert(*args):
    
    frame4.pack_forget()
    frame2.forget()
    
    global frame5
    global b12
    
    frame5 = Frame(root)
    frame5.pack(pady=10)
    
    
    global b6
    global b8
    
    b6 = Button(frame5, text="With Index",font=font,borderwidth=3,bg="black",fg="white",relief=FLAT,activebackground="black",activeforeground="white")
    b6.grid(row=2,column=0,padx=3,pady=5)
    b6.bind("<Return>",In)
    b6.bind("<Button-1>",In)
    
    b8 = Button(frame5,text="With Value",font=font,borderwidth=3,bg="black",fg="white",relief=FLAT,activebackground="black",activeforeground="white")
    b8.grid(row=2,column=2,padx=3,pady=5)
    b8.bind("<Return>",add)
    b8.bind("<Button-1>",add)
    
    b11 = Button(frame5,text="Back",font=font,borderwidth=3,bg="black",fg="white",relief=FLAT,activebackground="black",activeforeground="white")
    b11.grid(row=3,columnspan=3,padx=3,pady=5)
    b11.bind("<Return>",back5)
    b11.bind("<Button-1>",back5)


# back buttons

def back9(*args):
    frame11.pack_forget()
    
    
    option_D()

def back8(*args):
    frame9.pack_forget()
    
    
    option_D()

def back7(*args):
    frame10.pack_forget()
    
    
    tab3()

def back6(*args):
    frame2.pack_forget()
    frame8.pack_forget()
    tab3()

def back5(*args):
    frame5.pack_forget()
    tab3()

def back4(*args):
    frame7.pack_forget()
    option_insert()

def back3(*args):
    frame6.pack_forget()
    option_insert()

def back2(*args):
    frame4.pack_forget()
    frame2.pack_forget()
    
    Add_button.pack_forget()
    Delete_button.pack_forget()
    Search_button.pack_forget()
    Back_button.pack_forget()
    frame2.pack_forget()
    tab2()

# back from tab2

def back1(*args):
    frame4.pack_forget()
    frame3.pack_forget()
    frame1.pack()
    

    tab1()






def button():
    frame1.pack_forget()
    
    global Add_button
    global Delete_button
    global Search_button
    global Back_button
       
    Add_button = Button(frame4, text="Insert",font=font,borderwidth=3,bg="black",fg="white",relief=FLAT,activebackground="black",activeforeground="white")
    Add_button.grid(row=1,column=0,padx=3,pady=5)
    Add_button.bind("<Return>",option_insert)
    Add_button.bind("<Button-1>",option_insert)
    
            
    Search_button = Button(frame4, text="Search",font=font,borderwidth=3,bg="black",fg="white",relief=FLAT,activebackground="black",activeforeground="white")
    Search_button.grid(row=1,column=2,padx=3,pady=5)
    Search_button.bind("<Return>",V_search)
    Search_button.bind("<Button-1>",V_search)
            
    Delete_button = Button(frame4, text="Delete",font=font,borderwidth=3,bg="black",fg="white",relief=FLAT,activebackground="black",activeforeground="white")
    Delete_button.grid(row=1,column=4,pady=5,padx=3)
    Delete_button.bind("<Return>",option_D)
    Delete_button.bind("<Button-1>",option_D)
    
    Back_button = Button(frame4, text="Back",font=font,borderwidth=3,bg="black",fg="white",relief=FLAT,activebackground="black",activeforeground="white")
    Back_button.grid(row=1,column=6,pady=5,padx=3)
    Back_button.bind("<Return>",back2)
    Back_button.bind("<Button-1>",back2)
    



def exit1(*args):
    root.quit()
    


def tab3(*args):
    
    global frame2
    global temp
    global elements_size
    global elements
    global ArrayI
    global ArrayN
    global Array_O
    global lb3
    
    frame2 = LabelFrame(root,bg="white",bd=5)
    
    
    
    Array_O=[]
    
    
    i = 0 
    temp = en1.get()
    elements_size = int(temp)
            
    elements = en2.get()
            
    ArrayI = [int(element) for element in elements.split()] 

    while i < elements_size:
        ArrayN = ArrayI[i]
        Array_O.append(ArrayN)
                 
        i = i + 1 


    frame3.pack_forget()
    
    lb3 = Label(frame2,text="",font=font)
    lb3.pack()
    
    lb3.config(text = Array_O)
    
    
    frame2.pack()
    frame4.pack()
    button()


def tab2(*args):
    frame3.pack()
    frame1.pack_forget()
    b1.pack_forget()
    b2.pack_forget()
    b3.pack_forget()
    
    
    global lb1
    global en1
    global en2
    global lb2
    global b4
    global b5

    
    lb1 = Label(frame3,text="No of elements:",font=font)
    lb1.grid(row=0,column=0,pady=10)
    
    en1 = Entry(frame3,width=5,bg="white",font = font,borderwidth=3)
    en1.grid(row=0,column=1)


    lb2 = Label(frame3,text="Enter elements:",font=font)
    lb2.grid(row=1,column=0,pady=10)
    
    en2 = Entry(frame3,bg="white",font = font,width=12,borderwidth=3)
    en2.grid(row=1,column=1)
    
    b4 = Button(frame3,text = "Create",font=font2,borderwidth=3,padx=50,bg="black",fg="white",relief=FLAT,activebackground="black",activeforeground="white")
    b4.grid(row=2,column=0,padx=3,pady=5)
    b4.bind("<Return>",tab3)
    b4.bind("<Button-1>",tab3)
    
    b5 = Button(frame3,text = "Back",font=font2,borderwidth=3,padx=50,bg="black",fg="white",relief=FLAT,activebackground="black",activeforeground="white")
    b5.grid(row=2,column=1,padx=3,pady=5)
    b5.bind("<Return>",back1)
    b5.bind("<Button-1>",back1)
    
    

    
    

def tab1(*args):
    
    global b1
    global b2
    global b3
    
    b1 = Button(frame1,text="Array",font=font,borderwidth=3,padx=50,bg="black",fg="white",relief=FLAT,activebackground="black",activeforeground="white")
    b1.grid(row=2,column=0,padx=3,pady=5)
    b1.bind("<Return>",tab2)
    b1.bind("<Button-1>",tab2)
    
    b2 = Button(frame1,text="Linked List",font=font,borderwidth=3,padx=16,bg="black",fg="white",relief=FLAT,activebackground="black",activeforeground="white")
    #b2.bind("<Return>",)
    #b2.bind("<Button-1>",)
    b2.grid(row=2,column=2,padx=3,pady=5)
    
    b3 = Button(frame1,text="Exit",font=font,borderwidth=3,padx=60,bg="black",fg="white",relief=FLAT,activebackground="black",activeforeground="white")
    b3.grid(row=3,columnspan=3,padx=3,pady=5)
    b3.bind("<Return>",exit1)
    b3.bind("<Button-1>",exit1)



def In(*args):
    frame4.pack_forget()
    frame5.pack_forget()
    frame2.pack()
    global frame7
    frame7 = Frame(root)
    frame7.pack()
    
    
    global lb5
    global lb6
    global en5
    global en6
    global b10
    global b11

    lb5 = Label(frame7,text="Enter Index No:",font=font)
    lb5.grid(row=0,column=0)
    
    en5 = Entry(frame7,font=font,bg="white",width=5,borderwidth=3)
    en5.grid(row=0,column=1)
    
    lb6 = Label(frame7,text="Enter Value:",font=font)
    lb6.grid(row=1,column=0,pady=10)
    
    en6 = Entry(frame7,font=font,bg="white",width=5,borderwidth=3)
    en6.grid(row=1,column=1)
    
    b10 = Button(frame7,text="Insert",font=font2,borderwidth=3,padx=50,bg="black",fg="white",relief=FLAT,activebackground="black",activeforeground="white")
    b10.grid(row=2,column=0,padx=3,pady=5)
    b10.bind("<Return>",out)
    b10.bind("<Button-1>",out)
    
    b11 = Button(frame7,text="Back",font=font2,borderwidth=3,padx=55,bg="black",fg="white",relief=FLAT,activebackground="black",activeforeground="white")
    b11.grid(row=2,column=1,padx=3,pady=5)
    b11.bind("<Return>",back4)
    b11.bind("<Button-1>",back4)
    

def out(*args):
    frame7.pack_forget()
    
    frame4.pack()
    global frame2
    frame2.destroy()
    frame2 = LabelFrame(root,bg="white")
    frame2.pack(pady=20)
    
    global lb7
    
    enI = en5.get()
    engI = int(enI)
    
    engV = en6.get()
    enAV = int(engV)
    
    Array_O.insert(engI,enAV)
    
    lb7 = Label(frame2,text="",font=font)
    lb7.pack()
    lb7.config(text=Array_O)
    
    button()
    
    


def show_V(*args):
    frame6.pack_forget()
    frame4.pack()
    
    global frame2
    
    frame2.destroy()
    frame2 = LabelFrame(root,bg="white")
    frame2.pack(pady=20)
    
    global lb4
    
    
    temp2 = en4.get()
    ArrayN = [int(element2) for element2 in temp2.split()]
    Array_O.extend(ArrayN)
    
    lb4 = Label(frame2,text="",font=font)
    lb4.pack()
    
    lb4.config(text=Array_O)
    
    button()

def option_D(*args):
    frame4.pack_forget()
    frame2.forget()
    
    global frame10
    global b15
    
    frame10 = Frame(root)
    frame10.pack(pady=10)
    
    
    global b16
    global b17
    
    b15 = Button(frame10,text="With Index",font=font,borderwidth=3,bg="black",fg="white",relief=FLAT,activebackground="black",activeforeground="white")
    b15.grid(row=1,column=0,padx=3,pady=5)
    b15.bind("<Return>",Delete_I)
    b15.bind("<Button-1>",Delete_I)
    
    b16 = Button(frame10,text="With Value",font=font,borderwidth=3,bg="black",fg="white",relief=FLAT,activebackground="black",activeforeground="white")
    b16.grid(row=1,column=2,padx=3,pady=5)
    b16.bind("<Return>",Delete_V)
    b16.bind("<Button-1>",Delete_V)
    
    b17 = Button(frame10,text="Back",font=font,bg="black",fg="white",relief=FLAT,borderwidth=3,padx=50,activebackground="black",activeforeground="white")
    b17.grid(row=2,columnspan=3,padx=3,pady=5)
    b17.bind("<Return>",back7)
    b17.bind("<Button-1>",back7)


def Delete_I(*args):
    frame10.pack_forget()
    frame2.pack()
    global frame11
    
    frame11 = Frame(root)
    frame11.pack(pady=20)
    
    global en10
    global lb9
    global b18
    global b19
    
    lb18 = Label(frame11,text="Enter Index No:",font=font)
    lb18.grid(row=0,column=0)
    
    en10 = Entry(frame11,width=5,font=font,bg="white",borderwidth=5)
    en10.grid(row=0,column=1)
    
    b18 = Button(frame11,text="Delete",font=font2,bg="black",fg="white",relief=FLAT,borderwidth=3,padx=50,activebackground="black",activeforeground="white")
    b18.grid(row=2,column=0,padx=3,pady=5)
    b18.bind("<Return>",Delete_IR)
    b18.bind("<Button-1>",Delete_IR)
    
    b19 = Button(frame11,text="Back",font=font2,bg="black",fg="white",relief=FLAT,borderwidth=3,padx=50,activebackground="black",activeforeground="white")
    b19.grid(row=2,column=1,padx=3,pady=5)
    b19.bind("<Return>",back9)
    b19.bind("<Button-1>",back9)    
    
def Delete_IR(*args):
    global frame2
    frame2.destroy
    frame2 = LabelFrame(root,bg="white")
    frame2.pack(pady=20)
    global lb9
    
    dI = en10.get()
    dO = int(dI)
    del Array_O[dO]   
    
    lb9 = Label(frame2,text="",font=font)
    lb9.pack()
    lb9.config(text=Array_O)
    
    frame11.pack_forget()
    frame4.pack()
    button()


def Delete_V(*args):
    frame10.pack_forget()
    frame2.pack()
    global frame9
    
    frame9 = Frame(root)
    frame9.pack(pady=20)
    
    global en9
    global lb8
    global b14
    global b15
    
    lb8 = Label(frame9,text="Enter Value:",font=font)
    lb8.grid(row=0,column=0)
    
    en9 = Entry(frame9,width=5,font=font,borderwidth=5,bg="white")
    en9.grid(row=0,column=1)
    
    b14 = Button(frame9,text="Delete",font=font2,bg="black",fg="white",relief=FLAT,borderwidth=3,padx=50,activebackground="black",activeforeground="white")
    b14.grid(row=2,column=0,padx=3,pady=5)
    b14.bind("<Return>",Delete_VR)
    b14.bind("<Button-1>",Delete_VR)
    
    b15 = Button(frame9,text="Back",font=font2,bg="black",fg="white",relief=FLAT,borderwidth=3,padx=50,activebackground="black",activeforeground="white")
    b15.grid(row=2,column=1,padx=3,pady=5)
    b15.bind("<Return>",back8)
    b15.bind("<Button-1>",back8)
    
def Delete_VR(*args):
    
    
    global frame2
    frame2.destroy()
    frame2 = Label(root,bg="white",borderwidth=3)
    frame2.pack(pady=20)
    
    global lb8
    
    enGT = en9.get()
    en_D = int(enGT)
    
    Array_O.remove(en_D)
    
    lb8 = Label(frame2,text = "",font=font)
    lb8.pack()
    lb8.config(text=Array_O)
    
    frame9.pack_forget()
    frame4.pack()
    button()
    


def add(*args):
    frame5.pack_forget()
    frame2.pack()
    global frame6
    
    frame6 = Frame(root)
    frame6.pack(pady=10)
    
    global en3
    global en4
    global b7
    global b9
    
    en3= Label(frame6,text="Enter Value:",font=font)
    en3.grid(row=0,column=0)
    
    en4 = Entry(frame6,width=5,font=font,borderwidth=5,bg="white")
    en4.grid(row=0,column=1)
    
    b7 = Button(frame6,text="Insert",font=font2,bg="black",fg="white",relief=FLAT,borderwidth=3,padx=50,activebackground="black",activeforeground="white")
    b7.grid(row=2,column=0,padx=3,pady=5)
    b7.bind("<Return>",show_V)
    b7.bind("<Button-1>",show_V)
    
    b9 = Button(frame6,text="Back",font=font2,bg="black",fg="white",relief=FLAT,borderwidth=3,padx=50,activebackground="black",activeforeground="white")
    b9.grid(row=2,column=1,padx=3,pady=5)
    b9.bind("<Return>",back3)
    b9.bind("<Button-1>",back3)
    
    

def V_search(*args):
    frame4.pack_forget()
    frame2.pack()
    
    global frame8
    frame8 = Frame(root)
    frame8.pack()
    
    global en7
    global en8
    global b12
    global b13
    
    
    en7= Label(frame8,text="Enter Value:",font=font)
    en7.grid(row=0,column=0)
    
    en8 = Entry(frame8,width=5,font=font,borderwidth=5,bg="white")
    en8.grid(row=0,column=1)
    
    b12 = Button(frame8,text="Search",font=font2,bg="black",fg="white",relief=FLAT,borderwidth=3,padx=50,activebackground="black",activeforeground="white")
    b12.grid(row=2,column=0,padx=3,pady=5)
    b12.bind("<Return>",V_search_result)
    b12.bind("<Button-1>",V_search_result)
    
    b13 = Button(frame8,text="Back",font=font2,bg="black",fg="white",relief=FLAT,borderwidth=3,padx=50,activebackground="black",activeforeground="white")
    b13.grid(row=2,column=1,padx=3,pady=5)
    b13.bind("<Return>",back6)
    b13.bind("<Button-1>",back6)
    
    
def V_search_result(*args):
    frame8.pack_forget()
    
    global frame2
    frame2.destroy()
    frame2 = LabelFrame(root,bg="white")
    frame2.pack(pady=20)
    
    global eng
    global enI
    global pos
    global pos1
    eng = en8.get()
    enI = int(eng)
    

    
    if enI in Array_O:
        pos = Array_O.index(enI)
        pos1 = pos+1
        
        lb8 =  Label(frame2,text=str(enI)+" Found On Position "+str(pos1),font=font)
        lb8.pack()
        
    else:
        

        lb9 = Label(frame2,text=str(enI)+" Not Found",font=font)
        lb9.pack()
    
    
    frame4.pack()
    button()
    


tab1()
root.mainloop()
