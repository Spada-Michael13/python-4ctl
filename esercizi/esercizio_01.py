# ==================================================
# ESERCIZIO 1 - Maggiore tra due numeri
# ==================================================
# Chiedi all'utente di inserire due numeri.
# Stampa quale dei due numeri è il maggiore.
# Se i due numeri sono uguali, segnalalo chiaramente.
#
# Esempi:
# - Il numero maggiore è 8
# - I due numeri sono uguali
n1=int(input("inserisci il primo numero"))
n2=int(input("inserisci il secondo numero"))
if n1>n2:
  print(f"il valore maggiore è:{n1}")
elif n1<n2:
  print(f"il valore maggiore è:{n2}")
else:
  print("i valori sono uguali")
