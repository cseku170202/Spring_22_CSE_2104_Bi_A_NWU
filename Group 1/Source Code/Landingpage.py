from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
import os

windo = Tk()
windo.geometry('800x650+10+10')
# windo.config(bg="#FFFFFF")


wlc_lable = Label(text='INSTUCTOR',
                  fg='#1A044D', font=('Trebuchet Ms', 15, 'bold'))
wlc_lable.place(x=350, y=5)

image1 = Image.open("imeag/shymumsir.png").resize((96, 100))
a_image = ImageTk.PhotoImage(image1)
image_label = Label(windo, image=a_image)
image_label.place(x=350, y=40)

label1 = Label(
    windo, text="Md. Shymon Islam \n LECTURER \n Dept. of CSE \n North Western University,khulna")
label1.place(x=315, y=140)

wl_lable = Label(text='DEVELOPER',
                 fg='#1A044D', font=('Trebuchet Ms', 15, 'bold'))
wl_lable.place(x=50, y=215)


image2 = Image.open("imeag/shoyeb.jpg").resize((96, 100))
b_image = ImageTk.PhotoImage(image2)
image_labe2 = Label(windo, image=b_image)
image_labe2.place(x=30, y=245)
label1 = Label(
    windo, text="Sheikh Soyeb \n Student \n Dept. of CSE \n North Western University,\nkhulna \n ID:20221001010")
label1.place(x=10, y=345)


image3 = Image.open("imeag/rezwan.jpg").resize((96, 100))
c_image = ImageTk.PhotoImage(image3)
image_labe3 = Label(windo, image=c_image)
image_labe3.place(x=220, y=245)
label1 = Label(
    windo, text="Rezwan Hossen \n Student \n Dept. of CSE \n North Western University,\nkhulna \n ID:20221033010")
label1.place(x=200, y=345)


image4 = Image.open("imeag/jubaer.jpg").resize((96, 100))
d_image = ImageTk.PhotoImage(image4)
image_labe4 = Label(windo, image=d_image)
image_labe4.place(x=400, y=245)
label1 = Label(
    windo, text="S M Jubaer Hossain \n Stdunt \n Dept. of CSE \n North Western University,\nkhulna \n ID:20221002010")
label1.place(x=380, y=345)


image5 = Image.open("imeag/nafi.jpg").resize((96, 100))
e_image = ImageTk.PhotoImage(image5)
image_labe5 = Label(windo, image=e_image)
image_labe5.place(x=580, y=245)

label1 = Label(
    windo, text="Nafi Uz Zaman \n student \n Dept. of CSE \n North Western University,\nkhulna \n ID:20221006010")
label1.place(x=560, y=345)

lable = Label(text='CLICK AND OPEN OUR PROJECT :',
              fg='#1A044D', font=('Trebuchet Ms', 20, 'bold'))
lable.place(x=50, y=500)


def mainproj():
    os.system("python indexAndArray.py")


button1 = Button(windo, text="OPEN >> ", bg='#CCCCFF',
                 fg='#1A044D', font=('Trebuchet Ms', 20, 'bold'), width='10', command=mainproj)
button1.place(x=480, y=490)

windo.mainloop()
