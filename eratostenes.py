#Este programa gera e imprime os numeros primos entre 2 e N, escolhidos
#pelo usuario, usando o algoritmo chamado de Crivo de Estatóstenes.

#Subprogramas
def imprime(num, osPrimos):
     print("Primos entre 2 e", num, ":")
     for candidato in range(2, num + 1):
          if candidato in osPrimos:
               print(candidato, end="")
     print()
     return None

def eratostenes(num):
     resposta = set() # inicializa resposta
     vazio = set()    # inicializa conjunto vazio
     crivo = set(range(2, num +1) # conta conjunto 3 a N.
     prox = 2
     while crivo != vazio:
          while not (prox in crivo):
               prox += 1
          resposta.add(prox)
          j = prox
          while j <= num:
               crivo.discard(j)
               j += prox
     return resposta

#Programa Principal - Crivo de Eratostenes

n = int(input("Digite o valor:")
primos = eratostenes(n)
imprime(n,primos)