# def print_number(n):

#     if n <= 0:
#         return


#     print(n)

#     print_number(n-1)


# def find_factorial(n):

#     if n == 1:
#         return 1

#     return n * find_factorial(n-1)

    
def find_sum(n):
    if n == 1:
        return 1

    return n + find_sum(n-1)     



if __name__ == "__main__":
    print(find_sum(5))
