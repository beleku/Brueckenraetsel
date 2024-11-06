import json
import random

from src.io import dictionary_reader


def get_bridges_random(charater: chr, bridges_file: str, max_iter=1000, min_length=4):
    with open(bridges_file, "r") as f:
        bridges = json.load(f)

        for first_word in random.sample(bridges.keys(), max_iter):
            # if len(bridges[first_word]) < 0: continue
            for second_word in bridges[first_word]:
                if second_word in ["der", "dem", "des"]:
                    continue
                if len(second_word) < min_length:
                    continue
                if charater not in second_word:
                    continue
                if second_word in bridges:
                    third_word = bridges[second_word][0]
                    return first_word, second_word, third_word
    return RuntimeError("No bridge found within max_iter")


def create_riddle_with_solution(solution_word: str, bridges_file="bruecken.json"):
    riddle = [list(get_bridges_random(letter, bridges_file)) for letter in solution_word]
    return riddle, solution_word


def create_riddle(length: int, path_to_dictionary="my.dict", path_to_bridges="bruecken.json"):
    solution = dictionary_reader.get_random_word_n(path_to_dictionary, length)
    riddle = [list(get_bridges_random(letter, path_to_bridges)) for letter in solution]
    return riddle, solution


def write_bridges_to_file(riddle, solution_word, file_path):
    with open(file_path, "w") as f:
        f.write(f"# Radomly generated riddle\n")
        f.write(f"solution: {solution_word}\n")
        for words in riddle:
            f.write(f"{words[0]}, {words[1]}, {words[2]}\n")


def main():
    riddle, solution_word = create_riddle_with_solution("hundertschaft")
    print(riddle)


if __name__ == "__main__":
    main()
