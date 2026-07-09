from typing import List

class BacktrackingDemo:
    @staticmethod
    def permute(nums: List[int]) -> List[List[int]]:
        """
        Finds all permutations of a list of distinct integers.
        Time Complexity: O(n * n!)
        Space Complexity: O(n) for the recursion stack
        """
        result = []
        
        def backtrack(start: int):
            if start == len(nums):
                result.append(nums[:])
                return
            
            for i in range(start, len(nums)):
                # Swap elements
                nums[start], nums[i] = nums[i], nums[start]
                # Recurse
                backtrack(start + 1)
                # Backtrack / Restore state
                nums[start], nums[i] = nums[i], nums[start]
                
        backtrack(0)
        return result

    @staticmethod
    def subsets(nums: List[int]) -> List[List[int]]:
        """
        Finds all possible subsets (power set) of a list of integers.
        Time Complexity: O(n * 2^n)
        Space Complexity: O(n)
        """
        result = []
        path = []
        
        def backtrack(index: int):
            result.append(path[:])
            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()  # Backtrack
                
        backtrack(0)
        return result

if __name__ == "__main__":
    demo = BacktrackingDemo()
    print("--- Permutations Demo ---")
    nums = [1, 2, 3]
    print(f"Permutations of {nums}:")
    for p in demo.permute(nums):
        print(p)

    print("\n--- Subsets Demo ---")
    print(f"Subsets of {nums}:")
    for s in demo.subsets(nums):
        print(s)
