#!/usr/local/bin/python3

#ps0.py
#A primeira linha torna possível executar o programa diretamente sem digitar
#explicitamente o "python3" no shell. Também é necessário tornar o arquivo
#executável: "chmod +x 'nomeDoArquivo'".
#Este programa solicita o primeiro e o último nome do usuário e o imprime
#como uma única string.

#A função input necessita de um parâmetro
nome1 = input("Digite seu primeiro nome: ")
nome2 = input("Digite seu último nome: ")

print(nome1 + " " + nome2)
