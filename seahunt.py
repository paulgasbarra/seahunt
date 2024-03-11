import grid
import input
import checks
import utils
import display
import random
from logo import logo
from ship_list import ships

# create something for ships to shoot at 
# the submarine will move, each time it moves it will reset the waters
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
# Create Firing Countdown

countdownSteps  = 5
countdown = countdownSteps

castles = [ "🏰", "🏰", "🏰" ]

def move_sub(ship_grid, display_grid):
    distance = random.choice([1, 2, 3])
    direction = random.choice(['up', 'right', 'down', 'left'])
    #pick distance
    #pick direction
    #check boundries
    #check other ships
    #move distance
    #update display grid
    #find 
    
    return ship_grid

def enemy_fire(castles):
    random.choice([1,2,3])
    print("Enemy 7firing at your position.")
    if random == 3:
        print(f"Enemy has hit your position. {len(castles)} canon left.")
        castles.pop()
    else:
        print("Enemy fire missed.")
    return castles

while not gameOver:
    # set display
    display.game_board(logo, result, ships, display_grid, countdown, castles)
    if countdown == 0:
        castles = enemy_fire(castles)
    
    # get inputs
    print("Enter a row and column to fire at: ")
    row = input.get_row()
    col = input.get_col()

    # get results
    result = checks.firingSolution(display_grid, ship_grid, row, col)
    precheck = list(ships)
    ships = checks.ifSunk(ship_grid, ships)
    if len(precheck) > len(ships):
        sunk_ship = utils.get_dict_difference(precheck, ships)
        result += (f" YOU JUST SUNK THE {next(iter(sunk_ship))}!")
    
    if len(ships) == 0 or len(castles) == 0:
        gameOver = True

    countdown = checks.turnsToCountdown(countdown, countdownSteps)
    ship_grid = move_sub(ship_grid, display_grid)
display.game_board(logo, result, ships, display_grid, countdown, castles)

if len(castles) == 0:
    print("MISSION FAILURE! ALL YOUR CANNON HAVE BEEN DESTROYED!")
else: 
    print("CONGRATULATIONS! YOU HAVE SUNK ALL THE SHIPS!")
 