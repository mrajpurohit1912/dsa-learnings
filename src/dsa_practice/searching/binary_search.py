from typing import List

def binary_search(arr: List[int], target: int) -> int:
    """
    Performs binary search on a sorted list.
    Returns the index of target if found, otherwise -1.
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

if __name__ == "__main__":
    arr = [2, 9, 11, 17, 45, 78, 90, 99]
    targets = [78, 2, 99, 100]

    print("--- Binary Search Demo ---")
    print(f"Array: {arr}")
    for target in targets:
        ans = binary_search(arr, target)
        print(f"Searching for {target} -> Found at index: {ans}")
