class Cursor:
    def __init__(self, row, col, grid_mask):
        self.grid_mask = grid_mask
        if self.valid_pos(row, col):
            self.x = row
            self.y = col
        else:
            self.x = 0
            self.y = 0
            self.y, self.x = self.find_nearest_valid_pos(row, col)

        self.x_prev = row
        self.y_prev = col

    def move(self, dy, dx):
        if self.valid_pos(dy, dx):
            self.x_prev = self.x
            self.y_prev = self.y
            self.x = dx
            self.y = dy
            return True
        return False


    def move_up(self):
        new_y = (self.y - 1) % len(self.grid_mask)
        new_y, new_x = self.find_nearest_valid_pos(new_y, self.x)
        if self.move(new_y, new_x):
            return True
        return False


    def move_down(self):
        new_y = (self.y + 1) % len(self.grid_mask)
        new_y, new_x = self.find_nearest_valid_pos(new_y, self.x)
        if self.move(new_y, new_x):
            return True
        return False


    def move_left(self):
        if self.move(self.y, self.x - 1):
            return True
        self.move_up()
        self.x = len(self.grid_mask[self.y]) - 1 - self.grid_mask[self.y][::-1].index(1)
        return True


    def move_right(self):
        if self.move(self.y, self.x + 1):
            return True
        self.move_down()
        self.x = self.grid_mask[self.y].index(1)


    def get_pos_yx(self):
        return self.y, self.x


    def find_nearest_valid_pos(self, y, x):
        if self.valid_pos(y, x):
            return y, x
        else:
            for i in range(1, len(self.grid_mask[y])):
                if self.valid_pos(y, x + i):
                    return y, x + i
                if self.valid_pos(y, x - i):
                    return y, x - i


    def find_next_pos(self):
        for i in range(self.y, len(self.grid_mask)):
            for j in range(self.x, len(self.grid_mask[0])):
                if self.grid_mask[i][j] == 1:
                    return i, j


    def valid_pos(self, y, x):
        if x < 0 or y < 0:
            return False
        if y >= len(self.grid_mask) or x >= len(self.grid_mask[y]):
            return False
        if self.grid_mask[y][x] == 0:
            return False
        return True


def main():
    test_grid = [[0, 0, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1], [1, 0, 0, 0, 1]]
    print(f"first index of 1 in row 0 is {test_grid[0].index(1)}")
    print(f"last index of 1 in row 0 is {len(test_grid[0]) - 1 - test_grid[0][::-1].index(1)}")
    cursor = Cursor(0, 0, test_grid)
    cursor.move_left()
    print(cursor.get_pos_yx())


if __name__ == '__main__':
    main()
