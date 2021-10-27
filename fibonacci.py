# import random

def calc_fib(n):
    if n < 2:
        return n
    fib_vals = [0]*(n+1)
    fib_vals[1] = 1
    for i in range(2, n+1):
        fib_vals[i] = fib_vals[i-1] + fib_vals[i-2]

    return fib_vals[n]


# def calc_fib_naive(n):
#     if n < 2:
#         return n
#     return calc_fib_naive(n-1) + calc_fib_naive(n-2)


# def generate_input():
#     return random.randint(0, 30)
    

# if __name__ == '__main__':
#     # stress test
#     while True:
#         n = generate_input()
#         print(n)
#         result1 = calc_fib_efficient(n)
#         result2 = calc_fib_naive(n)
#         if result1 == result2:
#             print("OK")
#         else:
#             print(result1, result2) 
#             break
        
# manual input
n = int(input())
print(calc_fib(n))
