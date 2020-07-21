class Bottiglia:
    "Classe che rappresenta la tabella bottiglie nel database"
    righe = 0

    def __init__(self,Codice,Nome,Quantita,P_acquisto,P_vendita,D_acquisto):
        self.Codice = Codice
        self.Nome = Nome
        self.Quantita = Quantita
        self.P_acquisto = P_acquisto
        self.P_vendita= P_vendita
        self.Data_Acquisto = D_acquisto
        Bottiglia.righe +=1


    def stampaBottiglia(self):

        print("codice" +self.Codice+ ", Nome:"+ self.Nome+", Qta: "+str(self.Quantita) +", Prezzo:"+str(self.P_vendita)+"€")
        return ("codice:" +self.Codice+ ", Nome:"+ self.Nome+", Qta: "+str(self.Quantita) +", Prezzo:"+str(self.P_vendita)+"€")

    def controlloValori(self):
        msgErrore ="Perfavore ricontrolla"
        errorList = []
        try:
            int(self.Codice)
        except ValueError:
            msgErrore+=" "+"Ricontrolla il codice"
            errorList.append("Codice")

        self.Nome=self.Nome[0:25]
        try:
            if (int(self.Quantita)> 99 or int(self.Quantita)<1):
                msgErrore+=" "+"Ricontrolla il numero di Bottiglie"
                errorList.append("Quantita")
        except ValueError:
            errorList.append("Quantita")
        try:
            #Cambiare la virgola in punto
            float(self.P_acquisto)
            float(self.P_vendita)
        except ValueError:
            msgErrore+=" "+"Ricontrolla i prezzi"
            errorList.append("P_acquisto")
            errorList.append("P_vendita")
        #Parse datetime non so se metterlo
        return errorList
