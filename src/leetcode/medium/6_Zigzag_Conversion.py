
class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if len(s) <= 1: 
            return s

        rows = [""] * numRows
        current_row = 0
        going_down = False

        for char in s:
            rows[current_row] = char

            if current_row == 0 or current_row == numRows -1:
                going_down = not going_down

            current_row += 1 if going_down else -1

        return "".join(rows)



if __name__ == "__main__":
    solution = Solution()

    s = "PAYPALISHIRING" 
    numRows = 3
    response = solution.convert(s,numRows)
    print(response)