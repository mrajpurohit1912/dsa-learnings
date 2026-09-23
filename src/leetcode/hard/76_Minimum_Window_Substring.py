# # # min_widow = len(t)
# # # iterate through the s string - starting from min_window,if not able to find the increase the size of window by 1 until windows size reaches is equivalent to the s string
# # how to check that t string is present in s string - wll google it

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not s or not t:
            return ""
        required = Counter(t)
        min_window = len(t)

        while min_window <= len(s):
            start = 0
            end = min_window

            while end <= len(s):
                min_window_string = s[start:end]
                current_count = Counter(min_window_string)

                #if all(char in min_window_string for char in t):
                if current_count >= required:
                    return min_window_string
                else: 
                    start += 1  
                    end += 1

            start =0
            min_window += 1 
            

        return ""

if __name__ == "__main__":

    # s = "ADOBECODEBANC"
    # t = "ABC"
    s = "bbaa"
    t = "aba"
    sl = Solution()
    result = sl.minWindow(s,t)
    print(result)


