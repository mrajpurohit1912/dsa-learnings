from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # start,end = 0,len(nums) -1

        # while start < end:
        #     current_sum = nums[start] + nums[end]
        #     if current_sum  == target:
        #         return [start,end]
        #     elif current_sum < target:
        #         start += 1
        #     else:
        #         end -= 1

        my_dict = {}

        for index,num in enumerate(nums):
            difference = target - num

            if difference in my_dict:
                return [my_dict[difference] , index]
            
            my_dict[num] = index


if __name__ == "__main__":
    
    # nums = [2,7,11,15]
    # target = 9
    nums = [3,2,4]
    target = 6
    sl = Solution()
    ans = sl.twoSum(nums,target)
    print(ans)