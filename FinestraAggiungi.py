from tkinter import *
from Classe import Bottiglia
from Var import Bottiglie, tipi, get_key, fornitori
import Queryfunctions as Qf

# Variables Global
entries = {}
msg = ""


def btn_conferma_cliccato(tipo, fornitore, testo_msg):
    global entries, Bottiglie, tipi

    tmplist = []  # lista per accogliere temporeaneamente i dati del fonrm

    for x in entries.values():
        tmplist.append(x.get())  # Prendo i valori dal dizionario delle entries e li metto in una lista

    nBottiglia = Bottiglia(tmplist[0], tmplist[1], tmplist[2], tmplist[3], tmplist[4], tmplist[5])

    if not nBottiglia.controlloValori() and tmplist[0] not in Bottiglie.keys():
        # controllo se non ci sono errori e se il codice non è già presente
        # Non ci sono errori procedere all' Inserimento
        testo_msg.set("Non ci sono errori")

        id_tipo = get_key(tipi, tipo.get())  # grazie alla funzione get_key
        id_fornitore = get_key(fornitori, fornitore.get())  # prendo l' id

        esito = Qf.insertBottiglia(nBottiglia, id_tipo,
                                   id_fornitore)  # passo alla funzione la chiave dell' elemento corrispondente
        if esito == 0:
            testo_msg.set("Dati inseriti correttamente")
        else:
            testo_msg.set(esito)  # Spiegarlo nel readme
    else:

        if tmplist[0] in Bottiglie.keys():
            entries["Codice"].delete(0, END)  # If necessario per sapere se eliminare o meno il codice
        testo_msg.set("Ricontrolla i campi che si sono eliminati")

        for er in nBottiglia.controlloValori():
            entries[er].delete(0, END)


def lanciafinestra(root):
    global entries, tipi, fornitori, msg

    fin_inserimento = Toplevel(root)
    labels = []
    row = 1
    testo_msg = StringVar()
    tipo = StringVar()
    fornitore = StringVar()
    Campi = ["Codice", "Nome", "Quantita", "P_acquisto", "P_vendita", "Data_Acqusito"]

    testo = Label(fin_inserimento, text="Inserisci i dati richiesti")
    btn_conferma = Button(fin_inserimento, text="inserisci",
                          command=lambda: btn_conferma_cliccato(tipo, fornitore, testo_msg))
    msg = Label(fin_inserimento, textvariable=testo_msg)
    Qf.getFornitori()
    Qf.getTipi()
    #print(tipi)
    #print(fornitori)
    # print("Query fornitori:"+str(Qf.getFornitori()))
    # print("Query Tipi:"+ str(Qf.getTipi()))
    dropdownTipi = OptionMenu(fin_inserimento, tipo, *tipi.values())
    dropdownFornitori = OptionMenu(fin_inserimento, fornitore, *fornitori.values())
    # Il punto esclamativo serve
    # per "spalmare" le variabili
    testo_msg.set("Inserisci la data nel formato YYYYMMDD")
    tipo.set(tipi[1])

    keys = fornitori.keys()
    print(keys)
    fornitore.set(fornitori[list(keys)[0]])  # Da spiegare nel readme

    fin_inserimento.title("Inserisci")

    for cam in Campi:
        entries[cam] = Entry(fin_inserimento, text=cam)

    for cam in Campi:
        labels.append(Label(fin_inserimento, text=cam))  # Genero i label per ogni campo

    for lab in labels:
        lab.grid(row=row, column=0)
        row += 1
    row = 1

    for en in entries.values():
        en.grid(row=row, column=1)
        row += 1

    testo.grid(row=0, column=0, columnspan=2)
    dropdownTipi.grid(row=row + 1, column=0, columnspan=2)
    dropdownFornitori.grid(row=row + 2, column=0, columnspan=2)
    msg.grid(row=row + 3, column=0, columnspan=2)
    btn_conferma.grid(row=row + 4, column=0, columnspan=2)