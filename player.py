class HumanPlayer:


    def __init__(self,side) -> None:
        self.side=side


    def make_move(self,board) -> tuple:
       col=input(f"enter the col you want to place \"{side}\":")
       row=input(f"enter the col you want to place \"{side}\":")
       return (col,row)



class ComputerPlayer:

    def __init__(self,side) -> None:
        self.side=side


    def make_move(self,board) -> tuple:
        pass