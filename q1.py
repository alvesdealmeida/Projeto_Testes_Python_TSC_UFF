#Q1
#subprogramas
def criaArqPts(nome,qtd,min,max):
    from random import randint
    arq = open(nome, "w")
    for pos in range(qtd):
        arq.write(str(randint(min,max))+""+str(randint(min,max))+"\n")
    arq.close()
    return None
def mostra(nome):
    arq = open(nome,"r")
    for pt in arq:
        print(pt, end="")
    arq.close()
    return None
#Program Principal (ou Main) - aqui sera criando e mostrado o arquivo 2D
criaArqPts("pontos.txt", 30,0,40)
mostra("pontos.txt")
