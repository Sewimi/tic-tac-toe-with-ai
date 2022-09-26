from main import Game

class HumanPlayer:


    def __init__(self,side) -> None:
        self.side=side


    def make_move(self,board=None) -> tuple:
       col=int(input(f"enter the col you want to place \"{self.side}\": "))
       row=int(input(f"enter the row you want to place \"{self.side}\": "))
       return (col,row)



class ComputerPlayer:

    def __init__(self,side) -> None:
        self.side=side


    def make_move(self,board):
        

        col,row=self.minimax(board,5,True)

    def minimax(self,board,depth,maximizingPlayer):
        
        x=Game.check_win()
            if x[1]== True:
                winner=x[0]
                if winner == self.side:                    
                    return 1
                else:
                    return -1
        
        
        if depth == 0:   #or game is over
            return 0
            

        