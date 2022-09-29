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
        



    def make_move(self,board):

       
        from main import Game
        
       

        
        

        def minimax(board,depth,maximizingPlayer,mv_made):
            col = mv_made%3
            row = mv_made//3

            x=Game.check_win(col,row,self.side,board)
            if x[0]== True:
                winner=x[1]
                if winner == self.side:                    
                    return 1 #win1,draw0/lose-1
                else:
                    return -1

            x=Game.check_win(col,row,"o",board)
            if x[0] == True:
                winner=x[1]
                if winner == self.side:                    
                    return 1 #win1,draw0/lose-1
                else:
                    return -1
                    
            if depth == 0 or Game.give_valid_moves(board) == []:   
                return 0
            
            if maximizingPlayer:
                moves=[-1]
                for i in Game.give_valid_moves(board):

                    board[i] = self.side
                    win=minimax(board,depth-1,False,i)
                    moves.append(win)
                    board[i] = "."
                return max(moves)

            else:

                  moves=[1]
                  for i in Game.give_valid_moves(board):

                    board[i] = "o"
                    win=minimax(board,depth-1,True,i)
                    moves.append(win)
                    board[i] = "."

                  return min(moves)

        mvs=[]
        for i in Game.give_valid_moves(board):

            board[i] = self.side
            w=minimax(board,6,False,i)
            mvs.append((i,w))
            board[i] = "."


        highest=-1
        x=0
        for i in mvs:
            if i[1]>highest:
                highest=i[1]
                x=i[0]


        col = x%3
        row = x//3
        print(col,row)
        return (col,row)
        # return (random.randint(0,2),random.randint(0,2))