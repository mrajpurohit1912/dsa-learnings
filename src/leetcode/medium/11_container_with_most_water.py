from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # max_value = 0
        # slow = 0

        # for fast in range(len(height)):
        #     if height[fast] > height[slow]:
        #         max_value = max(height[fast] - height[slow],max_value)
        #         max_value = 0
        #     else:
        #         max_value =+ height[fast]

        # return max_value
        
        left = 0
        right = len(height) - 1

        max_value = 0

        while left < right:
            h = min(height[left],height[right]) 
            w = right - left
            area = h * w

            max_value = max(max_value,area)

            if height[left] < height[right]:
                left +=1
            else:
                right -=1
        
        return max_value


if __name__ == "__main__":
    #arr = [7, 10, 1, 3, 6, 9, 2]
    #target = -2

    # arr = [1, -2, 1, 0, 5]
    # target = 0
    arr =  [1, 3, 6, 9, 11]
    sl = Solution()

    print(sl.maxArea(arr))