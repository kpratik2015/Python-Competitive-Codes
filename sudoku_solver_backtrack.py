import collections

# Problem: https://leetcode.com/problems/sudoku-solver/
# Solved By: https://leetcode.com/problems/sudoku-solver/discuss/140837/Python-very-simple-backtracking-solution-using-dictionaries-and-queue-~100-ms-beats-~90

class Solution:
    def solveSudoku(self, board):
        rows, cols, triples, visit = collections.defaultdict(set), collections.defaultdict(set), collections.defaultdict(set), collections.deque([])
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    rows[r].add(board[r][c]) # add digit to r row
                    cols[c].add(board[r][c]) # add digit to c column
                    triples[(r // 3, c // 3)].add(board[r][c]) # add digit for 3x3 grid stored in triples
                else:
                    visit.append((r, c))  # add x,y to be visited
        print(f"We have:\n\nRows: {rows}\n\nColumns: {cols}\n\nTriples: {triples}\n\nTo Visit: {visit}\n\n")
        def dfs():
            if not visit: # done condition is when nothing is there to visit
                return True
            r, c = visit[0]
            t = (r // 3, c // 3)
            for dig in {"1", "2", "3", "4", "5", "6", "7", "8", "9"}:
                if dig not in rows[r] and dig not in cols[c] and dig not in triples[t]: # looking for unused digit
                    board[r][c] = dig # assigning digit in-place
                    # adding digit as used to rows, cols and triples
                    rows[r].add(dig)
                    cols[c].add(dig)
                    triples[t].add(dig)
                    visit.popleft() # pop from visit queue
                    if dfs(): # recrusion on moving forward with this digit assigned
                        return True # return True when all paths in this recursion are successful
                    else:  # not able to find an unused digit, fail path, backtrack
                        # print(f"Backtracking for digit {dig} which was placed at ({r},{c})")
                        board[r][c] = "."  # mark unsolved in board
                        # remove digit from rows, cols and triples
                        rows[r].discard(dig)
                        cols[c].discard(dig)
                        triples[t].discard(dig)
                        visit.appendleft((r, c)) # re-insert in queue as the next visit
            return False
        dfs()

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Solution().solveSudoku(board)

print(board)

"""
We have:

Rows: defaultdict(<class 'set'>, {0: {'3', '7', '5'}, 1: {'1', '9', '6', '5'}, 2: {'6', '9', '8'}, 3: {'6', '3', '8'}, 4: {'3', '1', '4', '8'}, 5: {'6', '7', '2'}, 6: {'8', '2', '6'}, 7: {'9', '1', '4', '5'}, 8: {'7', '9', '8'}})

Columns: defaultdict(<class 'set'>, {0: {'7', '4', '6', '5', '8'}, 1: {'3', '9', '6'}, 4: {'7', '9', '2', '1', '8', '6'}, 3: {'1', '4', '8'}, 5: {'3', '9', '5'}, 2: {'8'}, 
7: {'8', '7', '6'}, 8: {'3', '9', '1', '5', '6'}, 6: {'2'}})

Triples: defaultdict(<class 'set'>, {(0, 0): {'3', '9', '6', '5', '8'}, (0, 1): {'1', '7', '9', '5'}, (0, 2): {'6'}, (1, 0): {'7', '4', '8'}, (1, 1): {'8', '3', '2', '6'}, 
(1, 2): {'3', '1', '6'}, (2, 0): {'6'}, (2, 2): {'7', '9', '2', '5', '8'}, (2, 1): {'9', '1', '4', '8'}})

To Visit: deque([(0, 2), (0, 3), (0, 5), (0, 6), (0, 7), (0, 8), (1, 1), (1, 2), (1, 6), (1, 7), (1, 8), (2, 0), (2, 3), (2, 4), (2, 5), (2, 6), (2, 8), (3, 1), (3, 2), (3, 3), (3, 5), (3, 6), (3, 7), (4, 1), (4, 2), (4, 4), (4, 6), (4, 7), (5, 1), (5, 2), (5, 3), (5, 5), (5, 6), (5, 7), (6, 0), (6, 2), (6, 3), (6, 4), (6, 5), (6, 8), (7, 0), (7, 1), (7, 2), (7, 6), (7, 7), (8, 0), (8, 1), (8, 2), (8, 3), (8, 5), (8, 6)])
"""