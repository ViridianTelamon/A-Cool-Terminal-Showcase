#Menu Screen.
print("""
  ___    _____             _   _____                   _             _   _____ _                                     
 / _ \  /  __ \           | | |_   _|                 (_)           | | /  ___| |                                    
/ /_\ \ | /  \/ ___   ___ | |   | | ___ _ __ _ __ ___  _ _ __   __ _| | \ `--.| |__   _____      _____ __ _ ___  ___ 
|  _  | | |    / _ \ / _ \| |   | |/ _ \ '__| '_ ` _ \| | '_ \ / _` | |  `--. \ '_ \ / _ \ \ /\ / / __/ _` / __|/ _ |
| | | | | \__/\ (_) | (_) | |   | |  __/ |  | | | | | | | | | | (_| | | /\__/ / | | | (_) \ V  V / (_| (_| \__ \  __/
\_| |_/  \____/\___/ \___/|_|   \_/\___|_|  |_| |_| |_|_|_| |_|\__,_|_| \____/|_| |_|\___/ \_/\_/ \___\__,_|___/\___|
""")

print("\nBy:  ViridianTelamon.")

print("\n----------------------------------------")

print("\nThis Showcase Is Just A Showcase Where You Can Move Around In A Certain Area And Push A Box Around By Entering In Certain Characters To Do Certain Actions And Stuff Like That.  You Play As The Letter O And You Can Move Around As The Letter O As Well.  You Can Push Around A Box Which Is The Letter D. The Controls Of The Game Should Be Near The Game Area Or Around The Game Area In General.  It Is Cool.")

print("\n----------------------------------------")


#Board.
board = [
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
        ]

player = "O"

player_position = [0, 0]

board[player_position[0]][player_position[1]] = player

player_y, player_x = player_position

box = "D"

box_position = [5, 5]

board[box_position[0]][box_position[1]] = box

#The Game.
run = True

while run:
    #Board Generation.
    print("\n\n")
    print(" ________________________________________________ ")
    print(*board, sep="\n")
    print(" \u203e\u203e\u203e\u203e\u203e\u203e\u203e\u203e\u203e\u203e\u203e\u203e\u203e\u203e\u203e\u203e\u203e\u203e\u203e\u203e\u203e\u203e\u203e\u203e\u203e\u203e\u203e\u203e\u203e\u203e\u203e\u203e\u203e\u203e\u203e\u203e\u203e\u203e\u203e\u203e\u203e\u203e\u203e\u203e\u203e\u203e\u203e\u203e ")

    board[player_position[0]][player_position[1]] = "."

    board[box_position[0]][box_position[1]] = "."
    
    #Player Movement.
    movement = input("\nEnter In Either W A S D To Move Your Character Or Enter In E To Exit This Program:  ")

    movement = movement.lower()

    player_position_used = [player_position[0], player_position[1]]

    match movement:
        case "w":
            if box_position[0] > 0:
                if [player_position[0] - 1, player_position[1]] == box_position:
                    box_position[0] -= 1
                    player_position[0] += 0
            
            if player_position[0] > 0:
                player_position[0] -= 1
        case "a":
            if box_position[1] > 0:
                if [player_position[0], player_position[1] - 1] == box_position:
                    box_position[1] -= 1
                    player_position[1] += 0

            if player_position[1] > 0:
                player_position[1] -= 1
        case "s":
            if box_position[0] < 9:
                if [player_position[0] + 1, player_position[1]] == box_position:
                    box_position[0] += 1
                    player_position[0] -= 0

            if player_position[0] < 9:
                player_position[0] += 1
        case "d":
            if box_position[1] < 9: 
                if [player_position[0], player_position[1] + 1] == box_position:
                    box_position[1] += 1
                    player_position[1] -= 0

            if player_position[1] < 9: 
                player_position[1] += 1
        case "e":
            run = False
    
    if player_position[0] == box_position[0] and player_position[1] == box_position[1]:
        player_position[0] = player_position_used[0]
        player_position[1] = player_position_used[1]
    
    board[player_position[0]][player_position[1]] = player

    board[box_position[0]][box_position[1]] = box