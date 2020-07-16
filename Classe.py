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
            print("codice :" +self.Codice+ ", Nome:"+ self.Nome+", Qta: "+str(self.Qauantita) +", Prezzo:"+str(self.P_vendita)+"€")

            return("codice :" +self.Codice+ ", Nome:"+ self.Nome)
