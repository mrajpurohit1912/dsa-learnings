class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        max_value = -float("inf")
        max_str = ""

        n = len(s)
        for i in range(n):
            temp_max_str = ""
            for j in s[i:]:
                if j in temp_max_str:
                    break
                
                temp_max_str += j
                
            
            if len(temp_max_str) > len(max_str):
                max_value = len(temp_max_str)
                max_str = temp_max_str
        return max_value


if __name__ == "__main__":
    sl = Solution()
    ans = sl.lengthOfLongestSubstring("pwwkew")
    print(f"Ans: {ans}")


