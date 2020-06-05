from Var import *
import mysql.connector as mariadb
mariadb_connection = mariadb.connect(user=utente,password=password,database=db)
cursor = mariadb_connection.cursor()
class Found(Exception): pass


class Bottiglia:
    "Classe che rappresenta la tabella bottiglie nel database"
    righe = 0
    
    def __init__(self,Codice,Nome,Quantita,P_acqusito,P_vendita,D_acquisto):
        self.Codice = Codice
        self.Nome = Nome
        self.Qauantita = Quantita 
        self.P_acqusito = P_acqusito
        self.P_vendita= P_vendita
        self.Data_Acquisto = D_acquisto
        Bottiglia.righe +=1 

    def stampaBottiglia(self):
        print("codice :" +self.Codice+ ", Nome:"+ self.Nome)
    
    def controlloCodice(self,cod):
        if cod == self.Codice:
            return True

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
while True:
    try:
        codice=input("inserisci un codice corretto")
        print(Bottiglie[codice].Nome)
        break
    except KeyError:
        print("Codice errato")

print("DISPONIBILITA ="+str(Bottiglie["80220718"].Qauantita))
#implementare i controlli come funzioni nella classe