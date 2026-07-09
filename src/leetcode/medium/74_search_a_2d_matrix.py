from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Searches for a target value in an m x n 2D matrix.
        The matrix has properties:
        1. Integers in each row are sorted from left to right.
        2. The first integer of each row is greater than the last integer of the previous row.
        
        Approach: Treat the 2D matrix as a 1D sorted list and perform binary search.
        Time Complexity: O(log(m * n))
        Space Complexity: O(1)
        """
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        low, high = 0, m * n - 1

        while low <= high:
            mid = (low + high) // 2
            # Map mid index back to 2D coordinates
            row = mid // n
            col = mid % n
            val = matrix[row][col]

            if val == target:
                return True
            elif val < target:
                low = mid + 1
            else:
                high = mid - 1

        return False

if __name__ == "__main__":
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    sl = Solution()
    targets = [3, 13, 30, 65]
    print("--- Search a 2D Matrix Demo ---")
    for t in targets:
        print(f"Searching for {t} -> Found: {sl.searchMatrix(matrix, t)}")