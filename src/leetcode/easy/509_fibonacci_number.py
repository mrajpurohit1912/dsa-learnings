class Solution:
    def fib(self, n: int) -> int:
        """
        Calculates the n-th Fibonacci number.
        Time Complexity: O(2^n) recursion, optimized can be O(n)
        Space Complexity: O(n) recursion stack
        """
        if n <= 1:
            return n
        
        return self.fib(n - 1) + self.fib(n - 2)

if __name__ == "__main__":
    sl = Solution()
    n = 4
    print(f"Fibonacci({n}) = {sl.fib(n)}")