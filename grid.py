import random

def create_grid(): 
    grid = []
    for i in range(10):
        row = []
        for j in range(10):
            row.append(".")
        grid.append(row)
    return grid
    
def print_grid(grid):
    print("   A B C D E F G H I J")
    for index, row in enumerate(grid):
        if index < 9:
            printRow = " " + str(index + 1) + " "
        else:
            printRow = str(index + 1) + " "
        for cell in row:
            printRow = printRow + cell + " "
        printRow += str(index + 1)
        print(printRow)
    print("   A B C D E F G H I J")

def is_valid_placement(grid, row, col, orientation, ship_length):
    if orientation == "horizontal":
        if col + ship_length > 10:
            return False
        for i in range(col, col + ship_length):
            if grid[row][i] != ".":
                return False
    else:  # vertical
        if row + ship_length > 10:
            return False
        for i in range(row, row + ship_length):
            if grid[i][col] != ".":
                return False
    return True


def place_ship(grid, row, col, orientation, ship_length, ship_symbol):
    if orientation == "horizontal":
        for i in range(col, col + ship_length):
            grid[row][i] = ship_symbol
    else:
        for i in range(row, row + ship_length):
            grid[i][col] = ship_symbol

def populate_grid(grid, ships):
    for ship in ships:
        placed = False
        attempts = 0
        while not placed:
            attempts += 1
            length = ships[ship]
            orientation = random.choice(["horizontal", "vertical"])
            if orientation == "horizontal":
                row, col = random.randint(0, 9), random.randint(0, 10 - length)
            else:
                row, col = random.randint(0, 10 - length), random.randint(0, 9)

            if is_valid_placement(grid, row, col, orientation, length):
                place_ship(grid, row, col, orientation, length, ship[0])  # using first letter of ship name as symbol
                placed = True
    return grid

