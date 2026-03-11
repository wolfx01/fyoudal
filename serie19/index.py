from tkinter import *
from tkinter import messagebox
from tkinter import ttk


nb1 = nb2 = nb3 = nb4 = op_var = None
attempts = 0


def action1():
    try:

        t = float(nb1.get())
        c = op_var.get()
        pd = t / 4


        if c == "jeure":
            z = 0.2 * pd
        elif c == "vieux":
            z = 0.5 * pd
        elif c == "andicepe":
            z = 0.8 * pd
        else:  # adulte
            z = 0

        bpt = pd - z


        nb2.config(state="normal")
        nb3.config(state="normal")
        nb4.config(state="normal")

        nb2.delete(0, END)
        nb2.insert(0, f"{pd:.2f}")
        nb3.delete(0, END)
        nb3.insert(0, f"{z:.2f}")
        nb4.delete(0, END)
        nb4.insert(0, f"{bpt:.2f}")

        # Disable fields after calculation
        nb2.config(state="disabled")
        nb3.config(state="disabled")
        nb4.config(state="disabled")
    except ValueError:
        messagebox.showerror("Error", "Veuillez entrer un nombre valide pour le trajet")


def action2():
    # Helper to clear all fields
    for entry in [nb1, nb2, nb3, nb4]:
        if entry:
            entry.config(state="normal")
            entry.delete(0, END)
    if op_var:
        op_var.set('')
    nb1.focus()


def open_ticket_window():
    global nb1, nb2, nb3, nb4, op_var

    # Hide the login window instead of quitting
    fen.withdraw()

    fin = Toplevel()  # Use Toplevel for secondary windows
    fin.title("Billet ONCF")
    fin.geometry("400x350")

    Label(fin, text="Trajet (KM)").place(x=50, y=40)
    Label(fin, text="Catégorie").place(x=50, y=80)
    Label(fin, text="Plein Tarif").place(x=50, y=120)
    Label(fin, text="Réduction").place(x=50, y=160)
    Label(fin, text="Prix Billet").place(x=50, y=200)

    nb1 = Entry(fin)
    nb1.place(x=160, y=40)

    op_var = ttk.Combobox(fin, values=["jeure", "adulte", "vieux", "andicepe"])
    op_var.place(x=160, y=80, width=125)
    op_var.set("adulte")

    nb2 = Entry(fin)
    nb2.place(x=160, y=120)

    nb3 = Entry(fin)
    nb3.place(x=160, y=160)

    nb4 = Entry(fin)
    nb4.place(x=160, y=200)

    Button(fin, text="Calcul", command=action1).place(x=50, y=260)
    Button(fin, text="Vider", command=action2).place(x=150, y=260)
    Button(fin, text="Fermer", command=fen.destroy).place(x=250, y=260)


def action5():
    global attempts
    login_input = n1.get()
    pass_input = n2.get()

    if login_input == "bilal" and pass_input == "12345":
        open_ticket_window()
    else:
        attempts += 1
        remaining = 3 - attempts
        if remaining > 0:
            messagebox.showerror("Erreur", f"Login incorrect. Tentatives restantes: {remaining}")
        else:
            messagebox.showerror("Erreur", "Trop de tentatives. Fermeture.")
            fen.destroy()



fen = Tk()
fen.title("Login")
fen.geometry("400x300")

Label(fen, text="Login:").place(x=50, y=40)
Label(fen, text="Mot de passe:").place(x=50, y=80)

n1 = Entry(fen)
n1.place(x=160, y=40)
n2 = Entry(fen, show="*")
n2.place(x=160, y=80)

Button(fen, text="Se connecter", command=action5).place(x=50, y=200)
Button(fen, text="Quitter", command=fen.destroy).place(x=250, y=200)

fen.mainloop()