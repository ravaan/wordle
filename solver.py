#solver.py
class Solver:
    def __init__(self, word, length, difficulty, guesses, solution, slow) -> None:
        self.word = word
        self.length = length
        self.difficulty = difficulty
        self.guesses = guesses
        self.solution = solution
        self.slow = slow

    def solve(self):
        pass