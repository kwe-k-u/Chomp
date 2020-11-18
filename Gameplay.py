class GamePlay:
    def __init__(self, rows=5, columns=5):
        self.rows, self.columns = rows, columns
        self.possibleMoves = []
        # Gameboard
        for i in range(rows):
            print()
            for j in range(columns):
                print("# ", end="")
                self.possibleMoves.append((i + 1, j + 1))
    


