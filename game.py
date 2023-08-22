import random
import pandas as pd


class Sudoku:
    symbols = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "Z",
        "!",
    ]

    def __init__(self, size=3) -> None:
        self.size = size

    def __repr__(self) -> str:
        pass

    def __str__(self) -> str:
        pass

    def create_board(self):
        pass

        return board


class Player:
    def __init__(self) -> None:
        pass

    def __repr__(self) -> str:
        pass

    def __str__(self) -> str:
        pass


game1 = Sudoku()
nums = game1.create_board()
print(nums)
