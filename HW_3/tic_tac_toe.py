def printed_menu():
    print ("""
        (9) -> Top    rigth
        (8) -> Top     center
        (7) -> Top     left
        (6) -> Middle  rigth
        (5) -> Middle  center
        (4) -> Middle  left
        (3) -> Bottom  rigth
        (2) -> Bottom  center
        (1) -> Bottom  left
        """) 

def valid_input(player, data):
    print("Player {}:".format(player))
    selected_option = input()

    valid_options = str([index+1 for (index, choice) in enumerate(data) if choice == 'E'])
    
    while selected_option not in valid_options:
        print("Invalid input")
        print("Player {}:".format(player))
        selected_option = input()

    if player == 1:
        data[int(selected_option)-1] = 'x'
    elif player == 2:
        data[int(selected_option)-1] = 'o'
    return selected_option

def map_update(player, data):

    E_indexes = [index for (index, choice) in enumerate(data) if choice == 'E']
    data_copy = data.copy()
    for index in E_indexes:
        data_copy[index] = ' '


    print("""
      {}  |  {}  |  {}
    -----------------
      {}  |  {}  |  {}
    -----------------
      {}  |  {}  |  {}
    """.format(data_copy[6], data_copy[7], data_copy[8], data_copy[3], data_copy[4], data_copy[5], data_copy[0], data_copy[1], data_copy[2]))

def check_game_status(player, data):  
    win_con = ('xxx', 'ooo')
    bot_row   = data[0]+data[1]+data[2]
    mid_row   = data[3]+data[4]+data[5]
    top_row   = data[6]+data[7]+data[8]
    left_col  = data[6]+data[3]+data[0]
    mid_col   = data[7]+data[4]+data[1]
    right_col = data[8]+data[5]+data[2]
    cross_1   = data[6]+data[4]+data[2]
    cross_2   = data[0]+data[4]+data[8]
    game_state = [bot_row, mid_row, top_row, left_col, mid_col, right_col, cross_1, cross_2]

    for state in game_state:
        if state in win_con:
            print("player {} won!!".format(player))
            exit()
        
data = 9 * ['E']  
printed_menu()
turn = 1
while 'E' in data:
    if turn%2 == 0:
        player = 2
    else:
        player = 1
        
    valid_input(player, data)
    map_update(player, data)
    check_game_status(player, data)
    turn += 1
print("It's a draw!!")
