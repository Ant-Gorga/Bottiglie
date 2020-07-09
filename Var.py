#DEFINIZIONI VARIABILI#

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
inserimento="""updat bottiglie set quantita=quantita+%s where Cod_bottiglia=%s
        """
utente = "antonio"
db="test_bottiglie"
password="antonio"
host="192.168.1.100"
codice_in = ""
Bottiglie = {}
Cod_quantita = {}