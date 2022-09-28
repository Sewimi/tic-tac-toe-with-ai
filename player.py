import random

class HumanPlayer:


    def __init__(self,side) -> None:
        self.side=side


    def make_move(self,board=None):
       col=int(input(f"enter the col you want to place \"{self.side}\": "))
       row=int(input(f"enter the row you want to place \"{self.side}\": "))
       return (col,row)



class ComputerPlayer:

    def __init__(self,side) -> None:
        self.side=side
        self.f1=True
        



    def make_move(self,board):

       
        from main import Game
        
       

        
        

        def minimax(board,depth,maximizingPlayer):
            
            x=Game.check_win(1,1,self.side,board)
            if x[1]== True:
                winner=x[0]
                if winner == self.side:                    
                    return 1
                else:
                    return -1
                    
            if depth == 0:   
                return 0
            
            if maximizingPlayer:
                pass
            else:
                pass
        
        # col,row=minimax(board,5,True)

        return (random.randint(0,2),random.randint(0,2))
            
     