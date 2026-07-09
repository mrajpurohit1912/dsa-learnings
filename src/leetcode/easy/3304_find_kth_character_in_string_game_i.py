
class Solution:
    def kthCharacter(self, k: int) -> str :#
        word = "a"

        while len(word) < k :

            word += "".join(
                chr(ord(c) + 1)
                for c in word
            )

        return word[k-1]


if __name__ == "__main__":
    #arr = [7, 10, 1, 3, 6, 9, 2]
    #target = -2

    # arr = [1, -2, 1, 0, 5]
    # target = 0
    # arr =  [1, 3, 6, 9, 11]
    sl = Solution()
    print(sl.kthCharacter(3))