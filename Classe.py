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
            print("codice" +self.Codice+ ", Nome:"+ self.Nome+", Qta: "+str(self.Qauantita) +", Prezzo:"+str(self.P_vendita)+"€")
            return("codice :" +self.Codice+ ", Nome:"+ self.Nome)

        def controlloValori(self):
            msgErrore ="Perfavore ricontrolla"
            errorList = []
            try:
                int(self.Codice)
            except ValueError:
                msgErrore+=" "+"Ricontrolla il codice"
                errorList.append(0)

            self.Nome=self.Nome[0:25]

            if (self.Quantita> 99 or self.Quantita<1):
                msgErrore+=" "+"Ricontrolla il numero di Bottiglie"
                errorList.append(2)
            try:
                float(self.P_acquisto)
                float(self.P_vendita)
            except ValueError:
                msgErrore+=" "+"Ricontrolla i prezzi"
                errorList.append(3)
                errorList.append(4)
            #Parse datetime non so se metterlo
