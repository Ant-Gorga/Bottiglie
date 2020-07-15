from tkinter import *
from testclasse import restbottiglie
result_row = []
def visualizza():
    diz = restbottiglie()
    testo=""
    for x in diz.values():
        testo += x.stampaBottiglia()+"\n"
    label = Label(root,text=testo,anchor="w")
    label.grid(row=1,column=0)
root = Tk()

root.title("Bottiglie")

btn_visualizza = Button(root,text="Visualizza tutte le bottiglie",command=visualizza)
#risultato = Entry(root,text="Test",width="50")


btn_visualizza.grid(row=0,column=0)
#risultato.grid(row=1,column=0)

root.mainloop()