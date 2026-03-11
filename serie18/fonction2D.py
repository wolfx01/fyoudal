from tkinter import *
from tkinter import messagebox



fen  =  Tk()
fen.title("1er degree")
lb1 = Label(fen , text = "valeur a :")
lb1.place(x = 50, y = 60)
lb2 = Label(fen , text = "valeur b :")
lb2.place(x = 50, y = 80)
lb3 = Label(fen , text = "valeur c :")
lb3.place(x = 50, y = 100)
lb4 = Label(fen , text = "delta : ")
lb4.place(x = 50, y = 120)
lb5 = Label(fen , text = "une solution : ")
lb5.place(x = 50, y = 140)
lb6 = Label(fen , text = "2 solutions : ")
lb6.place(x = 50, y = 160)
lb7 = Label(fen , text = "X1 : ")
lb7.place(x = 120, y = 160)
lb8 = Label(fen , text = "X2 : ")
lb8.place(x = 300, y = 160)
nb1 = Entry(fen)
nb1.place(x = 160, y = 60)
nb2 = Entry(fen)
nb2.place(x = 160, y = 80)
nb3 = Entry(fen)
nb3.place(x = 160, y = 100)
nb4 = Entry(fen)
nb4.place(x = 160, y = 120)
nb5 = Entry(fen)
nb5.place(x = 160, y = 140)
nb6 = Entry(fen)
nb6.place(x = 160, y = 160)
nb7 = Entry(fen)
nb7.place(x = 320, y = 160)
def action1():
    a = int(nb1.get())
    b = int(nb2.get())
    c  = int(nb3.get())


    d = (b ** 2) - 4 * a * c
    racine = d ** 0.5

    if a == 0 and b == 0 and c == 0:
        messagebox.showerror("imposible", "imposible")
    elif a == 0 and b != 0 and c != 0:
        x = -c / b
        nb5.insert(0, x)

    elif a == 0 and c == 0:
        x = 1 / b
        nb5.insert(0, x)

    elif d <= 0:
        messagebox.showerror("nest pas solution" ,"nest pas solution")
    elif d == 0:
        x = (-b) / (2 * a)
        nb5.insert(0, x)
    else:
        x1 = (-b - racine) / (2 * a)
        nb6.insert(0, x1)
        x2 = (-b + racine) / (2 * a)
        nb7.insert(0, x2)


    nb4.insert(0, d)
    nb4.config(state = "disabled")
    nb5.config(state = "disabled")
    nb6.config(state = "disabled")
    nb7.config(state = "disabled")
def action2():
    nb4.config(state="normal")
    nb5.config(state="normal")
    nb6.config(state="normal")
    nb7.config(state="normal")

    nb1.delete(0, END)
    nb2.delete(0, END)
    nb3.delete(0, END)
    nb4.delete(0, END)
    nb5.delete(0, END)
    nb6.delete(0, END)
    nb7.delete(0, END)
    nb1.focus()

def action3():
    fen.quit()


b1  = Button(fen, text = "calcul", command = action1).place(x = 100, y = 200)
b2 = Button(fen, text = "vider", command = action2).place(x = 200, y = 200)
b3 = Button(fen, text = "fermer", command = action3).place(x = 300, y = 200)
fen.mainloop()