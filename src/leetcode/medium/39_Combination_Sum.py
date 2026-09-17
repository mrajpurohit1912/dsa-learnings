
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        combinations = []

        def backtracking(index):
            if sum(combinations) == Tar


# if __name__ == "__main__":
#     solution = Solution()
#     sl = solution.letterCombinations("23")