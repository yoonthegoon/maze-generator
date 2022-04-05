import random


class Cell:
    def __init__(self, x: int, y: int):
        self.x, self.y = x, y
        self.north, self.south, self.east, self.west = 4*(None,)
        self.visited = False
        self.walls = 0x1111

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
        print(f'┌{self.width*"─"}┐')
        for y in range(self.height):
            print('│', end='')
            for x in range(self.width):
                match self.board[y][x].walls:
                    case 0x0000:
                        print('╋', end='')
                    case 0x0001:
                        print('┣', end='')
                    case 0x0010:
                        print('┫', end='')
                    case 0x0011:
                        print('┃', end='')
                    case 0x0100:
                        print('┻', end='')
                    case 0x0101:
                        print('┗', end='')
                    case 0x0110:
                        print('┛', end='')
                    case 0x0111:
                        print('╹', end='')
                    case 0x1000:
                        print('┳', end='')
                    case 0x1001:
                        print('┏', end='')
                    case 0x1010:
                        print('┓', end='')
                    case 0x1011:
                        print('╻', end='')
                    case 0x1100:
                        print('━', end='')
                    case 0x1101:
                        print('╺', end='')
                    case 0x1110:
                        print('╸', end='')
                    case 0x1111:
                        print(' ', end='')
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
        unvisited.remove(next_cell)

        match next_cell:
            case current_cell.north:
                current_cell.walls -= 0x1000
                next_cell.walls -= 0x0100
            case current_cell.south:
                current_cell.walls -= 0x0100
                next_cell.walls -= 0x1000
            case current_cell.east:
                current_cell.walls -= 0x0010
                next_cell.walls -= 0x0001
            case current_cell.west:
                current_cell.walls -= 0x0001
                next_cell.walls -= 0x0010

        dfs(next_cell.x, next_cell.y, board)

    return


def main(w: int, h: int):
    x, y = random.randrange(0, w), random.randrange(0, h)
    b = Board(w, h)
    dfs(x, y, b)
    b.show()


if __name__ == '__main__':
    main(4, 4)
