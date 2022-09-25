import player

class Game:

    def __init__(self,player1,player2) -> None:
        self.board=["." for i in range (9)]
        self.player1=player1
        self.player2=player2
        self.turn='p1'


    def print_board(self):
        print("|--------|")
        for i,val in enumerate(self.board):
            print("|",val,end="")
            if (i+1) %3 ==0:
                print("|")
                print("|--------|")


    def check_valid_move(self,col,row):
        if [3*row + col] != ".":
            print("invalid move")
            return False
        return True


    def check_win(self) -> bool:
        return True

    def change_turn(self):
        if self.turn=='p1':
            self.turn='p2'
        if self.turn=='p2':
            self.turn='p1'



    def make_move(self,player,position):

        col,row=player.make_move()

        if self.check_valid_move(col,row):
            
            self.board[3*row + col] = player.side

            self.change_turn()
        else:
            self.make_move(player,position)


    def game_loop(self):

        while True:

            if self.check_win():
                break

            self.print_board()

            if self.turn=='p1':
                self.make_move(self.player1)
            if self.turn=='p2':
                self.make_move(self.player2)



p1=player.HumanPlayer("o")
p2=player.HumanPlayer("x")

game=Game(p1,p2)

game.print_board()






  