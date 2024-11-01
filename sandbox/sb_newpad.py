import curses
import time
from curses import wrapper


def main(stdscr: curses.window):
    stdscr.addstr(1, 3, "Title")
    height, width = stdscr.getmaxyx()
    pad_height, pad_width = 20, 20

    lines = [f"Line {i}" for i in range(pad_height)]

    pad = curses.newpad(pad_height, pad_width)
    pad.scrollok(True)
    pad.idlok(1)
    for i, line in enumerate(lines):
        pad.addstr(i, 2, line)
    pad.border()

    stdscr.refresh()
    pad.refresh(0, 0, 2, 3, pad_height-4, pad_width+3)

    while True:
        key = stdscr.getch()

        if key == ord("q"):
            break

        if key == curses.KEY_UP or key == ord("k"):
            pad.scroll(-1)
        elif key == curses.KEY_DOWN or key == ord("j"):
            pad.scroll(1)

        pad.refresh(0, 0, 2, 3, pad_height-4, pad_width+3)


if __name__ == '__main__':
    wrapper(main)
