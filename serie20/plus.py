from tkinter import *
from tkinter import messagebox, ttk



def creer_fenetre_exo(titre):
    win = Toplevel(root)
    win.title(titre)
    win.geometry("450x450")
    Label(win, text=titre, font=("Arial", 12, "bold"), fg="darkblue").pack(pady=10)
    return win




def fen_q1_q2_q3():
    win = creer_fenetre_exo("Q1, Q2, Q3: Somme, Fact, Série K")
    Label(win, text="Entrez la valeur de n :").pack()
    ent_n = Entry(win)
    ent_n.pack()
    res = Label(win, text="", font=("Arial", 11), fg="green")
    res.pack(pady=15)

    def calculer(choix):
        try:
            n = int(ent_n.get())
            if choix == 1:
                res.config(text=f"Somme (0 à n) : {sum(range(n + 1))}")
            elif choix == 2:
                f = 1
                for i in range(1, n + 1): f *= i
                res.config(text=f"Factorielle ({n}!) : {f}")
            elif choix == 3:
                k = sum(1 / i for i in range(1, n + 1))
                res.config(text=f"Série K (1 + 1/2... + 1/n) : {k:.4f}")
        except:
            messagebox.showerror("Erreur", "Veuillez entrer un entier")

    Button(win, text="Calculer Somme (Q1)", width=25, command=lambda: calculer(1)).pack(pady=5)
    Button(win, text="Calculer Factorielle (Q2)", width=25, command=lambda: calculer(2)).pack(pady=5)
    Button(win, text="Calculer Série K (Q3)", width=25, command=lambda: calculer(3)).pack(pady=5)


def fen_q4():
    win = creer_fenetre_exo("Q4: Série Alternée T")
    Label(win, text="Entrez n :").pack()
    ent_n = Entry(win)
    ent_n.pack()
    res = Label(win, text="", font=("Arial", 11), fg="purple")
    res.pack(pady=20)

    def calculer():
        try:
            n = int(ent_n.get())
            t = 0
            for i in range(1, (2 * n) + 1):
                t = t - i if i % 2 != 0 else t + i
            res.config(text=f"Résultat T = {t}")
        except:
            messagebox.showerror("Erreur", "Entrer un entier")

    Button(win, text="Calculer", command=calculer).pack()


def fen_q5_q7_q8():
    win = creer_fenetre_exo("Q5, Q7, Q8: Armstrong, Parfaits, Premiers")
    lb = Listbox(win, width=40, height=12)
    lb.pack(pady=10)

    def armstrong():
        lb.delete(0, END)
        for i in range(101):
            if sum(int(d) ** 3 for d in str(i)) == i: lb.insert(END, f"{i} est Armstrong")

    def parfaits():
        lb.delete(0, END)
        for n in range(1, 41):
            if sum(i for i in range(1, n) if n % i == 0) == n: lb.insert(END, f"{n} est Parfait")

    def premiers():
        lb.delete(0, END)
        for n in range(2, 41):
            if all(n % i != 0 for i in range(2, int(n ** 0.5) + 1)): lb.insert(END, f"{n} est Premier")

    Button(win, text="Q5: Armstrong (0-100)", width=25, command=armstrong).pack(pady=2)
    Button(win, text="Q7: Parfaits (1-40)", width=25, command=parfaits).pack(pady=2)
    Button(win, text="Q8: Premiers (1-40)", width=25, command=premiers).pack(pady=2)


def fen_q6():
    win = creer_fenetre_exo("Q6: Série de Syracuse")
    ent = Entry(win);
    ent.pack();
    lb = Listbox(win, width=30);
    lb.pack(pady=10)

    def calculer():
        try:
            n = int(ent.get());
            lb.delete(0, END)
            while n != 1:
                lb.insert(END, n)
                n = n // 2 if n % 2 == 0 else n * 3 + 1
            lb.insert(END, 1)
        except:
            pass

    Button(win, text="Générer", command=calculer).pack()


def fen_q9():
    win = creer_fenetre_exo("Q9: Nombres Amis (Somme des chiffres)")

    Label(win, text="Entrez le nombre n (cible) :").pack(pady=5)
    ent_n = Entry(win)
    ent_n.pack()

    Label(win, text="Amis trouvés entre 0 et 100 :").pack(pady=5)
    lb = Listbox(win, width=40, height=10)
    lb.pack(pady=10)

    def verifier():
        try:
            n = int(ent_n.get())
            lb.delete(0, END)  # Effacer les anciens résultats

            for i in range(0, 101):
                dizaine = i // 10
                unite = i % 10
                somme = dizaine + unite

                if i == 100:
                    somme = 1 + 0 + 0

                if somme == n:
                    lb.insert(END, f"{i} est ami (car {dizaine} + {unite} = {n})")

            if lb.size() == 0:
                lb.insert(END, "Aucun ami trouvé.")

        except ValueError:
            messagebox.showerror("Erreur", "Saisir un entier valide")

    Button(win, text="Trouver les Amis", command=verifier, bg="lightgreen").pack()
def fen_q10():
    win = creer_fenetre_exo("Q10: Alphabet (Combobox)")
    combo = ttk.Combobox(win, values=["Majuscule", "Minuscule"]);
    combo.set("Majuscule");
    combo.pack()
    lb = Listbox(win, width=20);
    lb.pack(pady=10)

    def afficher():
        lb.delete(0, END)
        start = 65 if combo.get() == "Majuscule" else 97
        for i in range(start, start + 26): lb.insert(END, chr(i))

    Button(win, text="Afficher Alphabet", command=afficher).pack()


def fen_q11_q12():
    win = creer_fenetre_exo("Q11, Q12: Semaine & Table X")
    ent = Entry(win);
    ent.pack();
    lb = Listbox(win, width=30);
    lb.pack(pady=10)

    def semaine():
        lb.delete(0, END)
        for j in ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]: lb.insert(END, j)

    def table():
        try:
            n = int(ent.get());
            lb.delete(0, END)
            for i in range(1, 11): lb.insert(END, f"{n} x {i} = {n * i}")
        except:
            pass

    Button(win, text="Q11: Jours Semaine", width=20, command=semaine).pack(pady=2)
    Button(win, text="Q12: Table Multi.", width=20, command=table).pack(pady=2)


def fen_q13_q14():
    win = creer_fenetre_exo("Q13, Q14: Voyelles & Figure")
    ent = Entry(win, width=30)
    ent.pack()
    res = Label(win, text="");
    res.pack()
    lb = Listbox(win, width=40, font=("Courier", 10));
    lb.pack(pady=10)

    def voyelles():
        v = sum(1 for c in ent.get().lower() if c in "aeiouy")
        res.config(text=f"Voyelles : {v}")

    def figure():
        lb.delete(0, END)
        n = 4
        f_esp = lambda k: " " * (n - k)
        f_etol = lambda k: "*" * k
        for i in range(1, n + 1):
            lb.insert(END, f_esp(i) + f_etol(i))
        for i in range(n - 1, 0, -1):
            lb.insert(END, f_esp(i) + f_etol(i))

    Button(win, text="Q13: Compter Voyelles", width=20, command=voyelles).pack(pady=2)
    Button(win, text="Q14: Dessiner Figure", width=20, command=figure).pack(pady=2)


# --- MENU PRINCIPAL ---
root = Tk()
root.title("Menu TP Série 20 - Complet")
root.geometry("450x650")

Label(root, text="MENU GÉNÉRAL EXERCICES", font=("Arial", 14, "bold"), bg="lightgrey").pack(fill=X, pady=10)

frame_m = Frame(root)
frame_m.pack(pady=20)

btns = [
    ("Q1, Q2, Q3: Séries (n!, Somme, K)", fen_q1_q2_q3),
    ("Q4: Série Alternée (T)", fen_q4),
    ("Q5, Q7, Q8: Listes Nombres", fen_q5_q7_q8),
    ("Q6: Suite de Syracuse", fen_q6),
    ("Q9: Nombres Amis", fen_q9),
    ("Q10: Alphabet (Combo)", fen_q10),
    ("Q11, Q12: Semaine & Table", fen_q11_q12),
    ("Q13, Q14: Voyelles & Figure", fen_q13_q14)
]

for t, cmd in btns:
    Button(frame_m, text=t, width=35, height=2, command=cmd).pack(pady=5)

Button(root, text="QUITTER", bg="red", fg="white", command=root.destroy).pack(side=BOTTOM, pady=20)

root.mainloop()