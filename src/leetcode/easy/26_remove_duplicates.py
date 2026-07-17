from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0

        for fast in range(slow,len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]

        return slow + 1
    

if __name__ == "__main__":
    s = [1,1,2]
    #s = [0,0,1,1,1,2,2,3,3,4]

    sl = Solution()
    print(    sl.removeDuplicates(s))