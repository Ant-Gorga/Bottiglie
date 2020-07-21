from Var import *
from Classe import Bottiglia
def conn():

    global mariadb_connection,cursor
    try:
        mariadb_connection = mariadb.connect(user=utente,password=password,host=host,database=db)
        cursor = mariadb_connection.cursor()
    except mariadb.Error as error:
        return error

def getBottiglie():
    global cursor, Bottiglie
    cursor.execute(select_all)
    for Codice,Nome,Quantita,P_acqusito,P_vendita,D_acquisto in cursor:
        Bottiglie[Codice]=Bottiglia(Codice,Nome,Quantita,P_acqusito,P_vendita,D_acquisto)

def insertBottiglia(data,id_tipo,id_fornitore):
    global cursor
    try:
        cursor.execute(aggiunta,(data.Codice,data.Nome,data.Quantita,data.P_acquisto,data.P_vendita,data.Data_Acquisto,id_fornitore,id_tipo))
        mariadb_connection.commit()
        return 0
    except mariadb.Error as error:
        return error

def getTipi():
    global cursor,tipi
    try:
        cursor.execute(SQL_tipi)
        for Id_tipo,Nome in cursor:
            tipi[Id_tipo]=Nome
        return 0
    except mariadb.Error as error:
        return error

def getFornitori():
    global cursor,fornitori
    try:
        cursor.execute(SQL_fornitori)
        for Partita_IVA,Nome in cursor:
            fornitori[Partita_IVA]=Nome
        return 0
    except mariadb.Error as error:
        return error
