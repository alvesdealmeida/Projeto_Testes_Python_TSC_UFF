#Q5
# Subprogramas 
def mostrar(prods): 
	for chave, valor in sorted(prods.items()): 
		print(chave, "-", valor) 
	return None 
def preencher(prods, entradas): 
	for i in range(entradas): 
		cod = input("Codigo:") 
		desc = input("Descricao:") 
		qtd = int(input("Quantidade:")) 
		preco = float(input("Valor: ")) 
		data = input("Limite de Validade - dd/mm/aa: ") 
		partes = data.split("/") 
		prods[cod] = [desc, qtd, preco, (int(partes[0]),int(partes[1]), int(partes[2]))] 
	return None 
def vender(prods, codsQtds): 
	return None 

# Programa Principal 
produtos = { } 
preencher(produtos, 5) 
mostrar(produtos) 
vender(produtos, {"xkk":3, "yzb":2}) 
mostrar(produtos)