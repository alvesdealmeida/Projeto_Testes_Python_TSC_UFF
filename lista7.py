#Programa que imprime o numero de vogais e digitos 
#existentes em uma frase.

#Subprogramas

def contaVogaisDigitos(frase):
    vogais= {"A","E","I","O","U","a,"e","i","o","u"}
    digitos={"0","1","2","3","4","5","6","7","8","9"}
    nVogais=0 
    nDigitos=0
    
    for letra in frase:
        if letra in vogais:
            nVogais += 1
        elif letra in digitos:
            nDigitos += 1
        print("Quantidade de vogais:",nVogais)
        print("Quantidade de digitos:",nDigitos)
        
#Programa Principal

lida = input("dogite a frase:")
contaVogaisDigitos(lida)