def data_info(data_text):
    length = len(data_text)
    letters = []
    for i in range(len(data_text)):
        obecnosc = 0
        for j in range(len(letters)):
            if letters[j] == data_text[i]:
                obecnosc = 1
        if obecnosc == 0:
            letters.append(data_text[i])
    up = data_text.upper()
    low = data_text.lower()
    dictio = dict({"lenght": length, "letters": letters, "big_letters": up, "small_letters": low})
    return dictio

data_text = "Dog"
print(data_info(data_text))