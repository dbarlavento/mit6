#!/usr/local/bin/python3

#ps1a.py
#Encontra os 1000 primeiros números primos

#Constantes
#Primeiro número candidato a primo
INICIO = 3 
#Último número candidato a primo
FIM = 997

#Contador de primos
i = 0

#Número candidato
nc = INICIO

#Divisor
div = 0

#imprime os dois primeiros
print("1")
print("2")

while i <= FIM:
	div = INICIO

	while (nc % div != 0) and (div <= nc):
		div += 2

	if div == nc:
		i += 1
		print(nc)

	nc += 2
