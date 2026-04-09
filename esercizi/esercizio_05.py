# ==================================================
# ESERCIZIO 5 - Lunghezza delle parole
# ==================================================
# Data la seguente lista di parole:
# parole = ["cane", "sole", "python", "mare"]
#
# Costruisci una nuova lista che contenga la lunghezza
# di ciascuna parola.
#
# Esempio di output:
# [4, 4, 6, 4]
parole = ["cane", "sole", "python", "mare"]
i=0
while i < len(parole):
  nuova_lista=len(parole[i])
  print(nuova_lista)
  i+=1
