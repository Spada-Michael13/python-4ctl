# ==================================================
# ESERCIZIO 4 - Mini app calcolatrice
# ==================================================
# Realizza una mini applicazione che simuli una calcolatrice.
# Ogni operazione deve essere gestita tramite una funzione.
# Se viene inserito il simbolo /, il programma deve uscire.
def somma(n1,n2):
  return n1+n2
def differenza(n1,n2):
  return n1-n2
def moltiplicazione(n1,n2):
  return n1*n2
def divisione(n1,n2):
  return n1/n2

operazione=input("inserisci l'operatore(+:somma,-:differenza,*:moltiplicazione,d:divisione,/:per uscire)")
while operazione !='/':
  
  n1=int(input("inserisci il primo numero:"))
  
  n2=int(input("inserisci il secondo numero:"))
  match(operazione):
    case '+':
      print(somma(n1,n2))
    case '-':
      print(differenza(n1,n2))
    case '*':
      print(moltiplicazione(n1,n2))
    case 'd':
      print(divisione(n1,n2))
  operazione=input("inserisci l'operatore(+:somma,-:differenza,*:moltiplicazione,d:divisione,/:per uscire)")
  print("sei fuori")
