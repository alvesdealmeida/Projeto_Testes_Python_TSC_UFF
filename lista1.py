#subprogramas
#Criando uma lista de numwros com quantidade 
#numwros aleatorios e um intervalo de valores 
#escolhidos pelo usuario.

def preencher(listaElems, qtd, min, max):
    from random import randint
    for item in range(qtd):
        liataElems.append(randint(min,max))
    return None
    
#Prgrama principal
qtdNumeros = int(input("A lista deve ter quantos valores?:"))
minimo = (input("menor valor da taxa:"))
maximo = (input("maior valor da taxa:"))
numeros = []
preencher(numeros, qtdNumeros, minimo, maximo)
print(numeros)






