from tkinter import *
#from testclasse import restbottiglie
import FinestraAggiungi as Fa
import FinestraVisualizza as Fv
import FinestraDeposito as Fd
import Queryfunctions as Qf
import FinestraVendita as Fvn
result_row = []
def visualizza():
    return 0
def vendita():
    return 0
def deposito():
    return 0
root = Tk()
#root.geometry("500x500")
root.title("Bottiglie")

if Qf.conn():
    errorbox = Label(root,text=Qf.conn())
    errorbox.grid(row=4,column=0)
else:
    Qf.getBottiglie()

btn_visualizza = Button(root,text="Visualizza tutte le bottiglie",command= lambda:Fv.lanciafinestra(root))
btn_vendita = Button(root,text="Registra una vendita",command=lambda : Fvn.lanciafinestra(root))
btn_deposito = Button(root,text="Registra un deposito",command=lambda: Fd.lanciafinestra(root))
btn_aggiungi= Button(root,text="Aggiungi una Bottiglia",command=lambda: Fa.lanciafinestra(root))
#risultato = Entry(root,text="Test",width="50")


btn_visualizza.grid(row=0,column=0)
btn_vendita.grid(row=1,column=0)
btn_deposito.grid(row=2,column=0)
btn_aggiungi.grid(row=3,column=0)
#risultato.grid(row=1,col


root.mainloop()
