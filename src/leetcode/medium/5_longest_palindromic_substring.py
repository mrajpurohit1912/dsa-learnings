
# create a new string add the element into new string
# but for that we need to check or add element into a new string so that the it becomes a palindromic string


class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest= ""



        for i in range(len(s)):
            for j in range(i,len(s)):

                substring = s[i : j + 1]

        
                if (len(substring) > len(longest)) & (substring == substring[::-1]): 
                    longest = substring

        return longest




if __name__ == "__main__":
    sl = Solution()
    test_cases = ["babad", "cbbd", "a", "racecar"]
    print("--- Longest Palindromic Substring Demo ---")
    for s in test_cases:
        print(f"Input: '{s}' -> Longest Palindrome: '{sl.longestPalindrome(s)}'")
