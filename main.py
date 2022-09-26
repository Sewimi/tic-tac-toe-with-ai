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


    def check_win(self,side) -> bool:
        f=True
        for i in range(3):
            ch= self.board[3*i]

            if ch == self.board[3*i +1] == self.board[3*i +2] and ch!=".":
                print(f"The winner is {ch}")
                self.print_board()
                return True
            ch= self.board[i]
            if ch== self.board[i + 3] == self.board[i+6] and ch!=".":
                if self.board[0] != ".":
                    print(f"The winner is {ch}")
                    self.print_board()
                    return True

            if all(self.board[0] == self.board[3*x + x] for x in range(3)):
                if self.board[0] != ".":
                    print(f"The winner is {self.board[0]}")
                    self.print_board()
                    return True
            
            if all(self.board[2] == self.board[3*x - x] for x in range(3)):
                if self.board[2] != ".":
                    print(f"The winner is {ch}")
                    self.print_board()
                    return True

        return not ('.' in self.board)

                
                

    def change_turn(self):
        if self.turn=='p1':
            self.turn='p2'
            

        elif self.turn=='p2':
            self.turn='p1'
         



    def make_move(self,player):


        col,row=player.make_move()
        ind =   3*row + col

        self.update_valid_moves(self.board)

        print(self.valid_moves)
        if ind in self.valid_moves:
            
            self.board[ind] = player.side


            self.check_win(ind,player.side)

            self.change_turn()
        else:
            self.make_move(player)


    def game_loop(self):


        while True:

            if self.end:
                print(f"The winner is{self.winner}! Congrats!")
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






  