#Q4
#Subprogramas

def imprime(num,osPrimos):
    return None
def eratostenes(num):
    resposta = set() # inicializa resposta
    vazio = set()    #inicializa comjunto vazio
    crivo = set(range(2, num+1) # constroi connjunto 2...
    prox = 2
    while crivo != vazio:
        while not (prox in crivo):
            prox +=1
        resposta.add(prox) # ou resposta {prox}
        j = prox
        while j <= num:
            crivo.discard(j) # ou crivo - {j}
            j += prox
    return resposta

#Programa Principal - Crivo de Erastostenes
n = int(input("Diga o valor:"))
primos = eratostenes(n)
imprime (n,primos)
