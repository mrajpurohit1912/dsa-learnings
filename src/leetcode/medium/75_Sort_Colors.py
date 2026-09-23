#start = nums[0]
#end = nums[1]
# while fast < len(nums)
# if fast < slow
#   slow += fast
#   slow += 1
# fast += 1

#75. Sort Colors
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        fast = 1

        while fast < len(nums):
            if nums[fast] < nums[slow]:
                current_slow = nums[slow]
                nums[slow] = nums[fast]
                nums[fast] = current_slow
                slow += 1
            fast += 1

        print(nums)


if __name__ == "__main__":
    nums = [2,0,2,1,1,0]
    sl = Solution()

    print(sl.sortColors(nums))
