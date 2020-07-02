from tkinter import *
from testclasse import restbottiglie
root = Tk()
def bottone_click():
    ob = restbottiglie()
    print(str(ob[80220718].P_vendita))
    testo = Label(root,text=ob[80220718].stampaBottiglia())
    testo.grid(row=2,column=2)
#Creo un widget
label = Label(root,text="Ciao")
nome = Label(root,text="Antonio")
bottone = Button(root,text="Cliccami",padx=50,pady=10,command=bottone_click) #puo essere disabilitato con state=DISABLED
#lo mostro sullo schermo (diversi modi)
# label.pack(), label.grid
label.grid(row=0,column=0)
nome.grid(row=1,column=1)
bottone.grid(row=2,column=0)
root.mainloop()
