# 79 - Word Search
# Runtime = 6772ms, Beats = 36.54%

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row = len(board)
        col = len(board[0])
        seen = set()
        def check(c, i, j):
            if (c == len(word)):
                return True
            if((i<0 or i>=row) or
            (j<0 or j>=col) or
            (word[c] != board[i][j]) or
            (i, j) in seen):
                return False
            seen.add((i, j))
            res = (check(c+1, i-1, j) or
                check(c+1, i+1, j) or
                check(c+1, i, j-1) or
                check(c+1, i, j+1))
            seen.remove((i, j))
            return res
        
        for i in range(row):
            for j in range(col):
                if check(0, i, j):
                    return True
        return False