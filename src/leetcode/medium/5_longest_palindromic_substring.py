class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Finds the longest palindromic substring in s.
        Approach: Expand Around Center
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        if not s:
            return ""

        start, end = 0, 0

        def expand_around_center(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Length of palindrome is (right - 1) - (left + 1) + 1 = right - left - 1
            return right - left - 1

        for i in range(len(s)):
            # Odd length palindromes (single character center)
            len1 = expand_around_center(i, i)
            # Even length palindromes (two character center)
            len2 = expand_around_center(i, i + 1)
            
            max_len = max(len1, len2)
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]

if __name__ == "__main__":
    sl = Solution()
    test_cases = ["babad", "cbbd", "a", "racecar"]
    print("--- Longest Palindromic Substring Demo ---")
    for s in test_cases:
        print(f"Input: '{s}' -> Longest Palindrome: '{sl.longestPalindrome(s)}'")