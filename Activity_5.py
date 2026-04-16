# Subsets
def subsets(nums):
    res = [[]]

    for num in nums:
        res += [curr + [num] for curr in res]

    return res

# Permutation
def permute(nums):
    res = []

    def backtrack(path, remaining):
        if not remaining:
            res.append(path)
            return
        for i in range(len(remaining)):
            backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:])

    backtrack([], nums)
    return res

# Combination sum
def combinationSum(candidates, target):
    res = []

    def backtrack(start, path, total):
        if total == target:
            res.append(path)
            return
        if total > target:
            return

        for i in range(start, len(candidates)):
            backtrack(i, path + [candidates[i]], total + candidates[i])

    backtrack(0, [], 0)
    return res

# N queens
def solveNQueens(n):
    res = []
    board = [["."] * n for _ in range(n)]

    def isValid(row, col):
        for i in range(row):
            if board[i][col] == "Q":
                return False

        i, j = row-1, col-1
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        i, j = row-1, col+1
        while i >= 0 and j < n:
            if board[i][j] == "Q":
                return False
            i -= 1
            j += 1

        return True

    def backtrack(row):
        if row == n:
            res.append(["".join(r) for r in board])
            return

        for col in range(n):
            if isValid(row, col):
                board[row][col] = "Q"
                backtrack(row + 1)
                board[row][col] = "."

    backtrack(0)
    return res

# Sudoku solver
def solveSudoku(board):
    def isValid(r, c, val):
        for i in range(9):
            if board[r][i] == val or board[i][c] == val:
                return False

        box_r, box_c = (r//3)*3, (c//3)*3
        for i in range(box_r, box_r+3):
            for j in range(box_c, box_c+3):
                if board[i][j] == val:
                    return False
        return True

    def backtrack():
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    for num in map(str, range(1, 10)):
                        if isValid(i, j, num):
                            board[i][j] = num
                            if backtrack():
                                return True
                            board[i][j] = "."
                    return False
        return True

    backtrack()
