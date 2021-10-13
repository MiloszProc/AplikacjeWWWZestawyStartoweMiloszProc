slownik_pierwszy = dict({"jeden": 1, "dwa": 2, "trzy": 3})
slownik_drugi = dict({"one": 1, "two": 2, "three": 3})
slownik_trzeci = dict({"uno": 1, "due": 2, "tre": 3})
lista = [slownik_pierwszy, slownik_drugi, slownik_trzeci]
string = ""
for i in range(3):
    string = string + str(lista[i])
string = '{:{align}{width}}'.format(string, align='^', width='500')
print(string)