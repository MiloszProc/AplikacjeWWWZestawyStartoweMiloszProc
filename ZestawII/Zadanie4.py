def celciusz_zmiana(temperature, temperature_type):
    if temperature_type == "F":
        return ((9*temperature)/5+32)
    elif temperature_type == "R":
        return ((temperature+273.15)*1.8)
    elif temperature_type == "K":
        return (temperature+273)
    return "Błędny rodzaj temperatury";

temperatura = 34
print(celciusz_zmiana(temperatura, "F"))
print(celciusz_zmiana(temperatura, "R"))
print(celciusz_zmiana(temperatura, "K"))
print(celciusz_zmiana(temperatura, "B"))