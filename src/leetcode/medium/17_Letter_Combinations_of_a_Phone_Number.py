
# class Solution:
#     def letterCombinations(self, digits: str) :#-> list[str]
#         phone = { "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz", }

#         digits = list(digits)

#         for i 


# if __name__ == "__main__":
#     solution = Solution()
#     sl = solution.letterCombinations("23")


def generate_subsets(nums:list[str]):
    result = []
    current = []

    def backtrack(index:int):
        if index == len(nums):
            result.append(current.copy())
            return


        current.append(nums[index])
        backtrack(index+1)

        current.pop()

        backtrack(index + 1)

    backtrack(0)

    return result

if __name__ == "__main__":
    print(generate_subsets([1,2,3]))