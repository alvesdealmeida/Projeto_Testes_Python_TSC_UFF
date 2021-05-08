import struct

#Subprogramas para leitura dos n primeiros valores inteiros

def mostrarOsNPrimeirosValores(arq,n):
	print("Os primeiros valores contidos no arquivo sao:")
	arq.seek(0)
	for k in range(0, n):
		print(struct.unpack("i", arq.read(4)) [0])

#Programa Principal ou Main

try:
	with open("arquivo.bin", "w+b") as arq:
		print("Escrever os valores inteiros de 1 a 5 no arquivo")
		for x in range(1,6):
			arq.write(struct.pack("i", x))
		mostrarOsNPrimeirosValores(arq,5)
		print("Substituir o segundo valor contido no arquivo pr 99")
		arq.seek(4)
		arq.write(struct.pack("i", 99))
		mostrarOsNPrimeirosValores(arq,5)
except IOError:
	print("Erro ao abrir ou ao manipular o arquivo.")
