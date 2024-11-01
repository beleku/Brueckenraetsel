

dictionary_path = "my.dict"

dictionary = []

print("Reading dictionary...")
with open(dictionary_path, "r") as f:
    for word in f:
        word = word.split(" ")[0]
        word = word.replace("\n", "")
        word.lower()
        word = word.replace("ä", "ae")
        word = word.replace("ö", "oe")
        word = word.replace("ü", "ue")
        if len(word) > 2:
            dictionary.append(word.lower())

print("Dictionary read!")
print("Finding brücken...")
brücken = {}

for i, word in enumerate(dictionary[:1000]):
    contenders = []
    for j, word_2 in enumerate(dictionary[i+1:]):
        if word_2.startswith(word):
            contenders.append(word_2)
        else:
            break

    vaild_words = []

    for contender in contenders:
        contender = contender[len(word):]
        if contender[len(word):] in dictionary:
            vaild_words.append(contender[len(word):])

    if len(contenders) > 0:
        brücken[word] = contenders

print(brücken["abbau"])