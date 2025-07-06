# 74 - Search a 2D Matrix
# Runtime = 0ms, Beats = 100%

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        i = 0
        def bettersearch(matrix, i, target, high, low):
            while(high >= low):
                mid = (high+low)//2
                if(target == matrix[i][mid]):
                    return True
                elif(target > matrix[i][mid]):
                    low = mid + 1
                else:
                    high = mid - 1
            return False
        while(i < row-1):
            if (target>=matrix[i][0] and target<matrix[i+1][0]):	# to determine what row the target belongs to
                return bettersearch(matrix, i, target, col-1, 0)	# then we perform binary search on that row
            else:
                i += 1
        return bettersearch(matrix, row-1, target, col-1, 0)