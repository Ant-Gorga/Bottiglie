from tkinter import *
from Classe import Bottiglia
from Var import Bottiglie,tipi,get_key,fornitori
import Queryfunctions as Qf
from AutocompletamentoClass import EntryAutocompletamento

msg = ""

def btn_conferma_cliccato(codice,num,testo_msg):
    global Bottiglie
    if codice.get() not in Bottiglie.keys():
        testo_msg.set("Il codice non è correto")
    else:
        try:
            if int(num.get()) < 99 and int(num.get()) > 0 :
                if Qf.deposito(codice.get(),num.get()) == 0:    #Cambiare il controllo, che deve essere <= di n_bottiglia del codice
                    testo_msg.set("Deposito Registrato")
                else:
                    testo_msg.set(Qf.deposito(codice.get(),num.get()))
        except ValueError:
            testo_msg.set("Il numero non è corretto")

def lanciafinestra(root):


    fin_vendita = Toplevel(root)
    fin_vendita.title("Vendita")
    testo_msg = StringVar()
    testo_msg.set("Nessun dato inserito")
    text1 = Label(fin_vendita,text="Inserisci Codice")
    codice = EntryAutocompletamento(fin_vendita)
    n_Bottigia = Label(fin_vendita,textvariable=codice.n_Bottiglia_text)
    text2 = Label(fin_vendita,text="Quante bottiglie hai venuto?")
    num = Entry(fin_vendita)
    msg = Label(fin_vendita,textvariable=testo_msg)
    btn_conferma = Button(fin_vendita,text="Conferma",command=lambda:btn_conferma_cliccato(codice,num,testo_msg))

    codice.bind('<KeyRelease>',codice.tastolasciato)

    text1.grid(row=0,column=0)
    codice.grid(row=1,column=0)
    n_Bottigia.grid(row=2,column=0)
    text2.grid(row=3,column=0)
    num.grid(row=4,column=0)
    btn_conferma.grid(row=5,column=0)
    msg.grid(row=6,column=0)
