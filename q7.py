#q7
import struct
TAM = 43   #constante definindo o tamanho do registro em bytes
#Subprogramas

def escrever(arq, matricula, nome, cr):
	arq.write(matricula.encode("utf-8"))
	arq.write(nome[:30].ljust(30, chr(0)).encode("utf-8"))
	arq.write(struct.pack("f",cr))

def ler(arq):

	matricula =arq.read(9).decode("utf-8")
	nome = arq.read(30).decode("utf-8").rstrip(chr(0))
	cr = struct.unpack("f", arq.read(4))[0]
	return matricula,nome,cr

#Programa Principal
with open("arquivo.bin", "w+b") as arq:
	escrever(arq, "123456789","Carlos",10.0) #chave 0
	escrever(arq, "123456780","Fernando", 9.0) #chave 1
	escrever(arq, "123456700","Maia", 8.0) #chave 2

	arq.seek(2*TAM)
	matricula, nome, cr = ler(arq)
	print("Matricula:", matricula, "Nome:", nome, "CR:", cr)
