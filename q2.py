#Q2
#Subprogramas

def centroide(nome):
    arquivo = open(nome, "r")
    qtdPts = 0
    somaX = 0
    somaY = 0
    for coordenada in arquivo:
        partes = coordenada.split()
        somaX += float(partes[0])
        somaY += float(partes[1])
        qtdPts += 1
    arquivo.close()
    if qtdPts == 0:
        print(arquivo.name, "-vazio!!")
    else:
        print("Ponto calculado: (", somaX/qtdPts,",", somaY/qtdPts,")")
    return None
#Programa Principal ou Main - calcula e escreve o centroide de pontos.
centroide("pontos.txt")