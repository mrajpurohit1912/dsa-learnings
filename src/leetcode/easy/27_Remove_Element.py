

# check if the element is equal to val then replace in place
# how to replace in-place 


from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow  = 0

        for fast in range(len(nums)):
            if nums[fast] != val:

                
                nums[slow] = nums[fast]
                slow += 1

        return slow


if __name__ == "__main__":
    nums = [3,2,2,3]
    val = 3
    # nums = [0,1,2,2,3,0,4,2]
    # val = 2

    sl = Solution()
    print(sl.removeElement(nums,val))
    