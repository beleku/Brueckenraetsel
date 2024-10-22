import curses

def draw(stdscr: curses.window, pos_y, pos_x, height, width, cell_width=1):
    first_line = "╔" + ("═"*cell_width + "╤")*(width-1) + "═"*cell_width + "╗\n"
    stdscr.addstr(pos_y, pos_x, first_line)
    for i in range(height-1):
        stdscr.addstr(pos_y + (i*2+1), pos_x, "║" + (" "*cell_width + "│")*(width-1) + " "*cell_width + "║\n")
        stdscr.addstr(pos_y + (i*2+2), pos_x, "╟" + ("─"*cell_width + "┼")*(width-1) + "─"*cell_width + "╢\n")

    stdscr.addstr(pos_y + (height-1)*2+1, pos_x, "║" + (" "*cell_width + "│")*(width-1) + " "*cell_width + "║\n")
    stdscr.addstr(pos_y + (height-1)*2+2, pos_x, "╚" + ("═"*cell_width + "╧")*(width-1) + "═"*cell_width + "╝")

