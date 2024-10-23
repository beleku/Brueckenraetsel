import curses
from curses import wrapper
from curses.textpad import rectangle

from src.cli import menu
from src.cli import game


def draw_keymap(stdscr):
    height, width = stdscr.getmaxyx()

    # Key map to display
    key_map = "q - Quit | h - Help | Arrows - Navigate | Enter - Edit"

    # Clear the line before writing the key-map
    stdscr.addstr(height - 1, 0, " " * (width - 1), curses.color_pair(1))

    # Display the key map at the bottom row
    stdscr.addstr(height - 1, 0, key_map[:width - 1], curses.color_pair(1))  # Truncate if necessary
    stdscr.refresh()


def main(stdscr):
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(4, 2, curses.COLOR_BLACK)

    screen_opt = ["MENU", "GAME", "HELP", "EXIT", "CONTINUE"]
    screen = screen_opt[0]
    difficulty = 1
    game_state = None
    game_solution = None
    mask = None
    solution_idx = None

    while True:
        if screen == "MENU":
            screen, difficulty = menu.run(stdscr, game_state, 0)
        elif screen == "GAME":
            screen, game_state, game_solution, mask, solution_idx = game.init(stdscr)
        elif screen == "HELP":
            screen = "MENU"
        elif screen == "EXIT":
            break
        elif screen == "CONTINUE":
            screen, game_state, game_solution, mask, solution_idx = game.run(stdscr, game_state, game_solution, mask, solution_idx)
    stdscr.clear()



if __name__ == "__main__":
    wrapper(main)