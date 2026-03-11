from  tkinter import *
from  tkinter import ttk
from tkinter import messagebox
fen  = Tk()
fen.title("calcul poids")
lb1 = Label(fen ,  text= "taille")
lb1.place(x= 50 ,  y = 60 )
lb2 = Label(fen ,  text= "genre")
lb2.place(x= 50 ,  y = 80 )
lb2 = Label(fen ,  text= "prids")
lb2.place(x= 50 ,  y = 100 )
cb = ttk.Combobox(fen , values=["femme" ,  "homme"])
cb.place(x= 160 , y = 80 )
nb1 = Entry(fen )
nb1.place(x= 160 , y = 60 )
nb2 = Entry(fen )
nb2.place(x= 160 , y = 100 )



def action1():
    try:
        t= int(nb1.get())
        if t < 140:
            messagebox.showinfo("Error" , "taille invalide ")
        else:

            b = cb.get()
            if b == "homme":
                pi = (t - 100) * 0.9

            else:
                if b == "femme":
                    pi = (t - 100) * 0.85

                else:
                    messagebox.showerror("homme or femme !!!!")


        nb2.insert(0, pi)
        nb2.config(state="disabled")
    except:
        messagebox.showerror("homme or femme !!!!")



def action2():
    nb2.config(state="normal")
    nb1.delete(0, END)
    cb.delete(0, END)
    nb2.delete(0, END)
    nb1.focus()

def action3():
    fen.quit()


b1 = Button(fen, text="calcul", command=action1).place(x=100, y=140)
b2 = Button(fen, text="vider", command=action2).place(x=200, y=140)
b3 = Button(fen, text="fermer", command=action3).place(x=300, y=140)
fen.mainloop()



