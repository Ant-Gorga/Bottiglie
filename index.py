#stavo facendo il datetime
import mysql.connector as mariadb
import platform
import os
import datetime as datetime
if platform.platform() =="Windows":
    clear ="cls"
else:
    print("siamo su un altro sistema")
    clear = "clear"
os.system(clear)
query1 ="""SELECT Cod_Bottiglia, nome, P_vendita, quantita 
        from bottiglie 
        order by P_Vendita
        """
vendita=""" insert into vendite(Data_vendita,quantita,id_bottiglia)
           Values(%s,%s,%s);
        """
vendita_2="""
            update bottiglie set quantita=quantita-%s where Cod_Bottiglia =%s
        """
utente = "antonio"
password ="antonio"
db="test_bottiglie"
Cod_quantita = {}

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
        for cod , nome, prezzo , quantita in cursor:
            print("Codice : {} , Nome : {}, Prezzo : {}€, QTA:{}".format(cod,nome,prezzo,quantita))


    elif scelta == "2":
    
        print("Inserisci I seguenti Dati:")
        print("Lista Bottiglie presenti nel databasse ...")
        cursor.execute("Select Cod_bottiglia, nome, quantita from bottiglie where quantita <> 0")
        for codice, nome, quantita in cursor:
            print("NOME :{}, CODICE :{}, QTA: {}".format(codice,nome,quantita))
            Cod_quantita[codice]=quantita
        
        #Correggere la data
        
        codice_in = ""
        
        while codice_in not in Cod_quantita.keys():
            codice_in = input("inserisci il codice della bottiglia: . . ")
        max_bottiglie = Cod_quantita[codice_in]
        
        while True:
            quantita = int(input("Numero bottiglie vendute (max :"+str(max_bottiglie)+"): "))
            if quantita <= max_bottiglie and quantita > 0:
                break
        oggi = datetime.date.today()
        data = oggi.strftime("%Y%m%d")
        print("Data : "+ data)

        try:
            cursor.execute(vendita,(data,quantita,codice_in))
            cursor.execute(vendita_2,(quantita,codice_in))
            mariadb_connection.commit()
            print("Inserimento avvenuto con successo!")
        except mariadb.Error as error:
            print(format(error))
            print("Errore nell'inserimento della riga, controlla i tipi di dato o il codice della bottiglia")

    elif scelta=="3":
        print("Code2")


    mariadb_connection.close()

except KeyboardInterrupt:
    print("Programma terminato. . . .")
    mariadb_connection.close()