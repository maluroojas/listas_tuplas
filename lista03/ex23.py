nomes = ["Ana", "João", "Ana", "Maria", "João", "Pedro"]
unicos = []
for nome in nomes:
    if nome not in unicos:
        unicos.append(nome)
print(unicos)
