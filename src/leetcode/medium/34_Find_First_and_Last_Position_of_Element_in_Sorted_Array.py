class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def find_bound(is_first: bool) -> int:
            start, end = 0, len(nums) - 1
            ans = -1

            while start <= end:
                mid = (start + end) // 2

                if nums[mid] == target:
                    ans = mid
                    if is_first:
                        end = mid - 1   # Keep looking left
                    else:
                        start = mid + 1  # Keep looking right
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1

            return ans

        return [find_bound(is_first=True), find_bound(is_first=False)]
        # mid = len(nums) // 2
        # count = 0
        # ans = []

        # for idx,i in enumerate(nums[:mid]):
        #     if target == i and count == 1:
        #         ans.append(idx)
        #         return ans
            
        #     if target == i and count == 0:
        #         ans.append(idx)
        #         count += 1



        # for idx,i in enumerate(nums[mid-1:]):
        #     if target == i and count == 1:
        #         ans.append(idx)
        #         return ans 
            
        #     if target == i and count == 0:
        #         ans.append(idx)
        #         count += 1



        # return [-1,-1]

if __name__ == "__main__":
    sl = Solution()
    ans = sl.searchRange(nums = [5,7,7,8,8,10], target = 8)
    #ans = sl.searchRange(nums = [5,7,7,8,8,10], target = 6)
    print(ans)