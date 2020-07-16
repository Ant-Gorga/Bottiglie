from tkinter import *
entries = {}
def controllodati():
    return 0
def btn_conferma_cliccato():
    global entries
    for x in entries.values():
        print(x)

def lanciafinestra(root):
    global entries
    labels = []


    row=1
    Campi = ["Codice","Nome","Quantita","P_acquisto","P_vendita","Data_Acqusito"]
    fin_inserimento = Toplevel(root)
    testo = Label(fin_inserimento,text="Inserisci i dati richiesti")
    btn_conferma= Button(fin_inserimento,text="inserisci",command=btn_conferma_cliccato)

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

    btn_conferma.grid(row=row+1,column=1,columnspan=2)
