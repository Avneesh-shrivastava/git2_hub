
board = [" "] * 9 

def ttt():
    print(f"\n {board[0]} "+"|"+f" {board[1]} "+"|"+f" {board[2]} \n"+ 
        "---+---+---\n"+
        f" {board[3]} "+"|"+f" {board[4]} "+"|"+f" {board[5]} \n"+
        "---+---+---\n"+
        f" {board[6]} "+"|"+f" {board[7]} "+"|"+f" {board[8]} ",end="")
    

def applying_x():
    if player_x == 1:
        board[0] = "X"
        ttt()
    elif player_x == 2:
        board[1] = "X"
        ttt()
    elif player_x == 3:
        board[2] = "X" 
        ttt()
    elif player_x == 4:
        board[3] = "X" 
        ttt()
    elif player_x == 5:
        board[4] = "X" 
        ttt()
    elif player_x == 6:
        board[5] = "X" 
        ttt()
    elif player_x == 7:
        board[6] = "X" 
        ttt() 
    elif player_x == 8:
        board[7] = "X" 
        ttt()
    elif player_x == 9:
        board[8] = "X" 
        ttt()

def applying_o():
    if player_o == 1:
        board[0] = "O"
        ttt()
    elif player_o == 2:
        board[1] = "O"
        ttt()
    elif player_o == 3:
        board[2] = "O" 
        ttt()
    elif player_o == 4:
        board[3] = "O" 
        ttt()
    elif player_o == 5:
        board[4] = "O" 
        ttt()
    elif player_o == 6:
        board[5] = "O" 
        ttt()
    elif player_o == 7:
        board[6] = "O" 
        ttt() 
    elif player_o == 8:
        board[7] = "O" 
        ttt()
    elif player_o == 9:
        board[8] = "O" 
        ttt()

ttt()

status = ""

running = True
while running:
    while True:
        try:
            player_x = int(input("\n\nPlayer X : choose position (1-9) : "))
            player_x = int(player_x)
            applying_x()
            break
        except ValueError:
            print("An error occoured")

    # #index = 0,1,2
    if board[0] == "X" and board[1] == "X" and board[2] == "X":
        status = "x_win"
        running = False
        
    elif board[0] == "O" and board[1] == "O" and board[2] == "O":
        status = "o_win"
        running = False

    #index = 0,3,6
    elif board[0] == "X" and board[3] == "X" and board[6] == "X":
        status = "x_win"
        running = False
    elif board[0] == "O" and board[3] == "O" and board[6] == "O":
        status = "o_win"
        running = False

    #index = 1,4,7
    elif board[1] == "X" and board[4] == "X" and board[7] == "X":
        status = "x_win"
        running = False
    elif board[1] == "O" and board[4] == "O" and board[7] == "O":
        status = "o_win"
        running = False       

    #index = 2,5,8
    elif board[2] == "X" and board[5] == "X" and board[8] == "X":
        status = "x_win"
        running = False
    elif board[2] == "O" and board[5] == "O" and board[8] == "O":
        status = "o_win"
        running = False    

    #index = 3,4,5
    elif board[3] == "X" and board[4] == "X" and board[5] == "X":
        status = "x_win"
        running = False
    elif board[3] == "O" and board[4] == "O" and board[5] == "O":
        status = "o_win" 
        running = False
    
    #index = 6,7,8
    elif board[6] == "X" and board[7] == "X" and board[8] == "X":
        status = "x_win"
        running = False
    elif board[6] == "O" and board[7] == "O" and board[8] == "O":
        status = "o_win" 
        running = False

    #index = 0,4,8
    elif board[0] == "X" and board[4] == "X" and board[8] == "X":
        status = "x_win"
        running = False
    elif board[0] == "O" and board[4] == "O" and board[8] == "O":
        status = "o_win"
        running = False 

    #index = 6,4,2
    elif board[6] == "X" and board[4] == "X" and board[2] == "X":
        status = "x_win"
        running = False
    elif board[6] == "O" and board[4] == "O" and board[2] == "O":
        status = "o_win" 
        running = False

    #index = 1,4,7
    elif board[1] == "X" and board[4] == "X" and board[7] == "X":
        status = "x_win"
        running = False
    elif board[1] == "O" and board[4] == "O" and board[7] == "O":
        status = "o_win"
        running = False

    while True:
        try:
            if status != "x_win":
                player_o = int(input("\n\nPlayer O : choose position (1-9) : "))
                player_o = int(player_o)
                applying_o()
            break
        except ValueError:
            print("An error occured")

if status == "x_win":       
    print("\n\nplayer_X win's\n")
elif status == "o_win":
    print("\n\nplayer_O win's\n")
else :
    print("\nTie\n")
    
  
