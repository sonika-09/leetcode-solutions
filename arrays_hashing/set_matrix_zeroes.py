# 73 - Set Matrix Zeroes
# Runtime = 2ms, Beats = 83.03%

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        zero_row = set()
        zero_col = set()
        for i in range(row):
            for j in range(col):
                if(matrix[i][j] == 0):
                    zero_row.add(i)
                    zero_col.add(j)
        for i in zero_row:
            for j in range(col):
                matrix[i][j] = 0
        for j in zero_col:
            for i in range(row):
                matrix[i][j] = 0
        return matrix