import curses

import src.generator.grid as generator
from src.cli import table
from src.generator.cursor_logic import Cursor


def run(stdscr: curses.window, difficulty: int):
    riddle = [["vogel", "schreck", "schraube"],
              ["haar", "gummi", "baer", ],
              ["laden", "schluss", "licht"],
              ["spaghetti", "eis", "bein"],
              ["nudel", "holz", "bein"],
              ["fenster", "putzer", "fisch"],
              ["wochen", "tage", "dieb"],
              ["quell", "code", "wort"]]
    solution = "eissorte"

    grid, grid_solution, mask, solution_idx = generator.generate(riddle, solution)
    current_game_state = grid.copy()

    stdscr.clear()
    stdscr.addstr(0, 0, "Brückenrätsel | Spiel", curses.A_BOLD)

    cursor = Cursor(0, 0, mask)

    while True:
        draw(stdscr, current_game_state, mask, cursor.get_pos_yx())

        key = stdscr.getch()
        if key == curses.KEY_UP:
            cursor.move_up()
        elif key == curses.KEY_DOWN:
            cursor.move_down()
        elif key == curses.KEY_LEFT:
            cursor.move_left()
        elif key == curses.KEY_RIGHT:
            cursor.move_right()

        if key == ord("\t"):
            return "MENU"

        # if key is letter
        if 65 <= key <= 90 or 97 <= key <= 122:
            y, x = cursor.get_pos_yx()
            current_game_state[y][x] = chr(key).lower()
            cursor.move_right()

        # if key is backspace
        if key == 127:
            y, x = cursor.get_pos_yx()
            current_game_state[y][x] = " "
            cursor.move_left()



def draw(stdscr: curses.window, grid: list, mask: list, selected: tuple, pos_y=1, pos_x=3):
    stdscr.clear()
    stdscr.addstr(pos_y, pos_x, "Brückenrätsel", curses.A_BOLD)
    height, width = stdscr.getmaxyx()
    grid_height, grid_width = len(grid), len(grid[0])

    table.draw(stdscr, pos_y + 1, pos_x, grid_height, grid_width, 3)

    key_map = " tab - Menu | Arrows - Navigate | Enter - Select Option"
    height, width = stdscr.getmaxyx()
    stdscr.addstr(height - 1, 0, " " * (width - 1), curses.color_pair(1))

    # Display the key map at the bottom row
    stdscr.addstr(height - 1, 0, key_map[:width - 1], curses.color_pair(1))  # Truncate if necessary
    stdscr.refresh()

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if selected == (y, x):
                stdscr.addstr(pos_y + 2 + y*2, pos_x + 2 + x*4, cell.upper(), curses.A_REVERSE)
            elif mask[y][x]:
                stdscr.addstr(pos_y + 2 + y*2, pos_x + 2 + x*4, cell.upper(), curses.COLOR_BLUE)
            else:
                stdscr.addstr(pos_y + 2 + y*2, pos_x + 2 + x*4, cell.upper())

    stdscr.refresh()


