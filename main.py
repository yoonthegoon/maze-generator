import random


NORTH, SOUTH, EAST, WEST = 8, 4, 2, 1


class Cell:
    def __init__(self, x: int, y: int):
        self.x, self.y = x, y
        self.north, self.south, self.east, self.west = 4*(None,)
        self.visited = False
        self.walls = 0b1111

    def neighbors(self):
        return [i for i in (self.north, self.south, self.east, self.west) if i]


class Board:
    def __init__(self, width: int, height: int):
        self.width, self.height = width, height

        board = [[Cell(x, y) for x in range(width)] for y in range(height)]

        for y in range(height):
            for x in range(width):
                if y - 1 in range(height):
                    board[y][x].north = board[y - 1][x]
                if y + 1 in range(height):
                    board[y][x].south = board[y + 1][x]
                if x + 1 in range(width):
                    board[y][x].east = board[y][x + 1]
                if x - 1 in range(width):
                    board[y][x].west = board[y][x - 1]

        self.board = board

    def show(self):
        nodes = '╋┣┫┃┻┗┛╹┳┏┓╻━╺╸ '

        print(f'┌{self.width*"─"}┐')
        for y in range(self.height):
            print('│', end='')
            for x in range(self.width):
                print(nodes[self.board[y][x].walls], end='')

            print('│')
        print(f'└{self.width*"─"}┘')


def dfs(current_x: int, current_y: int, board: Board):
    current_cell = board.board[current_y][current_x]
    current_cell.visited = True

    while True:
        unvisited = [i for i in current_cell.neighbors() if not i.visited]

        if not unvisited:
            break

        next_cell = random.choice(unvisited)

        match next_cell:
            case current_cell.north:
                current_cell.walls -= NORTH
                next_cell.walls -= SOUTH
            case current_cell.south:
                current_cell.walls -= SOUTH
                next_cell.walls -= NORTH
            case current_cell.east:
                current_cell.walls -= EAST
                next_cell.walls -= WEST
            case current_cell.west:
                current_cell.walls -= WEST
                next_cell.walls -= EAST

        dfs(next_cell.x, next_cell.y, board)

    return


def main(w: int, h: int):
    x, y = random.randrange(0, w), random.randrange(0, h)
    b = Board(w, h)
    dfs(x, y, b)
    b.show()


if __name__ == '__main__':
    main(12, 8)
