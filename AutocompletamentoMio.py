from tkinter import *
Codici = [
    '12345', '7628194', '0098123', '123577',
    '2169084', '2672381', '1838091243', '12909012',
    '998212', '1298001']

def tastopremuto(event):
    print("tasto" +str(event.keysym))
    tasto = event.keysym
    if len(tasto)==1 and completato == True:
        posizione = box.index(INSERT)
        box.delete(pos,END)

def confronta_stringa():
    tasti = []
    for x in Codici:
        if x.startswith(testo.get()):
            tasti.append(x)
            print(x)
    return tasti

def mostra_comp(lista):
    if len(lista)==1:
        testo.set(lista[0])
        completato = True

def tastolasciato(event):
    if len(event.keysym)==1:
        tasti = confronta_stringa()
        mostra_comp(tasti)
    #print("non piu")
    return 0
completato = False
root = Tk()
testo = StringVar()
box = Entry(root,textvariable=testo)
box.bind('<KeyRelease>',tastolasciato)
box.bind('Key',tastopremuto)
box.pack()
root.mainloop()
