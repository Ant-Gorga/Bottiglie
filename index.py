#try except del eyboard interrupt
#stavo facendo il datetime
import mysql.connector as mariadb
import platform
import os
if platform.platform() =="Windows":
    clear ="cls"
else:
    print("siamo su un altro sistema")
    clear = "clear"
    date = """date +\"%Y%m%d\" """
os.system(clear)
query1 ="""SELECT Cod_Bottiglia, nome, P_vendita 
        from bottiglie order 
        by P_Vendita
        """
query2=""" insert into vendite(Data_vendita,quantita,id_bottiglia)
        Values(%s,%s,%s)
        """
utente = "antonio"
password ="antonio"
db="test_bottiglie"


def menu():
    print("COSA VUOI FARE?")
    print("1)Vedi tutte le bottiglie")
    print("2)Registra una vendita")
    print("3)Registra un deposito")
    print("4)Aggiungi una nuova bottiglia")



try:
    scelta = input("Connettersi al database? S-N . . . ")
    if scelta == "n" or scelta == "N":
        print("esco dal programma . . .")
        exit()
    try:
        mariadb_connection = mariadb.connect(user=utente,password=password,database=db)
        cursor = mariadb_connection.cursor()
    except NameError as error:
        print(format(error))

    menu()
    scelta = input("Scelta : ")
    if scelta == "1":
        try:
            cursor.execute(query1)
        except mariadb.Error as error:
            print(format(error))
        for cod , nome, prezzo in cursor:
            print("Codice : {} , Nome : {}, Prezzo : {}€".format(cod,nome,prezzo))


    elif scelta == "2":
    
        print("Inserisci I seguenti Dati:")
        quantita = input("Numero bottiglie vendute: ")
        print("Lista Bottiglie presenti nel databasse ...")
        cursor.execute("Select Cod_bottiglia, nome from bottiglie where quantita <> 0")
    
    
        #Correggere la data
        for codice, nome in cursor:
            print("Codice: " + codice + " Nome: " + nome )
        codice_in = input("inserisci il codice della bottiglia:")
        data  = os.system(date)
        #while codice_in i

        try:
            cursor.execute(query2,(data,quantita,codice_in))
            mariadb_connection.commit()
        
        except mariadb.Error as error:
            print(format(error))
            print("Errore nell'inserimento della riga, controlla i tipi di dato o il codice della bottiglia")

    elif scelta=="3":
        print("Code2")


    mariadb_connection.close()

except KeyboardInterrupt:
    print("Programma terminato. . . .")
    mariadb_connection.close()