#Q3
#Subprogramas

def contaVogaisDigitos(frase):
    vogais = {"A","E","I","O","U", "a","e","i","o","u"}
    digitos = {"0","1","2","3","4","5","6","7","8","9"}
    nVogais = 0
    nDigitos = 0
    for letra in frase:
        if letra in vogais:
           nVogais +=1
        elif letra in digitos:
           nDigitos +=1
    print("Quantidade de Vogais:", nVogais)
    print("Quantidade de Digitos:", nDigitos)
    return None

#Programa Principal ou Main
lida = input("Digite a frase:")
contaVogaisDigitos(lida)
       