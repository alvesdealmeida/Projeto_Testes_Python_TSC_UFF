#o programa abaixo faz a leitura de cinco nomes e telefones e cria um dicionario com ate
#nomes distintos digitados pelo usuario. Ocorre um a escrita do conteudo do dicionario
#a cada tentativa de inclusao de nome e fone.

pares = dict()
for i in range(5):
     nome = input("Digite o nome:")
     fone = input("Digite o fone de " +nome+ ":")
     pares[nome] = fone
     print(pares)