import struct

Aluno = struct.Struct("9s 30s f") # cria Struct com formato do registro

#Subprogramas
def escrever(arq, matricula, nome, cr):
	bloco = Aluno.pack(matricula.encode("utf-8"), nome.encode("utf-8"), cr)
	arq.write(bloco)

def ler(arq):
	bloco = arq.read(Aluno.size)
	campos = Aluno.unpack(bloco)
	return campos[0], campos[1].decode("utf-8").rstrip(chr(0)), campos[2]

#Progrma Principal ou Main

with open("arquivo.bin", "w+b") as arq:
	escrever(arq, "213031001", "Carlos", 9.9)  #chave 0
	escrever(arq, "114032012", "Fernando", 8.9) #chave 1
	escrever(arq, "214031173", "Maia", 7.9) #chave 2
	arq.seek(2 * Aluno.size)
	matricula, nome, cr = ler(arq)
	print("Matricula:", matricula, "Nome:",nome, "CR:", cr)