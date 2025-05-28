lista = []

while True:
    print("\nMenu:")
    print("1 - Adicionar elemento")
    print("2 - Remover elemento")
    print("3 - Listar elementos")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        elem = input("Digite o elemento para adicionar: ")
        lista.append(elem)
        print(f"'{elem}' adicionado.")

    elif opcao == "2":
        elem = input("Digite o elemento para remover: ")
        if elem in lista:
            lista.remove(elem)
            print(f"'{elem}' removido.")
        else:
            print("Elemento não encontrado.")

    elif opcao == "3":
        print("Elementos da lista:")
        for e in lista:
            print(e)

    elif opcao == "4":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida, tente novamente.")
