# Quando si inserisce si deve fare il commit
#Quando si legge non è necessario

import mysql.connector as mariadb
import platform
import os
import datetime as datetime
from Var import *
from Classe import Bottiglia
if platform.platform() =="Windows":
    clear ="cls"
else:
    print("siamo su un altro sistema")
    clear = "clear"

class Found(Exception): pass #Eccezione creata per uscire dal ciclo annidiato

os.system(clear)

def menu():
    print("COSA VUOI FARE?")
    print("1)Vedi tutte le bottiglie")
    print("2)Registra una vendita")
    print("3)Registra un deposito")
    print("4)Aggiungi una nuova bottiglia")



menu()
try:
    scelta = input("Connettersi al database? S-N . . . ")
    if scelta == "n" or scelta == "N":
        print("esco dal programma . . .")
        exit()
    try:
        mariadb_connection = mariadb.connect(user=utente,password=password,host=host,database=db)
        cursor = mariadb_connection.cursor()
    except NameError as error:
        print(format(error))

    cursor.execute("SELECT Cod_Bottiglia, nome, quantita ,P_acquisto, P_vendita, Data_Acqusito from bottiglie order by P_Vendita")


    for Codice,Nome,Quantita,P_acqusito,P_vendita,D_acquisto in cursor:
        Bottiglie[Codice]=Bottiglia(Codice,Nome,Quantita,P_acqusito,P_vendita,D_acquisto)
    menu()

    scelta = input("Scelta : ")
    if scelta == "1":
        try:
            cursor.execute(select_all)
        except mariadb.Error as error:
            print(format(error))
        for b in Bottiglie.values():
            b.stampaBottiglia()

    elif scelta == "2":
        #semicompleto controllare e sistemare il codice :)
        print("Inserisci I seguenti Dati:")

        print("Lista Bottiglie disponibili alla vendita ...")
        cursor.execute("Select Cod_bottiglia, nome, quantita from bottiglie where quantita <> 0")
        for codice, nome, quantita in cursor:
            print("NOME :{}, CODICE :{}, QTA: {}".format(codice,nome,quantita))
            Cod_quantita[codice]=quantita



        while codice_in not in Bottiglie.keys():
            codice_in = input("inserisci il codice della bottiglia: . . . ")
        max_bottiglie = Bottiglie[codice_in].Qauantita

        while True:
            try:
                quantita = int(input("Numero bottiglie vendute (max :"+str(max_bottiglie)+"): "))
            except ValueError:
                print("Errore, hai inserito un carattere non valido, inserisco 1 bottiglia")
                quantita=1

            if quantita <= max_bottiglie and quantita > 0:
                break
        oggi = datetime.date.today()
        data = oggi.strftime("%Y%m%d") #Formattazione data come piace a mysql
        try:
            cursor.execute(vendita,(data,quantita,codice_in))
            cursor.execute(vendita_2,(quantita,codice_in))
            mariadb_connection.commit()
            print("Inserimento avvenuto con successo!")
        except mariadb.Error as error:
            print(format(error))
            print("Errore nell'inserimento della riga, controlla i tipi di dato o il codice della bottiglia")

    elif scelta=="3":
        while codice_in not in Bottiglie.keys():
            codice_in = input("inserisci il codice della bottiglia: . . . ")
            try:
                quantita = int(input("Numero delle bottiglie da inserire:..."))
            except ValueError:
                print("Errore, hai inserito un carattere non valido, inserisco 1 bottiglia")
                quantita=1
        try:
            cursor.execute(inserimento,(quantita,codice_in))
            cursor.commit()
        except mariadb.Error as error:
            print(format(error))
            print("Errore nell'inserimento della riga, controlla i tipi di dato o il codice della bottiglia")


    elif scelta =="4":
        #quarto csaoù
        print("Non so se implementarlo o meno")
    mariadb_connection.close()

except KeyboardInterrupt:
    print("Programma terminato. . . .")
    mariadb_connection.close()
