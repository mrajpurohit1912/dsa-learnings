# def bubble_sort(arr:list):
#     n = len(arr)

#     for i in range(n -1):
#         swapped = False

#         for j in range(n - 1 - i):
#             if arr[j] > arr[j+1]:
#                 arr[j] , arr[j+1] =  arr[j+1],arr[j] 
#                 swapped  = True
#         if not swapped:
#             break

#     return arr

from typing import List
def bubble_sort(arr:List)->List:

    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j] , arr[j + 1] = arr[j + 1] , arr[j]
                swapped = True
        
        if not swapped:
            break
    return arr

if __name__ == "__main__":
    #arr = [2,9,11,17,78,90,99,45]
    arr = [99,56,23,68]
    response = bubble_sort(arr)
    print(response)