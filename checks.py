def ifSunk(ship_grid, ships):
    # check grid for first letter of each ship
    # if letter not there remove ship from list 
    # notify as sunk
    sunk_ships = []
    for ship in ships:
        sunk = True
        for row in ship_grid:
            if ship[0] in row:
                sunk = False
        if sunk:
            #add ship to sunk_ship list
            sunk_ships.append(ship)
    # remove sunk ships
    for ship in sunk_ships:
        del ships[ship]
    return ships

def firingSolution(display_grid, ship_grid, row, col):
    alpha = "ABCDEFGHIJ"
    result = f"{row + 1}:{alpha[col]} is a "
    if ship_grid[row][col] != ".":
        ship_grid[row][col] = "x"
        display_grid[row][col] = "X"
        result += "HIT!"
    else: 
        display_grid[row][col] = " "
        result += "MISS!"
    return result

def turnsToCountdown(countdown, countdownSteps):
    print(countdown, countdownSteps)
    if countdown == 0:
        return countdownSteps
    else:
        return countdown - 1
    