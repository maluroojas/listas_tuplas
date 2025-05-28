def elementos_unicos(lista):
    unica = []
    for elem in lista:
        if elem not in unica:
            unica.append(elem)
    return unica
