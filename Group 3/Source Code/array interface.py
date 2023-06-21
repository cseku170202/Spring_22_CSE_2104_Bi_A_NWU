from tkinter import *

root = Tk()
root.title("Our first GUI project")
root.geometry("800x700-0+0")
frame1 = Frame(root, bg="black")
frame2 = Frame(root, bg="white")
frame3 = Frame(root)
frame4 = LabelFrame(root, bg="pink")

frame1.pack(pady=100)
frame2.pack()
frame4.pack(pady=100)

font = ("Arial Bold", 22)
font2 = ("Arial Bold", 22)


def option_insert(*args):
    frame4.pack_forget()
    frame2.forget()

    global frame5
    global b12

    frame5 = Frame(root)
    frame5.pack(pady=10)

    global b6
    global b8

    b6 = Button(frame5, text="index", font=font2, bg="grey", fg="white", relief=SUNKEN, borderwidth=9, padx=40,
                activebackground="aquamarine", activeforeground="white")
    b6.pack(pady=20)
    b6.bind("<Return>", In)
    b6.bind("<Button-1>", In)

    b8 = Button(frame5, text="value", font=font2, bg="white", fg="black", relief=SUNKEN, borderwidth=9, padx=50,
                activebackground="white", activeforeground="black")
    b8.pack(pady=10)
    b8.bind("<Return>", add)
    b8.bind("<Button-1>", add)

    b11 = Button(frame5, text="Back", font=font2, bg="white", fg="black", relief=SUNKEN, borderwidth=6, padx=50,
                 activebackground="white", activeforeground="black")
    b11.pack(pady=10)
    b11.bind("<Return>", back5)
    b11.bind("<Button-1>", back5)




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




def back1(*args):
    frame4.pack_forget()
    frame3.pack_forget()
    frame1.pack()

    lb1.destroy()
    en1.destroy()
    en2.destroy()
    lb2.destroy()
    b4.destroy()
    b5.destroy()
    tab1()


def button():
    frame1.pack_forget()

    global Add_button
    global Delete_button
    global Search_button
    global Back_button

    Add_button = Button(frame4, text="Insert value", font=font2, borderwidth=6, bg="white", fg="black", relief=SUNKEN,
                        activebackground="black", activeforeground="red")
    Add_button.grid(row=0, column=0, padx=5, pady=8)
    Add_button.bind("<Return>", option_insert)
    Add_button.bind("<Button-1>", option_insert)

    Search_button = Button(frame4, text="Search value", font=font2, borderwidth=6, bg="grey", fg="yellow", relief=SUNKEN,
                           activebackground="black", activeforeground="red")
    Search_button.grid(row=1, column=0, padx=3, pady=5)
    Search_button.bind("<Return>", V_search)
    Search_button.bind("<Button-1>", V_search)

    Delete_button = Button(frame4, text="Delete value", font=font2, borderwidth=6, bg="white", fg="red", relief=SUNKEN,
                           activebackground="black", activeforeground="red")
    Delete_button.grid(row=2, column=0, pady=5, padx=3)
    Delete_button.bind("<Return>", option_D)
    Delete_button.bind("<Button-1>", option_D)

    Back_button = Button(frame4, text="Back", font=font2, borderwidth=6, bg="white", fg="black", relief=SUNKEN,
                         activebackground="black", activeforeground="red")
    Back_button.grid(row=3, column=0, pady=5, padx=3)
    Back_button.bind("<Return>", back2)
    Back_button.bind("<Button-1>", back2)


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

    frame2 = LabelFrame(root, bg="beige", bd=5)

    Array_O = []

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

    lb3 = Label(frame2, text="", font=font)
    lb3.pack()

    lb3.config(text=Array_O)

    frame2.pack()
    frame4.pack()
    button()


def tab2(*args):
    frame3.pack()
    frame1.pack_forget()
    b1.pack_forget()
    #b2.pack_forget()
    b3.pack_forget()

    global lb1
    global en1
    global en2
    global lb2
    global b4
    global b5

    lb1 = Label(frame3, text="SiZe of ArRaY:", font=font)
    lb1.grid(row=1, column=0, columnspan=4, pady=10)

    en1 = Entry(frame3, width=4, bg="grey",fg="white", font=font, borderwidth=7)
    en1.grid(row=1, column=4, pady=2)

    lb2 = Label(frame3, text="EnTeR ThE NUmber of ArRaY:", font=font)
    lb2.grid(row=3, column=1, columnspan=3, pady=10)

    en2 = Entry(frame3, bg="gray",fg="white", font=font, borderwidth=6)
    en2.grid(row=3, column=4, columnspan=4, pady=10)

    b4 = Button(frame3, text="Create", font=font, borderwidth=6, bg="grey", fg="yellow", relief=SUNKEN,
                activebackground="pink", activeforeground="black")
    b4.grid(row=5, column=1, pady=60)
    b4.bind("<Return>", tab3)
    b4.bind("<Button-1>", tab3)

    b5 = Button(frame3, text="Back", font=font, borderwidth=6, bg="grey", fg="white", relief=SUNKEN,
                activebackground="black", activeforeground="red", padx=30)
    b5.grid(row=5, column=2, pady=15)
    b5.bind("<Return>", back1)
    b5.bind("<Button-1>", back1)


def tab1(*args):
    global b1
    global b2
    global b3

    b1 = Button(frame1, text="ShOw ArRaY", font=font2, bg="gray", fg="aquamarine", relief=SUNKEN, borderwidth=10, padx=50,
                activebackground="pink", activeforeground="black")
    b1.grid(row=0,column=0)
    b1.bind("<Return>", tab2)
    b1.bind("<Button-1>", tab2)


    b3 = Button(frame1, text="LiNk LiSt", font=font2, bg="gray", fg="pink", relief=SUNKEN, borderwidth=10, padx=50,
                activebackground="white", activeforeground="black")
    b3.grid(row=10,column=2)
    b3.bind("<Return>", exit1)
    b3.bind("<Button-1>", exit1)


def In(*args):
    frame4.pack_forget()
    frame5.pack_forget()

    global frame7
    frame7 = Frame(root)
    frame7.pack()

    global lb5
    global lb6
    global en4
    global en5
    global b10
    global b11

    lb5 = Label(frame7, text="Input Index No:", font=font2)
    lb5.grid(row=10, column=5)

    en4 = Entry(frame7, font=font2, bg="white", width=7, borderwidth=6)
    en4.grid(row=10, column=1)

    lb6 = Label(frame7, text="Input Value:", font=font2)
    lb6.grid(row=0, column=0, pady=20)

    en5 = Entry(frame7, font=font2, bg="white", width=7, borderwidth=6)
    en5.grid(row=1, column=1)

    b10 = Button(frame7, text="Update insert", font=font2, bg="white", fg="black", relief=SUNKEN, borderwidth=6, padx=50,
                 activebackground="white", activeforeground="black")
    b10.grid(row=10, column=20, columnspan=2, pady=5)
    b10.bind("<Return>", out)
    b10.bind("<Button-1>", out)

    b11 = Button(frame7, text="Back", font=font2, bg="grey", fg="baby blue", relief=SUNKEN, borderwidth=6, padx=50,
                 activebackground="blue", activeforeground="red")
    b11.grid(row=3, column=0, columnspan=2, pady=5)
    b11.bind("<Return>", back4)
    b11.bind("<Button-1>", back4)


def out(*args):
    frame7.pack_forget()

    frame4.pack()
    global frame2
    frame2.destroy()
    frame2 = LabelFrame(root, bg="white")
    frame2.pack(pady=20)

    global lb7

    enI = en4.get()
    engI = int(enI)

    engV = en5.get()
    enAV = int(engV)

    Array_O.insert(engI, enAV)

    lb7 = Label(frame2, text="", font=font)
    lb7.pack()
    lb7.config(text=Array_O)

    button()


def show_V(*args):
    frame6.pack_forget()
    frame4.pack()

    global frame2

    frame2.destroy()
    frame2 = LabelFrame(root, bg="red")
    frame2.pack(pady=20)

    global lb4

    temp2 = en3.get()
    ArrayN = [int(element2) for element2 in temp2.split()]
    Array_O.extend(ArrayN)

    lb4 = Label(frame2, text="", font=font)
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

    b15 = Button(frame10, text="Index", font=font2, bg="gray", fg="white", relief=SUNKEN, borderwidth=7, padx=50,
                 activebackground="white", activeforeground="black")
    b15.pack(pady=10)
    b15.bind("<Return>", Delete_I)
    b15.bind("<Button-1>", Delete_I)

    b16 = Button(frame10, text="value", font=font2, bg="white", fg="black", relief=SUNKEN, borderwidth=7, padx=50,
                 activebackground="white", activeforeground="black")
    b16.pack(pady=10)
    b16.bind("<Return>", Delete_V)
    b16.bind("<Button-1>", Delete_V)

    b17 = Button(frame10, text="Back", font=font2, bg="white", fg="black", relief=SUNKEN, borderwidth=6, padx=50,
                 activebackground="white", activeforeground="black")
    b17.pack(pady=10)
    b17.bind("<Return>", back7)
    b17.bind("<Button-1>", back7)


def Delete_I(*args):
    frame10.pack_forget()

    global frame11

    frame11 = Frame(root)
    frame11.pack(pady=20)

    global en8
    global lb9
    global b18
    global b19

    lb18 = Label(frame11, text="Input Index:", font=font2)
    lb18.grid(row=0, column=0)

    en8 = Entry(frame11, width=5, font=font2, bg="white", borderwidth=7)
    en8.grid(row=0, column=1)

    b18 = Button(frame11, text="Enter", font=font2, bg="grey", fg="yellow", relief=SUNKEN, borderwidth=6, padx=50,
                 activebackground="white", activeforeground="black")
    b18.grid(row=2, column=0, columnspan=7, pady=20)
    b18.bind("<Return>", Delete_IR)
    b18.bind("<Button-1>", Delete_IR)

    b19 = Button(frame11, text="Back", font=font2, bg="white", fg="black", relief=SUNKEN, borderwidth=6, padx=50,
                 activebackground="white", activeforeground="black")
    b19.grid(row=4, column=0, columnspan=7, pady=20)
    b19.bind("<Return>", back9)
    b19.bind("<Button-1>", back9)


def Delete_IR(*args):
    global frame2
    frame2.destroy
    frame2 = LabelFrame(root, bg="red")
    frame2.pack(pady=20)
    global lb9

    dI = en8.get()
    dO = int(dI)
    del Array_O[dO]

    lb9 = Label(frame2, text="", font=font2)
    lb9.pack()
    lb9.config(text=Array_O)

    frame11.pack_forget()
    frame4.pack()
    button()


def Delete_V(*args):
    frame10.pack_forget()
    global frame9

    frame9 = Frame(root)
    frame9.pack(pady=20)

    global en7
    global lb8
    global b14
    global b15

    lb8 = Label(frame9, text="Input Value:", font=font2)
    lb8.grid(row=0, column=0)

    en7 = Entry(frame9, width=5, font=font2, borderwidth=7, bg="white")
    en7.grid(row=0, column=1)

    b14 = Button(frame9, text="Enter", font=font2, bg="white", fg="black", relief=SUNKEN, borderwidth=6, padx=50,
                 activebackground="white", activeforeground="black")
    b14.grid(row=2, column=0, columnspan=5, pady=20)
    b14.bind("<Return>", Delete_VR)
    b14.bind("<Button-1>", Delete_VR)

    b15 = Button(frame9, text="Back", font=font2, bg="white", fg="black", relief=SUNKEN, borderwidth=6, padx=50,
                 activebackground="white", activeforeground="black")
    b15.grid(row=4, column=0, columnspan=4, pady=20)
    b15.bind("<Return>", back8)
    b15.bind("<Button-1>", back8)


def Delete_VR(*args):
    global frame2
    frame2.destroy()
    frame2 = Label(root, bg="red", borderwidth=3)
    frame2.pack(pady=20)

    global lb8

    enGT = en7.get()
    en_D = int(enGT)

    Array_O.remove(en_D)

    lb8 = Label(frame2, text="", font=font2)
    lb8.pack()
    lb8.config(text=Array_O)

    frame9.pack_forget()
    frame4.pack()
    button()


def add(*args):
    frame5.pack_forget()

    global frame6

    frame6 = Frame(root)
    frame6.pack(pady=10)

    global en3
    global b7
    global b9

    en3 = Entry(frame6, font=font2, bg="white", borderwidth=7)
    en3.pack()

    b7 = Button(frame6, text="Update", font=font2, bg="apricot", fg="black", relief=SUNKEN, borderwidth=6, padx=50,
                activebackground="black", activeforeground="red")
    b7.pack(pady=10)
    b7.bind("<Return>", show_V)
    b7.bind("<Button-1>", show_V)

    b9 = Button(frame6, text="Back", font=font2, bg="white", fg="black", relief=SUNKEN, borderwidth=6, padx=50,
                activebackground="white", activeforeground="black")
    b9.pack(pady=10)
    b9.bind("<Return>", back3)
    b9.bind("<Button-1>", back3)


def V_search(*args):
    frame4.pack_forget()
    frame2.pack_forget()

    global frame8
    frame8 = Frame(root)
    frame8.pack()

    global en6
    global b12
    global b13

    en6 = Entry(frame8, font=font2, bg="white", borderwidth=6)
    en6.pack(pady=20)

    b12 = Button(frame8, text="Search", font=font2, bg="grey", fg="blue", relief=SUNKEN, borderwidth=6, padx=70,
                 activebackground="white", activeforeground="black")
    b12.pack(pady=20)
    b12.bind("<Return>", V_search_result)
    b12.bind("<Button-1>", V_search_result)

    b13 = Button(frame8, text="Back", font=font2, bg="grey", fg="yellow", relief=SUNKEN, borderwidth=6, padx=70,
                 activebackground="white", activeforeground="black")
    b13.pack(pady=10)
    b13.bind("<Return>", back6)
    b13.bind("<Button-1>", back6)


def V_search_result(*args):
    frame8.pack_forget()

    global frame2
    frame2.destroy()
    frame2 = LabelFrame(root, bg="pink")
    frame2.pack(pady=20)

    global eng
    global enI
    global pos
    global pos1
    eng = en6.get()
    enI = int(eng)

    if enI in Array_O:
        pos = Array_O.index(enI)
        pos1 = pos + 1

        lb8 = Label(frame2, text=str(enI) + " Found On Position " + str(pos1), font=font)
        lb8.pack()

    else:

        lb9 = Label(frame2, text=str(enI) + " Not Found", font=font)
        lb9.pack()

    frame4.pack()
    button()


tab1()
root.mainloop()