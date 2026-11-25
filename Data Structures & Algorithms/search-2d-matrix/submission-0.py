class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])
        low, high = 0, r * c

        while low <= high:
            mid = (low + high) // 2
            row = mid // c
            col = mid % c
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = mid+1
            else:
                high = mid-1
        return False
        