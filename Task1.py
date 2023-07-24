import random
board=["-","-","-",
       "-","-","-",
       "-","-","-"]

currentplayer="X"
winner=None
gamerunning=True

def printboard(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("----------------")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("----------------")
    print(board[6] + "|" + board[7] + "|" + board[8])
    print("----------------")



def playerinput(board):
    inp=int(input("select the spot  1-9:"))
    if board[inp-1]=="-":
        board[inp-1]=currentplayer 
    else:
        print("This place is taken by someone choose another one")       

def checkhorizontal(board):
    global winner
    if board[0]==board[1]==board[2] and board[0]!="-":
        winner=board[0]
        return True    
    elif board[3]==board[4]==board[5] and board[3]!="-":
        winner=board[0]
        return True    
    if board[6]==board[7]==board[8] and board[6]!="-":
        winner=board[0]
        return True    
def checkrow(board):
    global winner
    if board[0]==board[3]==board[6] and board[0]!="-":
        winner=board[0]
        return True    
    elif board[1]==board[4]==board[7] and board[1]!="-":
        winner=board[0]
        return True    
    if board[3]==board[5]==board[8] and board[3]!="-":
        winner=board[0]
        return True  
def checkdiagonal(board):
    global winner
    if board[0]==board[4]==board[8] and board[0]!="-":
        winner=board[0]
        return True    
    elif board[2]==board[4]==board[6] and board[3]!="-":
        winner=board[0]
        return True    


def checkifwin(board):
    global gamerunning
    if checkhorizontal(board):
        printboard(board)
        print(f"THE WINNER IS {winner}")
        gamerunning=False
    elif checkrow(board):
        printboard(board)
        print(f"THE WINNER IS {winner}")
        gamerunning=False
    elif checkdiagonal(board):
        printboard(board)
        print(f"THE WINNER IS {winner}")
        gamerunning=False        
    

def checkiftie(board):
    global gamerunning
    if "-" not in board :
        printboard(board)
        print("THIS GAME IS A TIE ")
        gamerunning=False   

def switchplayer():
    global currentplayer 
    if currentplayer=="X":
        currentplayer="O"
    else:
        currentplayer="X"

def computer(board):
    while currentplayer=="O":
        position=random.randint(0,8)
        if board[position]=="-":
            board[position]="O"
            switchplayer()


while gamerunning:
    printboard(board)
    playerinput(board)
    checkiftie(board)
    checkifwin(board)
    switchplayer()
    computer(board)
    checkifwin(board)
    checkiftie(board)