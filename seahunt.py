import grid
import input
import checks
import utils
import display
import random
from logo import logo
from ship_list import ships
 
# carrier fires every other turn
# battleship and destroyer fires every 2 turns 
# submarine fires every 3
# pt boat fires every 4 turns

# the submarine will move, each time it moves through a revealed zone or sunk ship, 
# it will reset the waters to "."

# it moves in a direction at variable speed
# ships will fire at targets a given number of turns, 
# if a ship was hit it will delay its firing by 1 turn
# the bigger the ship, the more often it will fire
# you get 3 sonar checks that will clear 9 squares for 1 turn 

# GAME SETUP

# Create string that notifies player of action results
result = ""
# Create a grid to display
display_grid = grid.create_grid()
# Create a grid to place ships
ship_grid = grid.populate_grid(grid.create_grid(), ships)
# Create Game Over Flag
gameOver = False
# Initialize Firing Countdown
countdownSteps  = 3
countdown = countdownSteps

castles = [ "🏰", "🏰", "🏰" ]


def move_sub(grid):
    # Find the submarine's position
    sub_positions = [(i, j) for i, row in enumerate(grid) for j, val in enumerate(row) if val == 'S' or val == "s"]
    
    # If the submarine is not found or is not properly sized, return the grid as is
    if not sub_positions or len(sub_positions) != 3:
        return grid
    
    # Get sub's orientation:
    sub_orientation = "vertical" if sub_positions[0][0] - sub_positions[1][0] == 0 else "horizontal"

    # Directions to attempt moves: (name, delta row, delta column)
    directions = [('up', -1, 0), ('down', 1, 0), ('left', 0, -1), ('right', 0, 1)]
    valid_moves = []

    # Check for each direction if the move is possible
    for direction, dr, dc in directions:
        # if orientation differs from direction then add 1 space to the direction search
        can_move = True
        # Determine if all parts of the sub can move in this direction
        for row, col in sub_positions:
            for step in range(1, 4):  # Check 1 to 3 spaces ahead
                new_row = row + dr * step
                new_col = col + dc * step
                if not (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0])):  # Check for out of bounds
                    can_move = False
                    break
                elif grid[new_row][new_col] not in ['.', 'x', ' ']:  # Check for collision
                    can_move = False
                    break
        if can_move:
            valid_moves.append((direction, dr, dc))

    # If no valid move, return the grid as is
    if not valid_moves:
        return grid

    # Randomly select a move direction and distance
    direction, dr, dc = random.choice(valid_moves)
    distance = random.randint(1, 3)

    # Clean the current submarine position
    for row, col in sub_positions:
        grid[row][col] = '.'

    # Move the submarine
    if ["up", "down"].includes(direction) and sub_orientation == "horizontal":
        #reorient sub
    if ["left", "right"].includes(direction) and sub_orientation == "vertical":
        #reorient sub
    for row, col in sub_positions:
        new_row = row + dr * distance
        new_col = col + dc * distance
        grid[new_row][new_col] = 'S'

    # Clean any 'x' or ' ' characters by replacing them with '.'
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val in ['x', ' ']:
                grid[i][j] = '.'

    return grid

while not gameOver:
    # set display
    display.game_board(logo, result, ships, display_grid, countdown, castles)
    if countdown == 0:
        castles = checks.enemy_fire(castles)
    
    # get inputs
    print("Enter a row and column to fire at: ")
    row = input.get_row()
    col = input.get_col()

    # get results
    result = checks.firing_solution(display_grid, ship_grid, row, col)
    precheck = list(ships)
    ships = checks.if_sunk(ship_grid, ships)
    if len(precheck) > len(ships):
        sunk_ship = utils.get_dict_difference(precheck, ships)
        result += (f" YOU JUST SUNK THE {next(iter(sunk_ship))}!")
    
    if len(ships) == 0 or len(castles) == 0:
        gameOver = True

    countdown = checks.countdown_to_salvo(countdown, countdownSteps)
    # ship_grid = move_sub(ship_grid, display_grid)
display.game_board(logo, result, ships, display_grid, countdown, castles)

if len(castles) == 0:
    print("MISSION FAILURE! ALL YOUR CANNON HAVE BEEN DESTROYED!")
else: 
    print("CONGRATULATIONS! YOU HAVE SUNK ALL THE SHIPS!")
 