from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Checks if a list contains duplicate elements.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

if __name__ == "__main__":
    sl = Solution()
    test_cases = [
        [1, 2, 3, 1],
        [1, 2, 3, 4],
        [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    ]
    print("--- Contains Duplicate Demo ---")
    for nums in test_cases:
        print(f"Nums: {nums} -> Contains Duplicate: {sl.containsDuplicate(nums)}")