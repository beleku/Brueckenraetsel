import curses
import time

def run(stdscr: curses.window):
    height, width = stdscr.getmaxyx()

    # Key map to display
    key_map = "q - Quit | h - Help | Arrows - Navigate | Enter - Select Option"
    selection = 0
    options = ["play", "help", "exit"]
    while True:
        draw(stdscr, options, selection)
        try:
            key = stdscr.getch()
        except curses.error:
            continue
        if key == curses.KEY_UP:
            selection = (selection - 1) % len(options)
        elif key == curses.KEY_DOWN:
            selection = (selection + 1) % len(options)
        elif key == curses.KEY_ENTER or key in [10, 13]:
            time.sleep(1)
            if selection == 0:
                return "GAME", 1
            elif selection == 1:
                return "HELP", 1
            elif selection == 2:
                return "EXIT"
        elif key == ord('q'):
            return "EXIT", 1


def draw(stdscr, options, selected, x=2, y=1):
    stdscr.clear()
    stdscr.addstr(y, x, "Brückenrätsel | Menu", curses.A_BOLD)
    for i, option in enumerate(options):
        if i == selected:
            stdscr.addstr(y + 1 + i, x + 1, "> " + option)
        else:
            stdscr.addstr(y + 1 + i, x + 1, option)
    stdscr.refresh()