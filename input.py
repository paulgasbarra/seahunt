def get_row():
    while True:
        try:
            row = int(input("Row: "))
            if 1 <= row <= 10:
                # decrement for grid
                return row - 1
            else:
                print("Invalid choice. Please choose again.")
        except ValueError:
            print("Invalid choice. Please choose again.")
    
def get_col():
    alpha = "ABCDEFGHIJabcdefghij"
    while True:
        try: 
            col = input("Col: ")
            if col in alpha and len(col) == 1:
                return alpha.index(col) % 10
            else:
                print("Invalid choice. Please choose again.")
        except ValueError:
            print("Invalid choice. Please choose again.")

