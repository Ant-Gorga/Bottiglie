#DEFINIZIONI VARIABILI#
import mysql.connector as mariadb
from Credenziali import *
select_all ="""SELECT Cod_Bottiglia, nome, quantita ,P_acquisto, P_vendita, Data_Acqusito
            from bottiglie
            order by P_Vendita
        """

SQL_vendita="""
            update bottiglie set quantita=quantita-%s where Cod_bottiglia =%s
        """
SQL_deposito="""
            update bottiglie set quantita=quantita+%s where Cod_Bottiglia=%s
        """

SQL_vendita="""update bottiglie set quantita=quantita-%s where Cod_bottiglia=%s
        """

aggiunta="""insert into bottiglie
            values(%s,%s,%s,%s,%s,%s,%s,%s)"""
SQL_tipi=""" select * from tipi
     """
SQL_fornitori="""select Partita_IVA,Nome from foritori"""

SQL_colonne=""" select column_name
                from INFORMATION_SCHEMA.COLUMNS
                WHERE TABLE_NAME='%s' """
codice_in = ""
Bottiglie = {}
Cod_quantita = {}
tipi={}
fornitori = {}
campi=[]
mariadb_connection = ""
cursor = ""

#Funzione per prendere il valore della chiave dall' elemento
def get_key(my_dict,val):
    for key, value in my_dict.items():
         if val == value:
             return key
