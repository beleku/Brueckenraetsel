import curses
import time

def run(stdscr: curses.window, game=None, selection=0):
    height, width = stdscr.getmaxyx()

    # Key map to display
    key_map = "q - Quit | h - Help | Arrows - Navigate | Enter - Select Option"
    options = ["new game", "help", "exit"]
    return_code = [["GAME", 1], ["HELP", 1], ["EXIT", 1]]

    if game is not None:
        options = ["continue", "new game", "help", "exit"]
        return_code = [["CONTINUE", 1], ["GAME", 0], ["HELP", 1], ["EXIT", 1]]

    curses.curs_set(0)

    while True:
        draw(stdscr, options, selection)
        try:
            key = stdscr.getch()
        except curses.error:
            continue
        if key == curses.KEY_UP or key == ord('k'):
            selection = (selection - 1) % len(options)
        elif key == curses.KEY_DOWN or key == ord('j'):
            selection = (selection + 1) % len(options)
        elif key == curses.KEY_ENTER or key in [10, 13]:
            return return_code[selection]
        elif key == ord('q'):
            return "EXIT", 1


def draw(stdscr, options, selected, x=2, y=1):
    stdscr.clear()
    stdscr.addstr(y, x, "Brückenrätsel | Menu", curses.A_BOLD)
    key_map = " q - Quit | h - Help | Arrows - Navigate | Enter - Select Option"
    height, width = stdscr.getmaxyx()
    stdscr.addstr(height - 1, 0, " " * (width - 1), curses.color_pair(1))

    # Display the key map at the bottom row
    stdscr.addstr(height - 1, 0, key_map[:width - 1], curses.color_pair(1))  # Truncate if necessary
    stdscr.refresh()

    for i, option in enumerate(options):
        if i == selected:
            stdscr.addstr(y + 1 + i, x + 1, "> " + option)
        else:
            stdscr.addstr(y + 1 + i, x + 1, option)