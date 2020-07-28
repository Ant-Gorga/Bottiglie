from tkinter import *
from Classe import Bottiglia
from Var import Bottiglie,tipi,get_key,fornitori,campi
import Queryfunctions as Qf
from AutocompletamentoClass import EntryAutocompletamento
campiMenu=""
old_value_text= ""
codice=""
# Scelta tabella-->campo--> Vecchio Valore, nuovo valore
#SELECT TABLE_NAME
#FROM INFORMATION_SCHEMA.TABLES
#WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA='dbName'


#SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='bottiglie';
def Optionmenuselezionato():
    pass

def varcambiata(var,index,mode,my_var,campo):
    global campiMenu,old_value_text,codice
    if my_var.get():
        campiMenu.config(state="normal")
        old_value_text.set(Qf.getcampo(campo.get(),codice.get()))
#Va ma anche no


def lanciafinestra(root):
    global campiMenu,codice,old_value_text
    Qf.getCampi()#bug
    fin_modifica = Toplevel(root)
    fin_modifica.title("Modifica un campo")
    old_value_text=StringVar()
    campo = StringVar()
    new_value_text= StringVar()
    campo.set(campi[0])
    old_value_text.set("...")
    new_value_text.set("...")
    codicetext = Label(fin_modifica,text="Inserisci il codice della bottiglia")
    codice = EntryAutocompletamento(fin_modifica)
    n_Bottiglia = Label(fin_modifica,textvariable=codice.n_Bottiglia_text)
    campotext = Label(fin_modifica,text="Scegli il campo da modificare")
    old_value = Label(fin_modifica,textvariable=old_value_text)
    new_value = Label(fin_modifica,textvariable=new_value_text)
    codice.bind("<KeyRelease>",codice.tastolasciato)
    codice.autocompletato.trace("w",lambda var,index, mode, x=codice.autocompletato,c=campo: varcambiata(var,index,mode,x,c))
    campiMenu = OptionMenu(fin_modifica,campo,*campi,command=Optionmenuselezionato)
    campiMenu.config(state="disabled")

    codicetext.grid(row=0,column=0)
    codice.grid(row=1,column=0)
    n_Bottiglia.grid(row=2,column=0)
    campotext.grid(row=3,column=0)
    campiMenu.grid(row=4,column=0)
    old_value.grid(row=5,column=0)
