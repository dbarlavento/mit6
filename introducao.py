#Programa introdutório às estruturas básicas de Python.

#Devlara e atribui um valor as variáveis.
x = 3
y = 4

#Estrutura condicional. 
#Inicia com ":" e termina com a proxima linha não identada.
#A identação é importante!
#Este verifica se x e y são impar ou par.
#if (x % 2) == 0:
#	print('x é par')
#else:
#	print('x é impar')
#
#if (y % 2) == 0:
#	print('y é par')
#else:
#	print('y é impar')

#Este verifica qual dos três é o menor
#z = 7 #podemos declarar variáveis onde quisermos!
##introdução do operador lógico AND.
#if x < y and x < z: 
#	print('x é o menor')
#elif y < z:
#	print('y é o menor')
#else:
#	print('z é o menor')

#Este executa uma intereação ou laço usando o comando "while".
#Uma forma bem ineficiente de calcular o quadrado de um número.
#x = 4
#y = 0
#cont = x
#while(cont > 0):
#	y = y + x
#	cont = cont - 1
#print(y)

#Este executa uma interação (loop) utilizando o comando "for".
#Este verifica todos os divisores de x e os imprime na tela.
#Utilizaremos a função "range()" para retornar os valores entre 1 e x.
#x = 10
#for i in range(1,x):
#	if x % i == 0:
#		print(i, " é divisor de ", x)

#Este verifica os divisores de x, os coloca em uma tupla e os imprime.
#x = 100
#divisores = ()
#for i in range(1, x):
#	if x % i == 0:
#		divisores = divisores + (i,)
#
#print("divisores de ", x, ": ", divisores)

#Strings também são coleções. Elas possuem prorpriedades e funções
#semelhantes as coleções.
#texto1 = "abcde"
#texto2 = "fghij"
#
#texto3 = texto1 + texto2
#
#print(texto1[0:3])
#print(texto2[3:5])
#print(texto3)


#Este soma os digitos de um número.
#Usadas as funções str() e int para converter números em texto e vice versa.
num = 1987
somDigitos = 0

for c in str(num):
	somDigitos += int(c)

print(somDigitos)
