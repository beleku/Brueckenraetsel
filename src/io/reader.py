import os

def read_file(file_path):
    with open(file_path, 'r') as file:
        solution = ""
        riddle = []
        for line in file:
            if line.startswith("#") or line == "\n":
                continue
            if line.startswith("solution:"):
                solution = line.split(":")[1].strip().lower()
                continue
            riddle.append([word.strip().lower() for word in line.split(",")])

        if solution is None:
            raise ValueError("No solution found in file")
        return riddle, solution


def get_available_games(file_path="../game_files"):
    names, file_paths = [], []
    for file in os.listdir("game_files"):
        if file.endswith(".txt"):
            names.append(file)
            file_paths.append(os.path.abspath(os.path.join(file_path, file)))
    return names, file_paths