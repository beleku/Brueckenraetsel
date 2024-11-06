import random


def sanitize(word):
    word = word.strip()
    word = word.lower()
    word = word.replace("ä", "ae")
    word = word.replace("ö", "oe")
    word = word.replace("ü", "ue")
    word = word.replace("ß", "ss")
    return word


def get_dictionary(file_path: str) -> list[str]:
    with open(file_path, "r") as f:
        return [sanitize(line.split(" ")[0]) for line in f]


def get_random_word_n(path_to_dictionary: str, length: int):
    dictionary = get_dictionary(path_to_dictionary)
    words_n = [word for word in dictionary if len(word) == length]
    return random.choice(words_n)


def main():
    print(get_random_word_n("my.dict", 5))
    print(len(get_dictionary("my.dict")))


if __name__ == '__main__':
    main()
