# check if current string present in all of the string

# start iterating from 1st element as 0th element will be used to compare:


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
 

        start = 0
        end  = len(strs)

        while start < end:
            if start