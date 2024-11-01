import curses
import os
import time

from src.cli.game import Game
import src.io.reader as reader
from src.generator import fill_board as generator


def run(stdscr: curses.window):
    stdscr.clear()
    stdscr.refresh()

    games_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../..", "game_files")
    available_games, filepaths = reader.get_available_games(games_dir)

    selection_scr = curses.newwin(len(available_games) + 1, 20, 1, 3)
    selected = 0

    while True:
        draw(selection_scr, available_games, selected)

        key = stdscr.getch()

        if key == curses.KEY_UP or key == ord('k'):
            selected = (selected - 1) % len(available_games)
        elif key == curses.KEY_DOWN or key == ord('j'):
            selected = (selected + 1) % len(available_games)
        elif key == curses.KEY_ENTER or key in [10, 13]:
            riddle, solution = reader.read_file(filepaths[selected])
            return Game(riddle, solution)
        elif key == ord('q'):
            return None


def draw(stdscr: curses.window, available_games: [str], selected: int):
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    stdscr.addstr(0, 0, "Select a game", curses.A_BOLD)
    for i, game in enumerate(available_games):
        if i == selected:
            stdscr.addstr(i + 1, 0, "> " + game, curses.color_pair(2))
        else:
            stdscr.addstr(i + 1, 0, game)
    stdscr.refresh()