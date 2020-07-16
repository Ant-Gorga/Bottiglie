from Var import *
import mysql.connector as mariadb
from Classe import Bottiglia
mariadb_connection = mariadb.connect(user=utente,password=password,database=db,host=host)
cursor = mariadb_connection.cursor()
class Found(Exception): pass
var= 0

cursor.execute("SELECT Cod_Bottiglia, nome, quantita ,P_acquisto, P_vendita, Data_Acqusito from bottiglie order by P_Vendita")

Bottiglie = {}
for Codice,Nome,Quantita,P_acqusito,P_vendita,D_acquisto in cursor:
    Bottiglie[Codice]=Bottiglia(Codice,Nome,Quantita,P_acqusito,P_vendita,D_acquisto)

for b in Bottiglie.values():
    b.stampaBottiglia()

def codice():
    try:
        while True:
            codice = input("Inserisci il codice della bottiglia")
            for b in Bottiglie.values():
                if b.controlloCodice(codice):
                    raise Found
    except Found:
        print("Controllo effettuato")
# while True:
#     try:
#         codice=input("inserisci un codice corretto")
#         print(Bottiglie[codice].Nome)
#         break
#     except KeyError:
#         print("Codice errato")

def restbottiglie():
    cursor.execute("SELECT Cod_Bottiglia, nome, quantita ,P_acquisto, P_vendita, Data_Acqusito from bottiglie order by P_Vendita")
    Bottiglie = {}
    for Codice,Nome,Quantita,P_acqusito,P_vendita,D_acquisto in cursor:
        Bottiglie[Codice]=Bottiglia(Codice,Nome,Quantita,P_acqusito,P_vendita,D_acquisto)
    return Bottiglie
