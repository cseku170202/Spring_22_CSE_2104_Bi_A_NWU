from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
import os

root = Tk()
image = PhotoImage(file="imeag//logo.png")
hight = 430
width = 530
x = (root.winfo_screenwidth()//2)-(width//2)
y = (root.winfo_screenheight()//2)-(hight//2)
root.geometry('{}x{}+{}+{}'.format(width, hight, x, y))
# root.overrideredirect(True)
root.config(background="#CCCCFF")
wlc_lable = Label(text='Data structure basic', bg='#CCCCFF',
                  fg='#1A044D', font=('Trebuchet Ms', 15, 'bold'))
wlc_lable.place(x=150, y=25)

bg_lable = Label(root, image=image, bg='#CCCCFF')
bg_lable.place(x=190, y=65)

program_la = Label(root, text='Loading>>....', font=(
    'Trebuchet Ms', 15, 'bold'), fg='#1A044D', bg='#CCCCFF')
program_la.place(x=190, y=230)

progress = ttk.Style()
progress.theme_use('clam')
progress.configure("red.Horizontal.TProgressbar", background="#108cff")

progress = Progressbar(root, orient=HORIZONTAL, length=400,
                       mode='determinate', style="red.Horizontal.TProgressbar")
progress.place(x=60, y=270)


def top():
    root.withdraw()
    os.system("python Landingpage.py")
    root.destroy()


i = 0


def load():
    global i
    if i <= 10:
        txt = ' loading.....'+(str(10*i)+'%')
        program_la.config(text=txt)
        program_la.after(600, load)
        progress['value'] = 10*i
        i += 1

    else:
        top()


load()


root.resizable(False, False)
root.mainloop()
