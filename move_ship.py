import random
import time

def will_collide(grid_space):
    return grid_space not in ['.', 'x', ' ', 'S', 's']

def is_in_bounds(row, col, ship_grid):
    return 0 <= row < len(ship_grid) and 0 <= col < len(ship_grid[0])

def should_turn(orientation, direction):
    return (orientation == "horizontal" and moving_vertically(direction)) or (orientation == "vertical" and moving_horizontally(direction)) 

def moving_vertically(direction):
    return direction in ["up", "down"]

def moving_horizontally(direction):
    return direction in ["left", "right"]

def clear_to_turn(orientation, sub_positions, ship_grid):
    mid_sub = sub_positions[1]
    if orientation == "horizontal":
        #check above and below
        above_sub = ship_grid[mid_sub[0]][mid_sub[1] - 1]
        below_sub = ship_grid[mid_sub[0]][mid_sub[1] + 1]
        return not will_collide(above_sub) and not will_collide(below_sub) 
    elif orientation == "vertical":
        #check left and right
        left_sub = ship_grid[mid_sub[0] - 1][mid_sub[1]]
        right_sub = ship_grid[mid_sub[0] + 1][mid_sub[1]]
        return not will_collide(left_sub) and not will_collide(right_sub)
    else:
        return True

def move_sub(ship_grid):
    # Find the submarine's position
    sub_positions = [(i, j) for i, row in enumerate(ship_grid) for j, val in enumerate(row) if val == 'S' or val == "s"]
   
    
    # If the submarine is not found or is not properly sized, return the grid as is
    if not sub_positions or len(sub_positions) != 3:
        return ship_grid
    
    # Get sub's orientation:
    sub_orientation = "vertical" if sub_positions[0][0] - sub_positions[1][0] == 0 else "horizontal"
    

    # Directions to attempt moves: (name, delta row, delta column)
    directions = [('up', -1, 0), ('down', 1, 0), ('left', 0, -1), ('right', 0, 1)]
    valid_moves = []

    # Check for each direction if the move is possible
    for direction, dr, dc in directions:
        # if orientation differs from direction check clearance to turn       
        can_move = True
        
        if should_turn(sub_orientation, direction) and not clear_to_turn(sub_orientation, sub_positions, ship_grid):
            can_move = False
            break



        # check from middle out
        sub_row, sub_col = sub_positions[1]
        for step in range(1, 4):  # Check 1 to 3 spaces ahead
            if moving_horizontally(direction):
                new_row = sub_row + dr * (step + 1)
                new_col = sub_col 
            elif moving_vertically(direction):
                new_col = sub_col + dc * (step + 1)
                new_row = sub_row
            if not is_in_bounds(new_row, new_col, ship_grid):  # Check for out of bounds
                can_move = False
                break
            elif will_collide(ship_grid[new_row][new_col]):  # Check for collision
                can_move = False
                break
        if can_move:
            valid_moves.append((direction, dr, dc))

    # If no valid move, return the grid as is
    print("valid moves", valid_moves)
    if not valid_moves:
        return ship_grid

    # Randomly select a move direction and distance
    direction, dr, dc = random.choice(valid_moves)
    distance = random.randint(1, 3)

    # Clean the current submarine position
    for row, col in sub_positions:
        ship_grid[row][col] = '.'

    # Turn the submarine
    if moving_vertically(direction) and sub_orientation == "horizontal":
        sub_positions[0] = [sub_positions[0][0] + 1, sub_positions[0][1] + 1]
        sub_positions[2] = [sub_positions[2][0] - 1, sub_positions[2][1] - 1]
    
    if moving_horizontally(direction) and sub_orientation == "vertical":
        sub_positions[0] = [sub_positions[0][0] - 1, sub_positions[0][1] - 1]
        sub_positions[2] = [sub_positions[2][0] + 1, sub_positions[2][1] + 1]

    # Move the submarine
    for row, col in sub_positions:
        new_row = row + dr * distance
        new_col = col + dc * distance
        ship_grid[new_row][new_col] = 'S'

    # Clean any 'x' or ' ' characters by replacing them with '.'
    for i, row in enumerate(ship_grid):
        for j, val in enumerate(row):
            if val in ['x', ' ']:
                ship_grid[i][j] = '.'

    return ship_grid