from typing import List

class Solution:
    def twoSumBruteForce(self, numbers: List[int], target: int) -> List[int]:
        """
        Brute Force Approach: Try all pairs.
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        n = len(numbers)
        for i in range(n):
            for j in range(i + 1, n):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        return []

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Optimized Approach: Two Pointers (since the input is sorted).
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

        return []

if __name__ == "__main__":
    sl = Solution()
    numbers = [2, 7, 11, 15]
    target = 9
    print("--- Two Sum II (Input Array Is Sorted) Demo ---")
    print(f"Numbers: {numbers}, Target: {target}")
    print(f"Brute Force Result: {sl.twoSumBruteForce(numbers, target)}")
    print(f"Optimized Result:   {sl.twoSum(numbers, target)}")