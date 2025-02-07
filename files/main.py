__author__ = "Shrinivas"
import os
from tkinter import *
from tkinter import messagebox

main = Tk()
main.geometry("1366x768")
main.title("Sales Trends Analytics")
main.resizable(0, 0)
def Exit():
    sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=main)
    if sure == True:
        main.destroy()
        
main.protocol("WM_DELETE_WINDOW", Exit)

def emp():
    main.withdraw()
    os.system("python dashboard.py")
    main.deiconify()


def adm():
    main.withdraw()
    os.system("python admin.py")
    main.deiconify()


def emp1():
    main.withdraw()
    os.system("python employee.py")
    main.deiconify()

label1 = Label(main)
label1.place(relx=0, rely=0, width=1366, height=768)
img = PhotoImage(file="./images/M.png")
label1.configure(image=img)

button1 = Button(main)
button1.place(relx=0.032, rely=0.51, width=120, height=90)
button1.configure(relief="flat")
button1.configure(overrelief="flat")
button1.configure(activebackground="#ffffff")
button1.configure(cursor="hand2")
button1.configure(foreground="#ffffff")
button1.configure(background="#ffffff")
button1.configure(borderwidth="0")
img2 = PhotoImage(file="./images/ana.png")
button1.configure(image=img2)
button1.configure(command=emp)

button2 = Button(main)
button2.place(relx=0.3, rely=0.51, width=120, height=90)
button2.configure(relief="flat")
button2.configure(overrelief="flat")
button2.configure(activebackground="#ffffff")
button2.configure(cursor="hand2")
button2.configure(foreground="#ffffff")
button2.configure(background="#ffffff")
button2.configure(borderwidth="0")
img3 = PhotoImage(file="./images/2.png")
button2.configure(image=img3)
button2.configure(command=adm)


button3 = Button(main)
button3.place(relx=0.16, rely=0.51, width=120, height=90)
button3.configure(relief="flat")
button3.configure(overrelief="flat")
button3.configure(activebackground="#ffffff")
button3.configure(cursor="hand2")
button3.configure(foreground="#ffffff")
button3.configure(background="#ffffff")
button3.configure(borderwidth="0")
img4 = PhotoImage(file="./images/1.png")
button3.configure(image=img4)
button3.configure(command=emp1)



main.mainloop()
