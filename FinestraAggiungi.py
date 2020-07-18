from tkinter import *
from Classe import Bottiglia
from Var import Bottiglie,tipi
import Queryfunctions as Qf
entries = {}

def btn_conferma_cliccato(fin_inserimento,):
    global entries
    global Bottiglie

    tmplist = [] #lista per accogliere temporeaneamente i dati
    for x in entries.values():
        tmplist.append(x.get())

    nBottiglia=Bottiglia(tmplist[0],tmplist[1],tmplist[2],tmplist[3],tmplist[4],tmplist[5])
    print(nBottiglia.controlloValori())

    if not nBottiglia.controlloValori() and tmplist[0] not in Bottiglie.keys() :
        x=0
        #Non ci sono errori procedere all' Inserimento
        msg = Label(fin_inserimento,text="Non ci sono errori")

        if Qf.insertBottiglia(tmplist)==0:
            msg = Label(fin_inserimento,text="Dati inseriti correttamente")
        else:
            msg = Label(fin_inserimento,text=Qf.insertBottiglia(tmplist))
    else:

        if tmplist[0] in Bottiglie.keys():
            entries["Codice"].delete(0,END)     #If necessario per sapere se eliminare o meno il codice
        msg = Label(fin_inserimento,text="Ricontrolla i campi che si sono eliminati")

        for er in nBottiglia.controlloValori():
            entries[er].delete(0,END)

    msg.grid(row=7,column=0,columnspan=2)

def cliccato():
    return 0

def lanciafinestra(root):
    global entries,tipi
    labels = []
    row=1
    Campi = ["Codice","Nome","Quantita","P_acquisto","P_vendita","Data_Acqusito"]
    fin_inserimento = Toplevel(root)
    testo = Label(fin_inserimento,text="Inserisci i dati richiesti")
    btn_conferma= Button(fin_inserimento,text="inserisci",command=lambda:btn_conferma_cliccato(fin_inserimento))
    print(Qf.getTipi().values())
    print(tipi.values())
    dropdown = OptionMenu(fin_inserimento,cliccato,tipi.values())


    fin_inserimento.title("Inserisci")

    for cam in Campi:
        entries[cam]= Entry(fin_inserimento,text=cam)

    for cam in Campi:
        labels.append(Label(fin_inserimento,text=cam)) #Genero i label per ogni campo

    for lab in labels:
        lab.grid(row=row,column=0)
        row+=1
    row=1

    for en in entries.values():
        en.grid(row=row,column=1)
        row+=1

    btn_conferma.grid(row=row+2,column=0,columnspan=2)
    dropdown.grid(row=row+1,column=0,columnspan=2)
    testo.grid(row=0,column=0,columnspan=2)
