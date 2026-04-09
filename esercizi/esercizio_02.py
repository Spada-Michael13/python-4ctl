# ==================================================
# ESERCIZIO 2 - Somma degli elementi di una lista
# ==================================================
# Data la seguente lista di numeri:
# numeri = [4, 7, 2, 9, 1]
#
# calcola e stampa la somma di tutti gli elementi
# utilizzando sia il costrutto for sia il costrutto while.
numeri = [4, 7, 2, 9, 1]
somma_for=0
for i in numeri:
  somma_for+=i
print(f"calcolo con il for:{somma_for}")
i=0
somma_while=0
while i<len(numeri):
  somma_while+=numeri[i]
print(f"calcolo con il while:{somma_while}")
