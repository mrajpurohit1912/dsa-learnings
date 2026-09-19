class Solution:
    def isValid(self, s: str) -> bool:
        """
        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
        determines if the input string is valid.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        
        return not stack



if __name__ == "__main__":
    sl = Solution()
    test_cases = ["()[]{}", "([)]", "{[]}", "(]"]
    for test in test_cases:
        print(f"Input: {test} -> Valid: {sl.isValid(test)}")
   