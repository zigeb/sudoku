import random


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
        chars = Sudoku().symbols[: self.size**2]
        board_dict = {k: [] for k in range(self.size**2)}
        board_dict = {}
        for i in range(self.size):
            random.shuffle(chars)
            if i == 0:
                for j in range(self.size):
                    if j == 0:
                        for k in range(self.size):
                            board_dict[k] = chars[k * self.size : self.size * (k + 1)]
                    else:
                        random.shuffle(chars)
                        foo_dict = {k: [] for k in chars}
                        for c in chars:
                            for k, v in board_dict.items():
                                if c not in v:
                                    foo_dict[c].append(k)
                        bar_dict = {}
                        for v in foo_dict.values():
                            for z in v:
                                if z in bar_dict:
                                    bar_dict[z][0] += 1
                                else:
                                    bar_dict[z] = [1, 0]

                        for c in chars:
                            print(f"Character: {c}")
                            for b in bar_dict.keys():
                                print(f"Board dict key available with highest no :{b}")
                                if b in foo_dict[c]:
                                    print(f"possible key in board dict {foo_dict[c]}")

                                    board_dict[b].append(c)
                                    print(f"Board dict key {b}: {board_dict[b]}")
                                    print()
                                    bar_dict[b][0] -= 1
                                    bar_dict[b][1] += 1
                                    if bar_dict[b][1] == 3:
                                        bar_dict.pop(b)
                                        print(f"Board dict key is full: {b}")
                                        print()

                                    bar_dict = {
                                        k: v
                                        for k, v in sorted(
                                            bar_dict.items(),
                                            key=lambda x: x[1],
                                            reverse=True,
                                        )
                                    }
                                    break

                """ print(foo_dict)
                print(bar_dict) """

        return board_dict


class Player:
    def __init__(self) -> None:
        pass

    def __repr__(self) -> str:
        pass

    def __str__(self) -> str:
        pass


game1 = Sudoku(3)
nums = game1.create_board()
print(nums)
