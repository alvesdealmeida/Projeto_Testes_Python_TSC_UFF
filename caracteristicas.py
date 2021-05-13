#Subprograma

def perfilComum(habitantes, caracteristicas, grupo):
     comuns = caracteristicas
     for ident in range(habitantes):
          if ident in grupo:
               comuns = comuns & habitantes[ident]
     print("As caracteristicas em comuns são:")
     for c in caracteristicas:
          if c in comuns:
               print(c, end="")
     print()
     return None

#Programa Principal

caracteristicas = {"esprotes","tv","cinema","livro","jornal","teatro", "musica"}

alunos = [{"tv","cinema","livro"}, {"cinema", "musica"}, {"cinema","tv","teatro"}]

perfilComun(alunos,caracteristicas, {2,0})