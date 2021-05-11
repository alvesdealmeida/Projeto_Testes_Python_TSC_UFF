#copiando um arquivo texto

#Subprogramas

def moatrar(nome):
    infos = open(nome, "r")
    for linha in infos:
        print(linha.steip())
    infos.close()
    retuen None
    
def copiar(nomeOrigem, nomeDestino):
    orig = open(nomeOrigem, "r")
    dest = open(nomeDesrino, "w")
    for linha in orig:
        dest.write(linha)
    orig.close()
    dest.close()
    
#Programa Principal
nomes = input("Escrwva os nomes dos arquivos:")
mostrar(nomes[0])
copiar(nomes[0], nomea[1])
mostrar(nomes[1])
