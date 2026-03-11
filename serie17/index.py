from tkinter import *
from tkinter import messagebox


print("1 - somme")
print("2 - produit")
print("3 - division")
print("4 - surface")
print("5 - poids ")
choix  = int(input("choix : "))
if choix == 1:
    fen  =  Tk()
    fen.title("somme")
    lb1 = Label(fen , text = "valeur a")
    lb1.place(x = 50, y = 60)
    lb2 = Label(fen , text = "valeur b")
    lb2.place(x = 50, y = 80)
    lb3 = Label(fen , text = "result")
    lb3.place(x = 50, y = 100)
    nb1 = Entry(fen)
    nb1.place(x = 160, y = 60)
    nb2 = Entry(fen)
    nb2.place(x = 160, y = 80)
    nb3 = Entry(fen)
    nb3.place(x = 160, y = 100)
    def action1():
        a = int(nb1.get())
        b = int(nb2.get())
        s  = a + b
        nb3.insert(0, s)
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

elif choix == 2:
    fen  =  Tk()
    fen.title("produit")
    lb1 = Label(fen , text = "valeur x")
    lb1.place(x = 50, y = 60)
    lb2 = Label(fen , text = "valeur y")
    lb2.place(x = 50, y = 80)
    lb3 = Label(fen , text = "result")
    lb3.place(x = 50, y = 100)
    nb1 = Entry(fen)
    nb1.place(x = 160, y = 60)
    nb2 = Entry(fen)
    nb2.place(x = 160, y = 80)
    nb3 = Entry(fen)
    nb3.place(x = 160, y = 100)
    def action1():
        a = int(nb1.get())
        b = int(nb2.get())
        s  = a * b
        nb3.insert(0, s)
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
elif choix == 3:
    fen  =  Tk()
    fen.title("division")
    lb1 = Label(fen , text = "valeur x")
    lb1.place(x = 50, y = 60)
    lb2 = Label(fen , text = "valeur y")
    lb2.place(x = 50, y = 80)
    lb3 = Label(fen , text = "result")
    lb3.place(x = 50, y = 100)
    nb1 = Entry(fen)
    nb1.place(x = 160, y = 60)
    nb2 = Entry(fen)
    nb2.place(x = 160, y = 80)
    nb3 = Entry(fen)
    nb3.place(x = 160, y = 100)
    def action1():


            a = int(nb1.get())
            b = int(nb2.get())
            if b == 0:
                messagebox.showerror("devision imposible")
            s  = a / b
            nb3.insert(0, s)
            nb3.config(state = "disabled")

    def action2():
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
elif choix == 4:
    fen  =  Tk()
    fen.title("surface")
    lb1 = Label(fen , text = "valeur r")
    lb1.place(x = 50, y = 60)


    lb3 = Label(fen , text = "result")
    lb3.place(x = 50, y = 100)
    nb1 = Entry(fen)
    nb1.place(x = 160, y = 60)

    nb3 = Entry(fen)
    nb3.place(x = 160, y = 100)
    def action1():

            r = int(nb1.get())

            s  = r*r*3.14
            nb3.insert(0, s)
            nb3.config(state = "disabled")

    def action2():
        nb1.delete(0, END)
        nb2.delete(0, END)
        nb3.delete(0, END)
        nb1.focus()
        nb3.config(state = "normal")
    def action3():
        fen.quit()


    b1  = Button(fen, text = "calcul", command = action1).place(x = 100, y = 140)
    b2 = Button(fen, text = "vider", command = action2).place(x = 200, y = 140)
    b3 = Button(fen, text = "fermer", command = action3).place(x = 300, y = 140)
    fen.mainloop()
elif choix == 5 :
    fen = Tk()
    fen.title("poids ideal")
    lb1 = Label(fen, text="talle ")
    lb1.place(x=50, y=60)
    lb2 = Label(fen, text="nature")
    lb2.place(x=50, y=80)
    lb3 = Label(fen, text="poids")
    lb3.place(x=50, y=100)
    nb1 = Entry(fen)
    nb1.place(x=160, y=60)
    nb2 = Entry(fen)
    nb2.place(x=160, y=80)
    nb3 = Entry(fen)
    nb3.place(x=160, y=100)


    def action1():
        a = int(nb1.get())
        b = nb2.get()
        pi = 0



        if a < 140:
            messagebox.showerror("taille incorrect")
        else:


            if b == "homme":
                pi = (a - 100) * 0.9

            else:
                if n == "femme":
                    pi = (a - 100) * 0.85

                else:
                    messagebox.showerror("homme or femme !!!!")
        nb3.insert(0, pi)
        nb3.config(state="disabled")



    def action2():
        nb3.config(state="normal")
        nb1.delete(0, END)
        nb2.delete(0, END)
        nb3.delete(0, END)
        nb1.focus()


    def action3():
        fen.quit()


    b1 = Button(fen, text="calcul", command=action1).place(x=100, y=140)
    b2 = Button(fen, text="vider", command=action2).place(x=200, y=140)
    b3 = Button(fen, text="fermer", command=action3).place(x=300, y=140)
    fen.mainloop()

