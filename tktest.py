from tkinter import *
from testclasse import restbottiglie
result_row = []
def visualizza():
    diz = restbottiglie()
    testo=""
    for x in diz.values():
        testo += x.stampaBottiglia()+"\n"
    label = Label(root,text=testo)
    label.grid(row=4,column=0)

def vendita():
    return 0
def deposito():
    return 0
def aggiungi():
    return 0
root = Tk()
root.geometry("500x500")
root.title("Bottiglie")

btn_visualizza = Button(root,text="Visualizza tutte le bottiglie",command=visualizza)
btn_vendita = Button(root,text="Registra una vendita",command=vendita)
btn_deposito = Button(root,text="Registra un deposito",command=deposito)
btn_aggiungi= Button(root,text="Aggiungi una Bottiglia",command=aggiungi)
#risultato = Entry(root,text="Test",width="50")


btn_visualizza.grid(row=0,column=0)
btn_vendita.grid(row=1,column=0)
btn_deposito.grid(row=2,column=0)
btn_aggiungi.grid(row=3,column=0)
#risultato.grid(row=1,column=0)

root.mainloop()
