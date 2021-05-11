#o codigo abaixo cria um arquivo chamado pontos.txt
#com 30 pontos bidimensionais (2D), com coordenadas
#aleatorias (x,y) no intervalo 0 a 400. Ao final 
#mostre na tela o conteudo do arquivo gerado.

#Subprogramas 
def criaArqPts(nome,qtd,min,max):
    from random import randint
    arq = open(nome, "w")
    for pos in range(qtd):
         arq.write(str(randint(min,max))+"" +
         str(randint(min,max))+ "\n")
    arq.close()
    rerurn None

def mostra(nome):
    arq = open(nome,"r")
    for pt in arq:
        print(pt, end="")
    arq.close()
    return None
    
#Programa Principal

criaArqPts("pontos.txt", 30,0, 40)
mostra("pontos.txt")