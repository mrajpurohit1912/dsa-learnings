class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:

        if len(nums) <2:
            return nums

        start = 0
        end = len(nums)
        max_value_list = []


        while start <= end-k:
            current_sliding_window = nums[start:start+k]
            max_value_list.append(max(current_sliding_window))
            start +=1

        return max_value_list


if __name__ == "__main__":
    sl = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    result = sl.maxSlidingWindow(nums,k)   
    print(result)