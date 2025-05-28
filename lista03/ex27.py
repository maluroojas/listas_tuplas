pilha = []

# Empilhando elementos
pilha.append(1)
print("Pilha após append 1:", pilha)

pilha.append(2)
print("Pilha após append 2:", pilha)

pilha.append(3)
print("Pilha após append 3:", pilha)

# Desempilhando elementos
item = pilha.pop()
print("Pilha após pop:", pilha, "| Item removido:", item)

item = pilha.pop()
print("Pilha após pop:", pilha, "| Item removido:", item)
