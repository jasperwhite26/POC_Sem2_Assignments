grid = [
    ["01", "02", "03", "04", "05", "06"],     # [R0C0, R0C1, R0C2]
    ["11", "12", "13", "14", "15", "16"],
    ["21", "22", "23", "24", "25", "26"],
    ["31", "32", "33", "44", "45", "46"],
    ["51", "52", "53", "54", "55", "56"],
    ["61", "62", "63", "64", "65", "66"],
    ["71", "72", "73", "74", "75", "76"]
]

current_piece = "R"

def print_grid():
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if col != 6:
                print(grid[col], sep="  ")            
            else:
                print()

def is_bad_num_string(choice : str):
    if (choice.isnumeric() and int(choice) >= 1 and int(choice) <= 7):
        return False
    return True
                
def is_bad_choice(choice : str):
    if(choice.__eq__("STOP")):
        return False
    return is_bad_num_string(choice)

def get_row(grid_spot):
    if grid_spot == 1 or grid_spot == 2 or grid_spot == 3:
        return 0
    elif grid_spot == 4 or grid_spot == 5 or grid_spot == 6:
        return 1
    else:
        return 2    

def get_col(grid_spot):
    if grid_spot == 1 or grid_spot == 4 or grid_spot == 7:
        return 0
    elif grid_spot == 2 or grid_spot == 5 or grid_spot == 8:
        return 1
    else:
        return 2
    
def place_piece(grid_spot : int):
    while(True):
        col = get_col(grid_spot)
        grid_value = grid[col]
        if (not grid_value.__eq__("R") and not grid_value.__eq__("Y")):
            break
        user_choice = ""
        while (is_bad_num_string(user_choice)):
            user_choice = input(
                "Bad Choice. Enter a number (1-7) where to put the piece: ")
        grid_spot = int(user_choice)
    col = int(user_choice)

def check_row():
    first_list = [last_col, last_col + 1, last_col + 2, last_col + 3]
    second_list = [last_col - 1, last_col, last_col + 1, last_col + 2]
    third_list = [last_col - 2 last_col -1, last_col, last_col + 1]
    fourth_list = [last_col - 3, last_col -2, last_col -1, last_col]

    if(first_list[0] >= 0 and first_list[0] < 7 and first_list[3] >=0 and first_list[3] < 7):
        one = grid[last_row][first_list[0]]
        two = grid[last_row][first_list[1]]
        three = grid[last_row][first_list[2]]
        fourth = grid[last_row][first_list[3]]
    if(second_list[0] >= 0 and second_list[0] < 7 and second_list[3] >=0 and second_list[3] < 7):
        one = grid[last_row][second_list[0]]
        two = grid[last_row][second_list[1]]
        three = grid[last_row][second_list[2]]
        fourth = grid[last_row][second_list[3]]
    if(third_list[0] >= 0 and third_list[0] < 7 and third_list[3] >=0 and third_list[3] < 7):
        one = grid[last_row][third_list[0]]
        two = grid[last_row][third_list[1]]
        three = grid[last_row][third_list[2]]
        fourth = grid[last_row][third_list[3]]
    if(fourth_list[0] >= 0 and fourth_list[0] < 7 and fourth_list[3] >=0 and fourth_list[3] < 7):
        one = grid[last_row][fourth_list[0]]
        two = grid[last_row][fourth_list[1]]
        three = grid[last_row][fourth_list[2]]
        fourth = grid[last_row][fourth_list[3]]
    
def check_col():
    for col in range(4):
        if grid[0][col].__eq__(grid[1][col]) and grid[1][col].__eq__(grid[2][col] and grid[col][2].__eq__(grid[col][3])):
            return True
    return False

def check_left_diag():
    return grid[0][0].__eq__(grid[1][1]) and grid[1][1].__eq__(grid[2][2])

def check_right_diag():
    return grid[0][2].__eq__(grid[1][1]) and grid[1][1].__eq__(grid[2][0])

def check_draw():
    for row in range(3):
        for col in range(3):
            if grid[row][col].isnumeric():
                return False  
    return True

def check_game_over():
    if check_row():
        print(current_piece + " wins!")
        return True
    elif check_col():
        print(current_piece + " wins!")
        return True
    elif check_left_diag():
        print(current_piece + " wins!")
        return True
    elif check_right_diag():
        print(current_piece + " wins!")
        return True
    elif check_draw():
        print("The Game Ends in a Draw!")
        return True
    else:
        return False

def game_loop():
    global current_piece
    print("Welcome to TIC TAC TOE")
    user_choice = ""
    while(True):
        print_grid()
        while(is_bad_choice(user_choice)):
            user_choice = input("Enter STOP to end.  Or a number (1-9) where to put the piece: ")
        if user_choice.__eq__("STOP"):
            break
        grid_spot = int(user_choice)
        place_piece(grid_spot)
        if(check_game_over()):
            print_grid()
            break
        current_piece = "Y" if current_piece.__eq__("R") else "R"
        user_choice = ""
    print("GAME OVER")
        
game_loop()