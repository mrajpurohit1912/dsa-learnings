from typing import List

def linear_search(arr: List[int], target: int) -> int:
    """
    Performs linear search on a list.
    Returns the index of target if found, otherwise -1.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1

if __name__ == "__main__":
    arr = [45, 9, 17, 11, 2, 78, 90, 99]
    targets = [78, 2, 99, 100]

    print("--- Linear Search Demo ---")
    print(f"Array: {arr}")
    for target in targets:
        ans = linear_search(arr, target)
        print(f"Searching for {target} -> Found at index: {ans}")
