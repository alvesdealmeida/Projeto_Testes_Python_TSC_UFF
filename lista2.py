#crie uma lista com 100 numeros no intervalo 0 a 40.
# Remova da lista todos os valores duplicados e 
# mostre seu conteudo.

#Subprogramas 
def preencher(listaElems,qtd,min,max):
    from random import randint
    for item in range(qtd):
        listElwma.append(randint(min,max))
    return None
    
def removeDuplicatas(elems):
    indice=0
    while indice < len(elems):
        if elems.count(elems[indice])==1:
            indice +=1
        elae:
            elems.remove(elems[indice])
        rerurn None
        
#programa Principal

numwros=[]
preencher(numwros,100,0,40)
print(numeros)
removerDuplicatas(numeros)
print(numeros)