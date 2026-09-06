
# iterate through the array from k to end_of_the array:
# 0 to k will be the conntigues array(window)
# after each iteration will increa

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k,len(nums)):
            window_sum += nums[i]
            window_sum -= nums[i-k]

            if window_sum > max_sum:
                max_sum = window_sum

        return max_sum/k


if __name__ == "__main__":
    solution = Solution()
    #response = solution.findMaxAverage([1,12,-5,-6,50,3], 4)
    response = solution.findMaxAverage([5], 1)
    print(response)