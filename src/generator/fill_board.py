def generate_board(riddle, solution: str):
    if len(riddle) != len(solution):
        raise ValueError("Die Anzahl der Rätselteile muss die selbe länge haben wie die Lösung")

    x, y = 0, len(solution)
    solution_idx = 0
    prev_max, next_max = 0, 0

    word_pos = [0 for _ in range(len(riddle))]

    for i, part in enumerate(riddle):
        idx = part[1].find(solution[i])
        if idx == -1:
            raise ValueError(f"Der Buchstabe {solution[i]} ist nicht im Rätselteil {part[1]} enthalten")
        temp_prev = len(part[0]) + idx
        temp_next = len("".join(part)) - temp_prev - 1

        if i != 0:
            if temp_prev > prev_max:
                for j in range(i):
                    word_pos[j] += temp_prev - prev_max
            if temp_prev < prev_max:
                word_pos[i] = prev_max - temp_prev

        if temp_prev > prev_max:
            prev_max = temp_prev
            solution_idx = temp_prev

        prev_max = max(prev_max, temp_prev)
        next_max = max(next_max, temp_next)

    x = prev_max + next_max + 1

    grid = []
    grid_solution = []
    mask_editable = []
    for i, r in enumerate(riddle):
        out = " " * word_pos[i] + r[0] + " " * len(r[1]) + r[2]
        out += " " * (x - len(out))
        grid.append([c for c in out])

        out_solution = " " * word_pos[i] + "".join(r)
        out_solution += " " * (x - len(out_solution))
        grid_solution.append([c for c in out_solution])

        out_editable = "x" * word_pos[i] + r[0] + " " * len(r[1]) + r[2]
        out_editable += "x" * x
        out_editable = [1 if c == " " else 0 for c in out_editable]
        mask_editable.append(out_editable)


    return grid, grid_solution, mask_editable, solution_idx



def main():
    riddle = [["vogel", "schreck", "schraube"], ["haar", "gummi", "baer", ], ["laden", "schluss", "licht"]]
    solution = "eis"

    generate_board(riddle, solution)


if __name__ == "__main__":
    main()
