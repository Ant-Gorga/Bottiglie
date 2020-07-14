#File per lavorare senza server,
#Creazione della gui
from tkinter import *
root = Tk()
root.title("Bottiglie")
def bottone_click():
    testo= Label(root,text="")
    
    testo = Label(root,text=e.get())
    testo.grid(row=3,column=3)

#Creo un widget
label = Label(root,text="Ciao")
nome = Label(root,text="Antonio")
bottone = Button(root,text="Cliccami",padx=50,pady=10,command=bottone_click) #puo essere disabilitato con state=DISABLED
e = Entry(root) #height, width, bg, fg
#e.get() # prende il testo

#lo mostro sullo schermo (diversi modi)
# label.pack(), label.grid
label.grid(row=0,column=0)
nome.grid(row=1,column=1)
bottone.grid(row=2,column=0)
e.grid(row=2,column=2)
root.mainloop()
