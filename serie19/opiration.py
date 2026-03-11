from tkinter import *
from tkinter import messagebox
from tkinter import ttk
fen = Tk()
fen.title("Calculatrice")
fen.geometry("400x300")
op_var = ttk.Combobox(fen , values = ["+", "-", "*", "/"])
Label(fen, text="valeur a").place(x=50, y=40)
Label(fen, text="valeur b").place(x=50, y=80)
Label(fen, text="operation").place(x=50, y=120)
Label(fen, text="resultat").place(x=50, y=160)
nb1 = Entry(fen)
nb1.place(x=160, y=40)
nb2 = Entry(fen)
nb2.place(x=160, y=80)
op_var.place(x=160, y=115, width=125)
nb3 = Entry(fen)
nb3.place(x=160, y=160)
def action1():
    try:
        a = float(nb1.get())
        b = float(nb2.get())
        op = op_var.get()
        if op == "+":
            res = a + b
        elif op == "-":
            res = a - b
        elif op == "*":
            res = a * b
        elif op == "/":
            if b == 0:
                messagebox.showerror("Error", "Division par 0")
                return
            res = a / b
        nb3.insert(0, str(res))
    except:
        messagebox.showerror("Error", "Entrez des nombres")
def action2():
    nb1.delete(0, END)
    nb2.delete(0, END)
    nb3.delete(0, END)
    op_var.delete(0, END)
def action3():
    fen.destroy()
Button(fen, text="calcul", command=action1).place(x=50, y=220)
Button(fen, text="vider", command=action2).place(x=150, y=220)
Button(fen, text="fermer", command=action3).place(x=250, y=220)
fen.mainloop()