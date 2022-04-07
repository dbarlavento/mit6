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

#Este executa uma intereação ou laço (loop).
#Uma forma bem ineficiente de calcular o quadrado de um número.
x = 4
y = 0
cont = x
while(cont > 0):
	y = y + x
	cont = cont - 1
print(y)
