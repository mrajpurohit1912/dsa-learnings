# def selection_sort(arr:list):
#     if arr is None:
#         return

#     n = len(arr) 

#     for i in range(n - 1):
#         min_idx = i
#         for j in range(i+1 ,n):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         arr[i] ,arr[min_idx] = arr[min_idx] ,arr[i] 

#     return arr
from typing import List

def selection_sort(arr:List)->List:
    n = len(arr)

    for i in range(n - 1):
        min_element = i
        for j in range(i+1,n):
            if arr[j] < arr[min_element]:
                min_element = j
        arr[i],arr[min_element]  = arr[min_element] , arr[i] 
    return arr

if __name__ == "__main__":
    #arr = [2,11,9,78,90,99,45,17]
    #arr = [99,56,23,68]
    arr = [87,45,90,11]
    response = selection_sort(arr)
    print(response)