import curses
import time

import src.generator.grid as generator
from src.cli import table
from src.generator.cursor_logic import Cursor


class Game:
    def __init__(self, riddle: [[str]], solution: str):
        self.board, self.grid_solution, self.mask, self.solution_idx = generator.generate(riddle, solution)
        self.solved_rows = [False for _ in range(len(riddle))]
        self.current = -1
        self.stop = len(self.board)*len(self.board[0])

    def __iter__(self):
        self.current = -1
        return self

    def __next__(self):
        self.current += 1
        y, x = divmod(self.current, len(self.board[0]))
        if self.stop <= self.current:
            raise StopIteration
        return y, x, self.board[y][x], bool(self.mask[y][x]), (x == self.solution_idx)

    def check_rows(self):
        for y in range(len(self.board)):
            self.solved_rows[y] = self.board[y] == self.grid_solution[y]
        return self.solved_rows

    def get_shape(self):
        return len(self.board), len(self.board[0])

    def get_solved_rows(self):
        return self.solved_rows

    def get_solution_index(self):
        return self.solution_idx

    def solved(self):
        return self.board == self.grid_solution

    def get_char(self, y: int, x: int):
        return self.board[y][x]

    def set_char(self, c, cursor: Cursor):
        y, x = cursor.get_pos_yx()
        self.board[y][x] = c
        self.check_rows()


def premade_game(stdscr: curses.window):
    riddle = [["nudel", "holz", "bein"],  # h
              ["wochen", "tage", "dieb"],  # a
              ["fenster", "putzer", "fisch"],  # p
              ["wasser", "spiegel", "bild"],  # p
              ["abwehr", "system", "administration"],  # y
              ["himmel", "blau", "pause"],  # b
              ["spaghetti", "eis", "bein"],  # i
              ["vogel", "schreck", "schraube"],  # r
              ["kaffee", "klatsch", "presse"],  # t doppelt
              ["nudel", "holz", "bein"],  # h
              ["quell", "code", "wort"],  # d
              ["wasser", "fall", "beil"],  # a
              ["hunde", "baby", "klappe"]]  # y doppelt

    solution = "happybirthday"
    return run(stdscr, Game(riddle, solution))


def run(stdscr: curses.window, game: Game):
    stdscr.clear()
    stdscr.addstr(0, 0, "Brückenrätsel | Spiel", curses.A_BOLD)
    cursor = Cursor(0, 0, game.mask)
    draw(stdscr, game, cursor)

    draw_check = False

    while True:
        if draw_check:
            draw_check_rows(stdscr, game, cursor)
            draw_check = False
        else:
            update(stdscr, game, cursor)

        key = stdscr.getch()
        if key == curses.KEY_UP:
            cursor.move_up()
        elif key == curses.KEY_DOWN:
            cursor.move_down()
        elif key == curses.KEY_LEFT:
            cursor.move_left()
        elif key == curses.KEY_RIGHT or key == ord(' '):
            cursor.move_right()

        if key == ord("\t"):
            return "MENU", game

        # if key is letter
        if 65 <= key <= 90 or 97 <= key <= 122:
            game.set_char(chr(key).lower(), cursor)
            cursor.move_right()
            if game.solved():
                return "WIN", game

        # if key is backspace
        if key == curses.KEY_BACKSPACE:
            game.set_char(" ", cursor)
            cursor.move_left()

        if key == curses.KEY_ENTER or key in [10, 13]:
            draw_check = True
            if game.solved():
                return "WIN", game


def draw(stdscr: curses.window, game: Game, cursor: Cursor, pos_y=1, pos_x=3):
    stdscr.clear()
    stdscr.addstr(pos_y, pos_x, "Brückenrätsel", curses.A_BOLD)
    height, width = stdscr.getmaxyx()
    grid_height, grid_width = game.get_shape()

    table.draw(stdscr, pos_y + 1, pos_x, grid_height, grid_width, 3)

    key_map = " tab - Menu | Arrows - Navigate | Enter - Check entries"
    height, width = stdscr.getmaxyx()
    stdscr.addstr(height - 1, 0, " " * (width - 1), curses.color_pair(1))

    # Display the key map at the bottom row
    stdscr.addstr(height - 1, 0, key_map[:width - 1], curses.color_pair(1))  # Truncate if necessary
    stdscr.refresh()

    for y, x, c, editabel, part_of_solution in game:
        if cursor.get_pos_yx() == (y, x):
            stdscr.addstr(pos_y + 2 + y * 2, pos_x + 2 + x * 4, c.upper(), curses.A_REVERSE)
        elif editabel:
            if part_of_solution:
                if c == " ":
                    stdscr.addstr(pos_y + 2 + y * 2, pos_x + 2 + x * 4, "_")
                else:
                    stdscr.addstr(pos_y + 2 + y * 2, pos_x + 2 + x * 4, str(c).upper(), curses.color_pair(4))
            else:
                stdscr.addstr(pos_y + 2 + y * 2, pos_x + 2 + x * 4, str(c).upper(), curses.color_pair(2))

        else:
            stdscr.addstr(pos_y + 2 + y * 2, pos_x + 2 + x * 4, c.upper())

    stdscr.refresh()


def draw_check_rows(stdscr: curses.window, game: Game, cursor: Cursor, pos_y=1, pos_x=3):
    solved_rows = game.check_rows()
    for y, x, c, editable, part_of_solution in game:
        if editable:
            if solved_rows[y]:
                stdscr.addstr(pos_y + 2 + y * 2, pos_x + 2 + x * 4, str(c).upper(), curses.color_pair(4))
            else:
                if c == " ":
                    stdscr.addstr(pos_y + 2 + y * 2, pos_x + 2 + x * 4, "_", curses.color_pair(5))
                else:
                    stdscr.addstr(pos_y + 2 + y * 2, pos_x + 2 + x * 4, str(c).upper(), curses.color_pair(5))
            if cursor.get_pos_yx() == (y, x):
                stdscr.addstr(pos_y + 2 + y * 2, pos_x + 2 + x * 4, str(c).upper(), curses.A_REVERSE)


    stdscr.refresh()


def update(stdscr: curses.window, game: Game, cursor: Cursor, pos_y=1, pos_x=3):
    for y, x, c, editable, part_of_solution in game:
        if editable:
            if cursor.get_pos_yx() == (y, x):
                stdscr.addstr(pos_y + 2 + y * 2, pos_x + 2 + x * 4, c.upper(), curses.A_REVERSE)
            elif part_of_solution:
                if c == " ":
                    stdscr.addstr(pos_y + 2 + y * 2, pos_x + 2 + x * 4, "_")
                else:
                    stdscr.addstr(pos_y + 2 + y * 2, pos_x + 2 + x * 4, str(c).upper(), curses.color_pair(4))
            else:
                stdscr.addstr(pos_y + 2 + y * 2, pos_x + 2 + x * 4, str(c).upper(), curses.color_pair(2))

        else:
            stdscr.addstr(pos_y + 2 + y * 2, pos_x + 2 + x * 4, c.upper())

    stdscr.refresh()