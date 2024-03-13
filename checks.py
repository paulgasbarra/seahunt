import random

def if_sunk(ship_grid, ships):
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

def firing_solution(display_grid, ship_grid, row, col):
    print(ship_grid)
    alpha = "ABCDEFGHIJ"
    result = f"{row + 1}:{alpha[col]} is a "
    if ship_grid[row][col] != ".":
        if ship_grid[row][col] == "S":
            ship_grid[row][col] == "s"
        else: 
            ship_grid[row][col] = "x"
            display_grid[row][col] = "X"
            result += "HIT!"
    else: 
        display_grid[row][col] = " "
        result += "MISS!"
    return result

def countdown_to_salvo(countdown, countdownSteps):
    if countdown == 0:
        return countdownSteps
    else:
        return countdown - 1

def enemy_fire(castles):
    hit = random.choice([1,2,3]) == 1
    print("Enemy firing at your position.")
    if hit:
        castles.pop()
        print(f"Enemy has hit your position. {len(castles)} canon left.")
    else:
        print("Enemy fire missed.")
    return castles