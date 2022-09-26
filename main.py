import player

class Game:

    def __init__(self,player1,player2) -> None:
        self.board=["." for i in range (9)]
        self.player1=player1
        self.player2=player2
        self.turn='p1'
        self.valid_moves=[]
        self.winner=None
        self.end=False


    def print_board(self):
        print("|--------|")
        for i,val in enumerate(self.board):
            print("|",val,end="")
            if (i+1) %3 ==0:
                print("|")
                print("|--------|")


    def update_valid_moves(self,board):
        self.valid_moves=[]
        for i,val in enumerate(board):
            if val == ".": self.valid_moves.append(i)


    def check_win(self,col,row,side,board):
       
        
       
        if all(side == board[i*3 + col] for i in range(3)): 
            return (True,side)
        elif all(side == board[row*3 + i] for i in range(3)): 
            return (True,side)           

        if (row*3 + col) % 2 == 0:
            diag1 = [board[i] for i in [0,4,8]]
            if all(side == i for i in diag1):
                return (True,side)

            diag2 = [board[i] for i in [2,4,6]]
            if all(side == i for i in diag2):
                return (True,side)



        return (not ('.' in self.board),side)

                
                

    def change_turn(self):
        if self.turn=='p1':
            self.turn='p2'
            

        elif self.turn=='p2':
            self.turn='p1'
         



    def make_move(self,player):


        col,row=player.make_move()
        ind =   3*row + col

        
        self.update_valid_moves(self.board)

        if ind in self.valid_moves:
            
            self.board[ind] = player.side


            win=self.check_win(col,row,player.side,self.board)
            if win[0] == True:
                self.winner=win[1]
                self.end=True

            self.change_turn()
        else:
            self.make_move(player)


    def game_loop(self):


        while True:

            if self.end:
                print(f"The winner is {self.winner}! Congrats!")
                break
         
            self.print_board()

            if self.turn=='p1':
                self.make_move(self.player1)
            elif self.turn=='p2':
                self.make_move(self.player2)



p1=player.HumanPlayer("o")
p2=player.HumanPlayer("x")

game=Game(p1,p2)

game.game_loop()






  