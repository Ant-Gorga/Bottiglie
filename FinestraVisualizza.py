from tkinter  import *
from Var import *
import Queryfunctions as Qf

def keypressed(event,fin_visualizza):
    if event.char == '\r':
        fin_visualizza.destroy()

def lanciafinestra(root):
    global Bottiglie
    Qf.getBottiglie()
    ris = ""
    for b in Bottiglie.values():
        ris += b.stampaBottiglia() + "\n"

    fin_visualizza = Toplevel(root)

    label_bottiglie = Label(fin_visualizza,text=ris)
    btn_chiudi = Button(fin_visualizza,text="Chiudi!",command= fin_visualizza.destroy)
    btn_chiudi.focus_set()
    btn_chiudi.bind("<Key>",lambda event,fin=fin_visualizza : keypressed(event,fin))
    label_bottiglie.grid(row=0,column=0)
    btn_chiudi.grid(row=1,column=0)
