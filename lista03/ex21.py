numeros = []
for _ in range(10):
    n = int(input("Digite um número: "))
    numeros.append(n)

for num in numeros[:]:
    if num % 2 == 0:
        numeros.remove(num)

print(numeros)
