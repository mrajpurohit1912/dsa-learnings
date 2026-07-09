class Solution:
    def lastRemainingSimulated(self, n: int) -> int:
        """
        Simulation approach: Simulates the elimination process.
        Time Complexity: O(n) - Will TLE/MLE for large n.
        Space Complexity: O(n)
        """
        arr = list(range(1, n + 1))
        left_to_right = True
        
        while len(arr) > 1:
            next_arr = []
            if left_to_right:
                # Remove every second element starting from the first
                for i in range(1, len(arr), 2):
                    next_arr.append(arr[i])
            else:
                # Remove every second element starting from the end
                if len(arr) % 2 == 0:
                    for i in range(0, len(arr), 2):
                        next_arr.append(arr[i])
                else:
                    for i in range(1, len(arr), 2):
                        next_arr.append(arr[i])
            
            arr = next_arr
            left_to_right = not left_to_right
            
        return arr[0]

    def lastRemaining(self, n: int) -> int:
        """
        Optimized Approach: Math tracking head and step.
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        left_to_right = True
        remaining = n
        step = 1
        head = 1

        while remaining > 1:
            # We move the head forward if:
            # 1. We are moving left to right
            # 2. We are moving right to left and the number of elements remaining is odd
            if left_to_right or remaining % 2 == 1:
                head += step
            
            remaining //= 2
            step *= 2
            left_to_right = not left_to_right

        return head

if __name__ == "__main__":
    sl = Solution()
    n_small = 9
    n_large = 10000000
    
    print("--- Elimination Game Demo ---")
    print(f"n = {n_small} (Simulated): {sl.lastRemainingSimulated(n_small)}")
    print(f"n = {n_small} (Optimized): {sl.lastRemaining(n_small)}")
    print(f"n = {n_large} (Optimized): {sl.lastRemaining(n_large)}")