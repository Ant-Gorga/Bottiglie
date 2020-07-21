from tkinter import *
from Classe import Bottiglia
from Var import Bottiglie,tipi,get_key,fornitori
import Queryfunctions as Qf
entries = {}

def btn_conferma_cliccato(fin_inserimento,tipo,fornitore):
    global entries
    global Bottiglie
    global tipi
    print("Cazzi"+str(get_key(tipi, tipo.get()))) # è possibile avere la chiave dal liquore

    tmplist = [] #lista per accogliere temporeaneamente i dati
    for x in entries.values():
        tmplist.append(x.get())

    nBottiglia=Bottiglia(tmplist[0],tmplist[1],tmplist[2],tmplist[3],tmplist[4],tmplist[5])
    print(nBottiglia.controlloValori())

    if not nBottiglia.controlloValori() and tmplist[0] not in Bottiglie.keys() :
        x=0
        #Non ci sono errori procedere all' Inserimento
        msg = Label(fin_inserimento,text="Non ci sono errori")
        id_tipo=get_key(tipi, tipo.get())
        id_fornitore=get_key(fornitori, fornitore.get())
        if Qf.insertBottiglia(tmplist,id_tipo,id_fornitore)==0: #passo alla funzione la chiave dell' elemento corrispondente
            msg = Label(fin_inserimento,text="Dati inseriti correttamente")
        else:
            msg = Label(fin_inserimento,text=Qf.insertBottiglia(tmplist,id_tipo,id_fornitore))
    else:

        if tmplist[0] in Bottiglie.keys():
            entries["Codice"].delete(0,END)     #If necessario per sapere se eliminare o meno il codice
        msg = Label(fin_inserimento,text="Ricontrolla i campi che si sono eliminati")

        for er in nBottiglia.controlloValori():
            entries[er].delete(0,END)

    msg.grid(row=7,column=0,columnspan=2)


def lanciafinestra(root):
    global entries,tipi,fornitori
    labels = []
    row=1
    Campi = ["Codice","Nome","Quantita","P_acquisto","P_vendita","Data_Acqusito"]
    fin_inserimento = Toplevel(root)
    testo = Label(fin_inserimento,text="Inserisci i dati richiesti")
    btn_conferma= Button(fin_inserimento,text="inserisci",command=lambda:btn_conferma_cliccato(fin_inserimento,tipo,fornitore))
    print("Query Tipi:"+ str(Qf.getTipi()))
    print("Query fornitori:"+str(Qf.getFornitori()))
    tipo = StringVar()
    tipo.set(tipi[1])

    fornitore = StringVar()

    dropdownTipi = OptionMenu(fin_inserimento,tipo,*tipi.values())
    #Il punto esclamativo serve
    #per "spalmare" le variabili
    dropdownFornitori = OptionMenu(fin_inserimento,fornitore,*fornitori.values())

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

    btn_conferma.grid(row=row+3,column=0,columnspan=2)
    dropdownTipi.grid(row=row+1,column=0,columnspan=2)
    dropdownFornitori.grid(row=row+2,column=0,columnspan=2)
    testo.grid(row=0,column=0,columnspan=2)
