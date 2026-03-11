from tkinter import *
from tkinter import messagebox



fen  =  Tk()
fen.title("resultet")
lb1 = Label(fen , text = "valeur   de m ")
lb1.place(x = 50, y = 60)
lb3 = Label(fen , text = " valeur de K ")
lb3.place(x = 50, y = 90)
lb3.place(x = 50, y = 100)
nb1 = Entry(fen)
nb1.place(x = 160, y = 60)
nb3 = Entry(fen)
nb3.place(x = 160, y = 100)
def action1():
    m = int(nb1.get())
    if m%2 == 0 :
        k  =  2*m +3
    else:
        k = 3*m -1



    nb3.insert(0, k)
    nb3.config(state = "disabled")
def action2():
    nb3.config(state="normal")
    nb1.delete(0, END)
    nb2.delete(0, END)
    nb3.delete(0, END)
    nb1.focus()

def action3():
    fen.quit()


b1  = Button(fen, text = "calcul", command = action1).place(x = 100, y = 140)
b2 = Button(fen, text = "vider", command = action2).place(x = 200, y = 140)
b3 = Button(fen, text = "fermer", command = action3).place(x = 300, y = 140)
fen.mainloop()