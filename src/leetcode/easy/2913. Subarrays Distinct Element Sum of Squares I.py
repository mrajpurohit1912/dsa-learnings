
from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        distinct_subarrays = []

        for i in range(len(nums)):
            for j in range(i+1,len(nums) + 1):
                if (i >= 0) and (j>=i) and (len(nums) >= j):
                    distinct_subarrays.append(nums[i:j])

        return sum(len(set(each_subarray))**2 for each_subarray in distinct_subarrays) 

if __name__ == "__main__":
    nums = [1,2,1]
    #nums  =  [1,1]
    sl = Solution()
    ans= sl.sumCounts(nums)
    print(ans)