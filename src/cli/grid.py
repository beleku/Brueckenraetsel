def draw(height, width, cell_width=1):
    grid = "╔" + ("═"*cell_width + "╤")*(width-1) + "═"*cell_width + "╗\n"
    for _ in range(height-1):
        grid += "║" + (" "*cell_width + "│")*(width-1) + " "*cell_width + "║\n"
        grid += "╟" + ("─"*cell_width + "┼")*(width-1) + "─"*cell_width + "╢\n"
    grid += "║" + (" "*cell_width + "│")*(width-1) + " "*cell_width + "║\n"
    grid += "╚" + ("═"*cell_width + "╧")*(width-1) + "═"*cell_width + "╝"
    return grid


def draw_square(height, width):
    return draw(height, width, cell_width=3)


def draw_slim(height, width):
    return draw(height, width, cell_width=1)


def main():
    print(draw(5, 8, 3))
    print(draw(4, 20))


if __name__ == "__main__":
    main()
