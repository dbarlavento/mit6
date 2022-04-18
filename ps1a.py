#!/usr/local/bin/python3

#ps1a.py
#Calcula os 1000 primeiros números primos

#Constantes
#Primeiro número candidato a primo
INICIO = 3 
#Último número candidato a primo
FIM = 1000000

i = INICIO
resto = 0

#imprime os dois primeiros
print("1")
print("2")

for i in range(INICIO, FIM):
	if i % 2 != 0:
		n = 3
		while (i % n != 0) and (n <= i):
			n += 2
		if n == i:
			print(n)

