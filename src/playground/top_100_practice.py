

# def two_sum(arr,target):
    # brut force approach
    # n = len(arr)
    # for i in range(n):
    #     for j in range(i+1,n):
    #         if arr[i] + arr[j] == target:
    #             return i,j
            
    # return False


    # optimized approch
    # my_dict = {}

    # for i,num in enumerate(arr):

    #     complement = target - num

    #     if complement in my_dict:
    #         return my_dict[complement] , i
        
    #     my_dict[num] = i

    # return False

def buy_and_sell_stock(arr):
    max_profit = 0
    n = len(arr)

    for i in range(n):
        for j in range(i + 1,n):
            if arr[j] - arr[i] > max_profit:
                max_profit = arr[j] - arr[i] 
    return max_profit

if __name__ == "__main__":
    #arr = [7, 10, 1, 3, 6, 9, 2]
    #target = -2

    # arr = [1, -2, 1, 0, 5]
    # target = 0
    arr =  [1, 3, 6, 9, 11]
    print(buy_and_sell_stock(arr))