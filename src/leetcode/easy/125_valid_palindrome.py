class Solution:
    def isPalindrome(self, s: str) -> bool:
        start,end = 0,len(s) - 1

        while start < end:
            if not s[start].isalnum():
                start += 1
            elif not s[end].isalnum():
                end -= 1
            elif s[start].lower() != s[end].lower():
                return False
            else:
                start,end = start + 1,end -1
            
        return True




#         # for i in s:
#         #     if i.isalpha():
#         #         new_str += i.lower()
#         # print(f"New_str = {new_str}")
#         # if new_str == new_str[::-1]:
#         #     return True
            
   

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         new_str = ""

#         for i in s:
#             if i.isalpha():
#                 new_str += i.lower()
#         if new_str == new_str[::-1]:
#             return True
            
        
#         return False




if __name__ == "__main__":
    #s = "A man, a plan, a canal: Panama"
    s = "0P"
    sl = Solution()

    print(sl.isPalindrome(s))