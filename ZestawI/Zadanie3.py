tekst = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
moje_imie= "Miłosz"
moje_nazwisko = "Proc"
liczba_liter1 = tekst.count(moje_imie[2])
liczba_liter2 = tekst.count(moje_nazwisko[3])
#Ćwiczenie3
print((("W tekście jest {:3d} liter {:>10}, oraz {:d} liter {:10}".format(liczba_liter1, moje_imie[2], liczba_liter2, moje_nazwisko[3]))) + "po przerwie")
print("Ćwiczenia w  {poglanguage} sprawiają, że tracę rozum.".format(poglanguage = 'pythonie'))
doktor = {'lekarz' : 'psychiatry'}
print("ale ponoć wizyty u {lekarz} nie są drogie.".format(**doktor))