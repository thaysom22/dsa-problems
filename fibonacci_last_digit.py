# Uses python3
import sys, random


def get_fibonacci_last_digit(n):
    if n < 2:
        return n
    
    last_digits = [0]*(n+1)
    last_digits[1] = 1
    for i in range(2, n+1):
        last_digits[i] = (last_digits[i-1] + last_digits[i-2]) % 10
    
    return last_digits[n]


# def get_fibonacci_last_digit_naive(n):
#     if n <= 1:
#         return n

#     previous = 0
#     current  = 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current

#     return current % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print("\n")
    print(get_fibonacci_last_digit(n))


# def generate_input():
#     return random.randint(0, 50)
    
# if __name__ == '__main__':
#     # stress test
#     while True:
#         n = generate_input()
#         print(n)
#         result1 = get_fibonacci_last_digit(n)
#         result2 = get_fibonacci_last_digit_naive(n)
#         if result1 == result2:
#             print("OK")
#         else:
#             print(result1, result2) 
#             break
