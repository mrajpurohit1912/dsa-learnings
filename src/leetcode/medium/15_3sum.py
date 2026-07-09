from typing import List

class Solution:
    def threeSumBruteForce(self, nums: List[int]) -> List[List[int]]:
        """
        Brute Force Approach: Try all combinations of triplets.
        Time Complexity: O(n^3)
        Space Complexity: O(1) extra space (ignoring output)
        """
        triplets = []
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = sorted([nums[i], nums[j], nums[k]])
                        if triplet not in triplets:
                            triplets.append(triplet)
        return triplets

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Optimized Approach: Sort the array and use Two Pointers.
        Time Complexity: O(n^2)
        Space Complexity: O(log n) or O(n) depending on sorting implementation
        """
        triplets = []
        nums.sort()
        n = len(nums)

        for i in range(n - 2):
            # Avoid duplicate elements for the first position
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicate elements for left and right pointers
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return triplets

if __name__ == "__main__":
    input_array = [-1, 0, 1, 2, -1, -4]
    sl = Solution()
    
    print("--- 3Sum Demo ---")
    print(f"Input: {input_array}")
    print(f"Brute Force Result: {sl.threeSumBruteForce(input_array)}")
    print(f"Optimized Result:   {sl.threeSum(input_array)}")