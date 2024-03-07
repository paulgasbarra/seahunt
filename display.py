import os
import grid

def ship_list(ships):
    ship_list_str = ''
    for ship in list(ships)[0:-1]:    
        ship_list_str +=  ship + ", "
    if ships:
        ship_list_str += list(ships)[-1]
    if len(ships) != 1: 
        plural = "s"
    else:
        plural = ""
    return str(f"{len(ships)} ship{plural} left: {ship_list_str}") 

def game_board(logo, result, ships, display_grid):
    os.system('clear')
    print(logo)
    print(" ")
    print(ship_list(ships))
    print(" ")
    grid.print_grid(display_grid)
    print(" ")
    print(result)
    print(" ")