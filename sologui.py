from tkinter import *
import FinestraAggiungi as Fa
import FinestraVisualizza as Fv
import FinestraDeposito as Fd
import Queryfunctions as Qf
import FinestraVendita as Fvn
import FinestraModifica as Fm
from Var import mariadb_connection,cursor
def keypressed(event,code):
    if event.char == '\r': #Con il keycode non è multiipllatform
        if code == "Fv":
            Fv.lanciafinestra(root)
        elif code == "Fvn":
            Fvn.lanciafinestra(root)
        elif code == "Fd":
            Fd.lanciafinestra(root)
        elif code == "Fa":
            Fa.lanciafinestra(root)
        elif code == "Fm":
            Fm.lanciafinestra(root)

root = Tk()
#root.geometry("500x500")
root.title("Bottiglie")
if Qf.conn():
    errorbox = Label(root,text=Qf.conn())
    errorbox.grid(row=5,column=0)
else:
    Qf.getBottiglie()

btn_visualizza = Button(root,text="Visualizza tutte le bottiglie",command= lambda:Fv.lanciafinestra(root))
btn_vendita = Button(root,text="Registra una vendita",command=lambda : Fvn.lanciafinestra(root))
btn_deposito = Button(root,text="Registra un deposito",command=lambda: Fd.lanciafinestra(root))
btn_aggiungi= Button(root,text="Aggiungi una Bottiglia",command=lambda: Fa.lanciafinestra(root))
btn_modifica = Button(root,text="Modifica un campo",command= lambda:Fm.lanciafinestra(root))

btn_visualizza.bind("<Key>",lambda event, code="Fv" :keypressed (event,code))
btn_vendita.bind("<Key>",lambda event, code="Fvn" :keypressed (event,code))
btn_deposito.bind("<Key>", lambda event,code="Fd": keypressed(event,code))
btn_aggiungi.bind("<Key>", lambda event,code ="Fa": keypressed(event,code))
btn_modifica.bind("<Key>",lambda event, code="Fm" :keypressed (event,code))
# replicarlo per gli altri
btn_visualizza.grid(row=0,column=0)
btn_vendita.grid(row=1,column=0)
btn_deposito.grid(row=2,column=0)
btn_aggiungi.grid(row=3,column=0)
btn_modifica.grid(row=4,column=0)


try:
    root.mainloop()
finally:
    global mariadb_connection
    #Controllare perchè non se lo prende
    mariadb_connection.close()
