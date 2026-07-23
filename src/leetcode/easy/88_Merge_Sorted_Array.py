# if take greter one from m and n then will get index error, so take smaller one and iterate through

from typing import List
from itertools import chain

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1 = nums1[:m]
        nums2 = nums2[:n]

        nums1.extend(nums2)
        nums1 = sorted(nums1)

        print(nums1)


if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    m= 3
    nums2 =[2,5,6]
    n= 3

    sl = Solution()

    print(sl.merge(nums1,m,nums2,n))

