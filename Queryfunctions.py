from Var import *
from Classe import Bottiglia
from Credenziali import *


def conn():
    global mariadb_connection, cursor
    try:
        mariadb_connection = mariadb.connect(user=utente, password=password, host=host, database=db)
    except  mariadb.Error as error:
        return error
    if mariadb_connection.is_connected():
        cursor = mariadb_connection.cursor()
        return 0
    else:
        return "Errore di connessione"


def getBottiglie():
    global cursor, Bottiglie
    cursor.execute(select_all)
    for Codice, Nome, Quantita, P_acqusito, P_vendita, D_acquisto in cursor:
        Bottiglie[Codice] = Bottiglia(Codice, Nome, Quantita, P_acqusito, P_vendita, D_acquisto)


def insertBottiglia(data, id_tipo, id_fornitore):
    global cursor
    try:
        cursor.execute(aggiunta, (
            data.Codice, data.Nome, data.Quantita, data.P_acquisto, data.P_vendita, data.Data_Acquisto, id_fornitore,
            id_tipo))
        mariadb_connection.commit()
        return 0
    except mariadb.Error as error:
        return error


def getTipi():
    global cursor, tipi
    try:
        cursor.execute(SQL_tipi)
        for Id_tipo, Nome in cursor:
            tipi[Id_tipo] = Nome
        return 0
    except mariadb.Error as error:
        return error


def getFornitori():
    global cursor, fornitori
    try:
        cursor.execute(SQL_fornitori)
        for Partita_IVA, Nome in cursor:
            fornitori[Partita_IVA] = Nome
        return 0
    except mariadb.Error as error:
        return error


def deposito(codice, num):
    global cursor
    try:
        cursor.execute(SQL_deposito, (num, codice))
        mariadb_connection.commit()
        return 0
    except mariadb.Error as error:
        return error


def vendita(codice, num):
    global cursor
    try:
        cursor.execute(SQL_vendita, (num, codice))
        mariadb_connection.commit()
        return 0
    except mariadb.Error as error:
        return error


def getCampi():
    global cursor, campi
    try:
        cursor.execute(SQL_colonne)  # bug
        for column_name in cursor:
            campi.append(list(column_name))
        campi.pop(0)  # toglie la chiave primaria
        for x in campi:
            x[0] = x[0].replace("'", "")
        print(campi)
        return 0
    except mariadb.Error as error:
        return error


def getcampo(campo, cod):
    try:
        SQL_gut_campo = """Select """ + campo + """ from bottiglie where cod_bottiglia={}""".format(cod)
        cursor.execute(str(SQL_gut_campo))
        for campo in cursor:
            value = campo
        print(cursor.statement)
        return value
    except mariadb.Error as error:
        return error


def modifcacampo(cod, cmp, new_value):
    try:
        tmp_SQL = SQL_modifica_campo.replace("#", cmp)
        cursor.execute(tmp_SQL, (new_value, cod))
        mariadb_connection.commit()
        return 0
    except mariadb.Error as Error:
        return Error
