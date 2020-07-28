from tkinter import *
from Var import Bottiglie

class EntryAutocompletamento(Entry):
    """Classe ereditaria per permettere l' autocompletamento ad Entry."""

    def __init__(self,scope):
        self.testo = StringVar()
        self.n_Bottiglia_text = StringVar()
        self.autocompletato= BooleanVar()
        self.autocompletato.set(False)
        self.codici = list(Bottiglie.keys())
        super().__init__(scope,textvariable=self.testo)

    def confronta_stringa(self):
        tasti = []
        for x in self.codici:
            if x.startswith(self.testo.get()):
                tasti.append(x)
        return tasti

    def mostra_comp(self,lista_da_mostrare):
        if len(lista_da_mostrare)==1:
            self.testo.set(lista_da_mostrare[0])
            self.autocompletato.set(True)
            #Prendo il nome dell' elemento autocompletato
            self.n_Bottiglia_text.set(Bottiglie[lista_da_mostrare[0]].Nome)

    def tastolasciato(self,event):
        if len(event.keysym)==1:
            da_mostrare = self.confronta_stringa()
            self.mostra_comp(da_mostrare)
            self.icursor(END)
