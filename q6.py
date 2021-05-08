#q6
#Subprogramas

def mostra(vs):                             # exibe a matriz organizada
	qtdLinhas = vs["Numero de Linhas"]
	qtdColunas = vs["Numero de Colunas"]
	for linha in range(qtdLinhas):	
		for coluna in range(qtdColunas):
			valor = vs.get((linha,coluna),0)
			print("%4d"%valor, end="") # saida formatada  4 espacos
		print()                            # pula para a proxima linha
	return 

#Programa Principal ou Main
#valores mantem apenas as dimensoes e os poucos numeros diferentes de zero

valores = {}
valores["Numeros de Linhas"]=5 # chave string mantem a quantidade de linhas
valores["Numeros de Colunas"]=10 # chave string mantem a quantidade de colunas
valores[(1,1)]=13 # chave tupla(1,1) com vlaor nao zero
valores[(0,8)]=-4 # chave tupla(0,8) com um valor nao zero
valores[(4,7)]=75 # chave tupla(4,7) com um valor nao zero
print(valores)
mostra(valores)

