from typing import List

def insertion_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list of integers in ascending order using Insertion Sort.
    Time Complexity: O(n^2) worst/average, O(n) best
    Space Complexity: O(1)
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == "__main__":
    arr = [87, 45, 90, 11, 2, 78]
    print("--- Insertion Sort Demo ---")
    print(f"Original Array: {arr}")
    response = insertion_sort(arr)
    print(f"Sorted Array:   {response}")