def nowa_lista(lista_a, lista_b):
    lista_paz = []
    lista_niepaz = []
    for i in lista_a:
        if i%2 == 0:
            lista_paz.append(lista_a[i])
    for j in lista_b:
        if j%2 != 0:
            lista_niepaz.append(lista_b[j])
    return lista_paz+lista_niepaz

listaa = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
listab = [0, 1, 2, 3, 4, 5]
print(nowa_lista(listaa, listab))
