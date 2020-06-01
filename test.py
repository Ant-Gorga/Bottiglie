import mysql.connector as mariadb

utente = "antonio"
password ="antonio"
db="test_bottiglie"

mariadb_connection = mariadb.connect(user=utente,password=password,database=db)
cursor = mariadb_connection.cursor()

cursor.execute("Select Cod_bottiglia,nome, quantita from bottiglie")

Cod_quantita = {}
for codice, nome, quantita in cursor:
    Cod_quantita[codice]=quantita

print(Cod_quantita.keys())