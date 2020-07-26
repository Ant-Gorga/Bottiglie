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
                esito =Qf.deposito(codice.get(),num.get())
                if  esito== 0:
                    testo_msg.set("Deposito Registrato")
                else:
                    testo_msg.set(esito)
        except ValueError:
            testo_msg.set("Il numero non è corretto")

def lanciafinestra(root):


    fin_deposito = Toplevel(root)
    fin_deposito.title("Deposito")
    testo_msg = StringVar()
    testo_msg.set("Nessun dato inserito")
    text1 = Label(fin_deposito,text="Inserisci Codice")
    codice = EntryAutocompletamento(fin_deposito)
    n_Bottigia = Label(fin_deposito,textvariable=codice.n_Bottiglia_text)
    text2 = Label(fin_deposito,text="Quante bottiglie vuoi aggiungere?")
    num = Entry(fin_deposito)
    msg = Label(fin_deposito,textvariable=testo_msg)
    btn_conferma = Button(fin_deposito,text="Conferma",command=lambda:btn_conferma_cliccato(codice,num,testo_msg))

    codice.bind('<KeyRelease>',codice.tastolasciato)

    text1.grid(row=0,column=0)
    codice.grid(row=1,column=0)
    n_Bottigia.grid(row=2,column=0)
    text2.grid(row=3,column=0)
    num.grid(row=4,column=0)
    btn_conferma.grid(row=5,column=0)
    msg.grid(row=6,column=0)
