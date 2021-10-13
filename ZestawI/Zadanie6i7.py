lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = []
listzapas = []
for x in lista:
    if x > 5 :
        lista2.append(x)
    else:
        #stworzone przez irytacje z przeskakującymi wartości removie.
        listzapas.append(x)
lista = listzapas
print(lista2)
print(lista)
#Zadanie7
listzapas = [0] + listzapas + lista2
print(listzapas)