from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Calculates the maximum profit from buying and selling a stock.
        Approach: Single Pass (Tracking Min Price)
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not prices:
            return 0

        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit

if __name__ == "__main__":
    sl = Solution()
    test_cases = [
        [7, 1, 5, 3, 6, 4],
        [7, 6, 4, 3, 1],
        [2, 4, 1]
    ]
    print("--- Best Time to Buy and Sell Stock Demo ---")
    for prices in test_cases:
        print(f"Prices: {prices} -> Max Profit: {sl.maxProfit(prices)}")
