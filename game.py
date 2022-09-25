from sys import ps1
import player

class Game:

    def __init__(self,playerO,playerX) -> None:
        self.board=["." for i in range (9)]


    def print_board(self):
        pass


    def check_valid_move(self):
        pass


    def check_win(self) -> bool:
        return True


    def make_move(self,player,position):
        if self.check_valid_move(player.make_move()):
            col,row=player.make_move()
            self.board = player.side[3*row + col]
        else:
            self.make_move()


    def game_loop(self):

        while True:

            if self.check_win():
                break

            self.print_board()

            self.make_move()



p1=player.HumanPlayer("o")
p2=player.HumanPlayer("x")

game=Game()






  