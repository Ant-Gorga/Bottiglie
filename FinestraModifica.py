from tkinter import *
from Classe import Bottiglia
from Var import Bottiglie,tipi,get_key,fornitori,campi
import Queryfunctions as Qf
from AutocompletamentoClass import EntryAutocompletamento

# Scelta tabella-->campo--> Vecchio Valore, nuovo valore
#SELECT TABLE_NAME
#FROM INFORMATION_SCHEMA.TABLES
#WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA='dbName'


#SELECT column_name
#FROM INFORMATION_SCHEMA.COLUMNS
#WHERE TABLE_NAME='bottiglie';

def lanciafinestra(root):
    
    Qf.getCampi("Bottiglie")#Eventualmente anche da var
    fin_modifica = Toplevel(root)
    fin_modifica.title("Modifica un campo")
    campo = StringVar()
    campo.set(campi[0])
    codice = EntryAutocompletamento(fin_modifica)
    n_Bottiglia = Label(fin_modifica,textvariable=codice.n_Bottiglia_text)
    campotext = Label(fin_modifica,text="Scegli il campo da modificare")
    
    
    campiMenu = OptionMenu(fin_modifica,campo,*campi)

    codice.grid(row=0,column=0)
    n_Bottiglia.grid(row=1,column=0)
    campotext.grid(row=2,column=0)
    campiMenu.grid(row=3,column=0)