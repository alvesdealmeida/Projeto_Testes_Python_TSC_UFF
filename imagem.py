#subprogramas

def cria_matriz(m, n, val):
    matriz = []
    for i in range(m):
        linha = []
        for j in range(n):
            linha.append(val)
        matriz.append(linha)
    return matriz

def grava_PGM(matriz, nomearquivo):
    arquivo = open(nomearquivo, "w")
    arquivo.write("P2\n")
    m = len(matriz)
    n = len(matriz[0])
    arquivo.write("%d %d\n"%(n,m))
    arquivo.write("255\n")
    for i in range(m):
        for j in range(n):
            arquivo.write(" %3d"%(matriz[i][j]))
        arquivo.write("\n")
    arquivo.close()

def desenha_reta(matriz, x1,y1, x2,y2, val):
    if abs(x2-x1) <= 1 and abs(y2-y1) <= 1:
        matriz[int(y1+0.5)][int(x1+0.5)] = val
        matriz[int(y2+0.5)][int(x2+0.5)] = val
    else:
        xm = (x1+x2)/2
        ym = (y1+y2)/2
        desenha_reta(matriz, x1,y1, xm,ym, val)
        desenha_reta(matriz, xm,ym, x2,y2, val)

def main():
    M = cria_matriz(240, 320, 0)
    desenha_reta(M, 20,15, 300,210, 255)
    grava_PGM(M, "reta.pgm")
 
main()