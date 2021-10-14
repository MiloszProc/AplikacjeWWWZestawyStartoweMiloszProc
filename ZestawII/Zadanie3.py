def destroy_letters(text, letters):
    for j in range(len(letters)):
        text = text.replace(letters[j], "")
    return text
text = "Ala ma kota kot ma ale"
letters = ["a","t"]
print(destroy_letters(text, letters))