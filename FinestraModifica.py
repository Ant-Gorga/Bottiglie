from tkinter import *
from Classe import Bottiglia
from Var import Bottiglie, tipi, get_key, fornitori, campi
import Queryfunctions as Qf
from AutocompletamentoClass import EntryAutocompletamento
from datetime import datetime, date
class Errore(Exception): pass

campiMenu = ""
old_value_text = ""
codice = ""
campo = ""


# Scelta tabella-->campo--> Vecchio Valore, nuovo valore
# SELECT TABLE_NAME
# FROM INFORMATION_SCHEMA.TABLES
# WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA='dbName'


# SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='bottiglie';
def Optionmenuselezionato(event):
    global campo, campiMenu, old_value_text, codice
    v1 = campo.get()
    v2 = codice.get()
    print(v1, v2)
    if v2 not in Bottiglie.keys():
        old_value_text.set("Codice Errato")
    else:
        tmp_campo = Qf.getcampo(v1, v2)
        old_value_text.set("Valore: " + str(tmp_campo[0]))


def btn_conferma_cliccato(new_value):
    cmp = campo.get()
    try:
        if cmp == "Nome":
            if  not new_value.isprintable():
                raise Errore
        elif cmp == "Quantita":
            if new_value <= 0 and new_value >= 99:
                raise Errore

        elif cmp == "P_acquisto":
            if "," in str(new_value):
                new_value = str(new_value).replace(",", ".")
            try:
                float(new_value)
            except ValueError:
                raise Errore

        elif new_value == "P_vendita":
            if "," in str(new_value):
                new_value = str(new_value).replace(",", ".")
            try:
                float(new_value)
            except ValueError:
                raise Errore
            # inserire il datetimecontrol
        elif cmp == "Data_Acqusito":
            mindata = datetime.strptime("12-08-2020","%d-%m-%Y")
            new_value = datetime(new_value,"%d-%m-%Y")
            if new_value < mindata or new_value > date.today():
                raise Errore
        print(Qf.modifcacampo(codice.get(), cmp, new_value))
        Qf.getBottiglie()
        print("IO ci arrivo qua, ma poi boh")

    except Errore:
        print("Errore inaspettato")
        #Riportare un errore

    # un elif con il campo.get come stringa
    
    


def varcambiata(var, index, mode, my_var, campo):
    global campiMenu, old_value_text, codice
    if my_var.get():
        campiMenu.config(state="normal")
        print("Qui")
        if (codice.get() not in Bottiglie.keys()):
            old_value_text.set("Codice Errato")
        else:
            tmp_campo = Qf.getcampo(campo.get(), codice.get())
            old_value_text.set("Valore: " + str(tmp_campo[0]))


# Va ma anche no


def lanciafinestra(root):
    global campo, campiMenu, codice, old_value_text
    Campi = ['Nome', 'Quantita', 'P_acquisto', 'P_vendita', 'Data_Acqusito']
    fin_modifica = Toplevel(root)
    fin_modifica.title("Modifica un campo")
    old_value_text = StringVar()
    campo = StringVar()
    campo.set(Campi[0])
    old_value_text.set(" . . . ")

    codicetext = Label(fin_modifica, text="Inserisci il codice della bottiglia")
    codice = EntryAutocompletamento(fin_modifica)
    campotext = Label(fin_modifica, text="Scegli il campo da modificare")
    old_value = Label(fin_modifica, textvariable=old_value_text)
    new_value = Entry(fin_modifica)
    btn_conferma = Button(fin_modifica, text="Conferma la modifica",
                          command=lambda: btn_conferma_cliccato(new_value.get()))

    codice.bind("<KeyRelease>", codice.tastolasciato)
    codice.autocompletato.trace("w",
                                lambda var, index, mode, x=codice.autocompletato, c=campo: varcambiata(var, index, mode,
                                                                                                       x, c))
    campiMenu = OptionMenu(fin_modifica, campo, *Campi, command=lambda event: Optionmenuselezionato(event))

    codicetext.grid(row=0, column=0)
    codice.grid(row=1, column=0)
    campotext.grid(row=3, column=0)
    campiMenu.grid(row=4, column=0)
    old_value.grid(row=5, column=0)
    new_value.grid(row=6, column=0)
    btn_conferma.grid(row=7, column=0)
