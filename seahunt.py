import grid
import input
import checks
import utils
import display
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

while not gameOver:
    # set display
    display.game_board(logo, result, ships, display_grid, countdown)
    
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
    
    if len(ships) == 0:
        gameOver = True

    countdown = checks.turnsToCountdown(countdown, countdownSteps)
display.game_board(logo, result, ships, display_grid)
print("CONGRATULATIONS! YOU HAVE SUNK ALL THE SHIPS!")
 