from tkinter import *
from Classe import Bottiglia
from Var import Bottiglie,tipi,get_key,fornitori,campi
import Queryfunctions as Qf
from AutocompletamentoClass import EntryAutocompletamento
campiMenu=""
old_value_text= ""
codice=""
campo =""
# Scelta tabella-->campo--> Vecchio Valore, nuovo valore
#SELECT TABLE_NAME
#FROM INFORMATION_SCHEMA.TABLES
#WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA='dbName'


#SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='bottiglie';
def Optionmenuselezionato():
    global  campo,campiMenu,old_value_text,codice
    v1=campo.get()
    v2=codice.get()
    tmp_campo=Qf.getcampo(v1,v2)
    old_value_text.set(tmp_campo)

def varcambiata(var,index,mode,my_var,campo):
    global campiMenu,old_value_text,codice
    if my_var.get():
        campiMenu.config(state="normal")
        print(campo.get())
        tmp_campo= Qf.getcampo(campo.get(),codice.get())
        old_value_text.set(tmp_campo)
#Va ma anche no


def lanciafinestra(root):
    global campo,campiMenu,codice,old_value_text
    Campi = ['Nome','Quantita','P_acquisto','P_vendita','Data_Acqusito']
    fin_modifica = Toplevel(root)
    fin_modifica.title("Modifica un campo")
    old_value_text=StringVar()
    campo = StringVar()
    campo.set(Campi[0])
    old_value_text.set("...")

    codicetext = Label(fin_modifica,text="Inserisci il codice della bottiglia")
    codice = EntryAutocompletamento(fin_modifica)
    n_Bottiglia = Label(fin_modifica,textvariable=codice.n_Bottiglia_text)
    campotext = Label(fin_modifica,text="Scegli il campo da modificare")
    old_value = Label(fin_modifica,textvariable=old_value_text)

    codice.bind("<KeyRelease>",codice.tastolasciato)
    codice.autocompletato.trace("w",lambda var,index, mode, x=codice.autocompletato,c=campo: varcambiata(var,index,mode,x,c))
    campiMenu = OptionMenu(fin_modifica,campo,*Campi,command=Optionmenuselezionato())
    campiMenu.config(state="disabled")

    codicetext.grid(row=0,column=0)
    codice.grid(row=1,column=0)
    n_Bottiglia.grid(row=2,column=0)
    campotext.grid(row=3,column=0)
    campiMenu.grid(row=4,column=0)
    old_value.grid(row=5,column=0)
