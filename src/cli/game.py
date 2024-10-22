import curses

import src.generator.grid as generator
from src.cli import table
from src.generator.cursor_logic import Cursor


def run(stdscr: curses.window, difficulty: int):
    riddle = [["vogel", "schreck", "schraube"], ["haar", "gummi", "baer", ], ["laden", "schluss", "licht"]]
    solution = "eis"

    grid, grid_solution, mask, solution_idx = generator.generate(riddle, solution)
    current_game_state = grid.copy()

    stdscr.clear()
    stdscr.addstr(0, 0, "Brückenrätsel | Spiel", curses.A_BOLD)

    cursor = Cursor(0, 0, mask)

    while True:
        draw(stdscr, current_game_state, cursor.get_pos_yx())

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



def draw(stdscr: curses.window, grid: list, selected: tuple, pos_y=2, pos_x=1):
    stdscr.clear()
    stdscr.addstr(pos_y, pos_x, "Brückenrätsel", curses.A_BOLD)
    height, width = stdscr.getmaxyx()
    grid_height, grid_width = len(grid), len(grid[0])

    table.draw(stdscr, pos_y + 1, pos_x, grid_height, grid_width, 3)

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if selected == (y, x):
                stdscr.addstr(pos_y + 2 + y*2, pos_x + 2 + x*4, cell.upper(), curses.A_REVERSE)
            else:
                stdscr.addstr(pos_y + 2 + y*2, pos_x + 2 + x*4, cell.upper())

    stdscr.refresh()


