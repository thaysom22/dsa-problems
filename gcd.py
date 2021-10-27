# Uses python3
import sys, random

# def gcd_naive(a, b):
#     current_gcd = 1
#     for d in range(2, min(a, b) + 1):
#         if a % d == 0 and b % d == 0:
#             if d > current_gcd:
#                 current_gcd = d

#     return current_gcd


def gcd_euclidian(a, b):
    # base case
    if b == 0:
        return a
        
    remainder = a % b
    return gcd_euclidian(b, remainder)


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_euclidian(a, b))


# def generate_input():
#     return random.randint(1, 2*10**5)
    

# if __name__ == '__main__':
#     # stress test
#     while True:
#         a = generate_input()
#         b = generate_input()
#         print(a, b)
#         result1 = gcd_euclidian(a, b)
#         result2 = gcd_naive(a, b)
#         if result1 == result2:
#             print("OK")
#         else:
#             print("ERROR")
#             print(result1, result2) 
#             break