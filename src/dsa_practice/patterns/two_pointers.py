from typing import List

class TwoPointersDemo:
    @staticmethod
    def reverse_array(arr: List[int]) -> List[int]:
        """
        1. Opposite Direction pattern: Reverses an array in-place.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        left, right = 0, len(arr) - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr

    @staticmethod
    def is_palindrome(s: str) -> bool:
        """
        1. Opposite Direction pattern: Checks if a string is a palindrome.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

    @staticmethod
    def remove_duplicates(nums: List[int]) -> int:
        """
        2. Same Direction (Slow/Fast pointer) pattern: Removes duplicates from sorted array.
        Returns the count of unique elements.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not nums:
            return 0
        
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        
        return slow + 1

    @staticmethod
    def merge_sorted_arrays(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        3. Merge sorted arrays in-place using two pointers starting from the end.
        Time Complexity: O(m + n)
        Space Complexity: O(1)
        """
        # Pointers for nums1, nums2, and the end of the merged array
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # Copy remaining elements from nums2 if any
        if p2 >= 0:
            nums1[:p2 + 1] = nums2[:p2 + 1]


if __name__ == "__main__":
    demo = TwoPointersDemo()
    
    print("--- 1. Opposite Direction: Reverse Array ---")
    arr = [1, 2, 3, 4, 5]
    print(f"Original: {arr} -> Reversed: {demo.reverse_array(arr)}")

    print("\n--- 2. Opposite Direction: Is Palindrome ---")
    s = "A man, a plan, a canal: Panama"
    print(f"'{s}' is palindrome -> {demo.is_palindrome(s)}")

    print("\n--- 3. Same Direction: Remove Duplicates ---")
    nums = [1, 1, 2, 2, 3, 4, 4]
    unique_count = demo.remove_duplicates(nums)
    print(f"Array after removing duplicates: {nums[:unique_count]} (Count: {unique_count})")

    print("\n--- 4. Merge Sorted Arrays ---")
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    demo.merge_sorted_arrays(nums1, m, nums2, n)
    print(f"Merged nums1: {nums1}")
