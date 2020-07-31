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
def Optionmenuselezionato(event):
    global  campo,campiMenu,old_value_text,codice
    v1=campo.get()
    v2=codice.get()
    print(v1,v2)
    if (v2 not in Bottiglie.keys()):
        old_value_text.set("Codice Errato")
    else:
        tmp_campo=Qf.getcampo(v1,v2)
        old_value_text.set("Valore: "+str(tmp_campo[0]))

def btn_conferma_cliccato(new_value):
    cmp = campo.get()
    if cmp=="Nome":
        if cmp.isalnum():
            print("ok")

    elif cmp=="Quantita":
        if cmp>=0 and cmp<=99:
            print("ok")
    elif cmp=="P_acquisto":
        if "," in str(cmp):
            cmp = str(cmp).replace(",",".")
        try:
            float(cmp)
            print("ok")
        except ValueError:
            print("No_prezzo")

    elif campo.get()=="P_vendita":
        if "," in str(cmp):
            cmp = str(cmp).replace(",",".")
        try:
            float(cmp)
            print("ok")
        except ValueError:
            print("No_prezzo")
            #inserire il datetimecontrol
    elif campo.get()=="Data_Acqusito":
        pass
    #un elif con il campo.get come stringa
    #Fare il controllo della var
    pass

def varcambiata(var,index,mode,my_var,campo):
    global campiMenu,old_value_text,codice
    if my_var.get():
        campiMenu.config(state="normal")
        print("Qui")
        if(codice.get() not in Bottiglie.keys()):
            old_value_text.set("Codice Errato")
        else:
            tmp_campo= Qf.getcampo(campo.get(),codice.get())
            old_value_text.set("Valore: "+str(tmp_campo[0]))
#Va ma anche no


def lanciafinestra(root):
    global campo,campiMenu,codice,old_value_text
    Campi = ['Nome','Quantita','P_acquisto','P_vendita','Data_Acqusito']
    fin_modifica = Toplevel(root)
    fin_modifica.title("Modifica un campo")
    old_value_text=StringVar()
    campo = StringVar()
    campo.set(Campi[0])
    old_value_text.set(" . . . ")

    codicetext = Label(fin_modifica,text="Inserisci il codice della bottiglia")
    codice = EntryAutocompletamento(fin_modifica)
    campotext = Label(fin_modifica,text="Scegli il campo da modificare")
    old_value = Label(fin_modifica,textvariable=old_value_text)
    new_value = Entry(fin_modifica)
    btn_conferma = Button(fin_modifica,text="Conferma la modifica",command= lambda:btn_conferma_cliccato(new_value.get(),campo.get()))

    codice.bind("<KeyRelease>",codice.tastolasciato)
    codice.autocompletato.trace("w",lambda var,index, mode, x=codice.autocompletato,c=campo: varcambiata(var,index,mode,x,c))
    campiMenu = OptionMenu(fin_modifica,campo,*Campi,command= lambda event :Optionmenuselezionato(event))


    codicetext.grid(row=0,column=0)
    codice.grid(row=1,column=0)
    campotext.grid(row=3,column=0)
    campiMenu.grid(row=4,column=0)
    old_value.grid(row=5,column=0)
    new_value.grid(row=6,column=0)
    btn_conferma.grid(row=7,column=0)
