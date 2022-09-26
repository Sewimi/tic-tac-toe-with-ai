class HumanPlayer:


    def __init__(self,side) -> None:
        self.side=side


    def make_move(self) -> tuple:
       col=int(input(f"enter the col you want to place \"{self.side}\": "))
       row=int(input(f"enter the row you want to place \"{self.side}\": "))
       return (col,row)



class ComputerPlayer:

    def __init__(self,side) -> None:
        self.side=side


    def make_move(self,board) -> tuple:
        pass