# if we sort it we in that sorted list we have to find the kth largest element

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        my_dict = {}

        for i,j in enumerate(nums):
            my_dict[i] = j

        my_dict = sorted(my_dict)
        print(my_dict)
        #return my_dict[len(my_dict) - k] 
        print(f"Debug: {len(my_dict)  } {k} { len(my_dict) - k}")
        return my_dict[len(my_dict) - (k )] 


if __name__ == "__main__":
    nums = [3,2,1,5,6,4]
    k = 2

    sl = Solution()
    ans = sl.findKthLargest(nums,k)
    print(ans)