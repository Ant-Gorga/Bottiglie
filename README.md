##### 

# Gestire un Piccolo database di bottigie con python3.8 e tkinter

---

Avendo studiato i database da poco ho deciso di provare ad integrarli con python e ad usare per la prima volta tkinter per l' interfaccia grafica.

Per funzionare necessita del file `Credenziali.py` avente la seguente struttura:

```python
utente = "..."
db="..."
password="..."
host="..."

```

Il programma è abbastanza semplice ma mi è stato utile per cominciare a capire il funzionamento della gui, che con tkinter è stata semplice da gestire.

Tutto inizia dall' index, che definisce la struttura della pagina principale e starta la gui con la chiamata alla funzione  `mainloop()`

Qui viene mostrato il menù principale, si avvia la connessione e tramite i pulsanti si raggiunge la funzione desiderata.
