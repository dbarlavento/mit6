#!/usr/local/bin/python3

#ps1b.py
#Calcula os 1000 primeiros números primos, começando em 3, e os relaciona com 
#o produto dos anteriores.

import math

#Constantes
#Primeiro número candidato a primo
INICIO = 3 
#Último número candidato a primo
FIM = 1000000

produto = 0

print("Primo: 2\t\tProduto: 0\t\tRazão: 0")

i = INICIO

#produto dos primos anteriores, o primeiro é 2
produto += math.log(2)

while i <= FIM:
	n = INICIO

	while (i % n != 0) and (n <= i):
		n += 2

	if n == i:
		print("Primo: ",i,"\t\tProduto: ", produto, "\t\tRazão: ", (produto/i))
		produto += math.log(i)

	i += 2

