import curses
import time


def draw(stdscr: curses.window):
    pass


def run(stdscr: curses.window):
    stdscr.clear()
    msg = "Herzlichen Glückwunsch"
    for i in range(len(msg)+1):
        draw(stdscr)
        stdscr.addstr(3, 3, msg[:i])
        stdscr.refresh()
        time.sleep(0.1)

    time.sleep(1)

    stdscr.addstr(4, 3, "Drücke eine Taste um zum Menü zurückzukehren")
    stdscr.refresh()
    stdscr.getch()

    return "MENU"

