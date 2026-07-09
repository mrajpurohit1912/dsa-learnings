from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int)-> List[int]:
        # if len(nums) <= 1:
        #     return nums

        # slow = 0

        # for fast in nums:
        #     if nums[fast] != nums[slow]:
        #         slow += 1
        #         nums[slow] = nums[fast]

        # return nums[:k]
       
        my_dict = {}

        for element in nums:
            if element in my_dict:
                my_dict[element] += 1
            else:
                my_dict[element] = 1

        my_dict = dict(sorted(my_dict.items(),key=lambda x : x[1],reverse=True))

        output_list = list(my_dict.keys())[:k]
        return output_list




if __name__ == "__main__":
    
    # nums = [1,1,1,2,2,3]
    # k = 2

    # nums = [1]
    # k = 1

    nums   =[1,2,1,2,1,2,3,1,3,2]
    k = 2

    sl = Solution()
    respons = sl.topKFrequent(nums=nums,k=k)
    print(respons)