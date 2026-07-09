from typing import List

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         slow = 0

#         for fast in range(1,len(nums)):
#             if nums[fast] != nums[slow]:
#                 slow += 1
#                 nums[slow] = nums[fast]

#         return slow + 1

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         profit = 0

#         for i in range(1,len(prices)):
#             if prices[i] > prices[i - 1]:
#                 profit += prices[i] - prices[i -1]
        
#         return profit

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         my_list = []

#         for i in nums:
#             if i in my_list:
#                 return True
#             my_list.append(i)

        
#         return False
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
        
#         my_dic = {}

#         for i in nums:
#             if i not in my_dic:
#                 my_dic[i] = 1
#             else:
#                 return True
            
#         return False

# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         while k > 0:
#             last_number = nums[-1]
        
#         k -= 1

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for i in nums:
            result ^= i
        return result





if __name__ == "__main__":
    #nums = [1,1,2]
    #nums = [0,0,1,1,1,2,2,3,3,4]
    #prices =  [1,2,3,4,5]
    nums = [2,2,1]
    sl = Solution()
    ans  = sl.singleNumber(nums)
    print(ans)