# maintain a empty string - max_array

#maintain 2 nested loops 
# inside the 2nd loop create add the element to the string by checking that element is present of or if not then add it 
# else compare the size of current_array with the max_array 


#Brute Force approch
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0

        for i in range(len(s)):
            current_array = ""
            current_array += s[i]
            max_len =  max(max_len,len(current_array))

            for j in range(i+1,len(s)):
                if s[j] in current_array:
                    break

                current_array += s[j]
                max_len =  max(max_len,len(current_array))

                

        return max_len

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         max_len = 0

#         for i in range(len(s)):
#             current_array = set()

#             for j in range(i+1,len(s)):
#                 if s[j] in current_array:
#                     break

#                 current_array += s[j]
#                 max_len =  max(max_len,len(current_array))

                

#         return max_len


                


if __name__ == "__main__":
    solution = Solution()

    s = "bbbbb"
    response = solution.lengthOfLongestSubstring(s)
    print(response)