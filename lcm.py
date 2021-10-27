# Uses python3
import sys, random

# def lcm_naive(a, b):
#     for l in range(1, a*b + 1):
#         if l % a == 0 and l % b == 0:
#             return l

#     return a*b


def lcm_efficient(a, b):
    def gcd_euclidian(a, b):
        if b == 0:
            return a
            
        remainder = a % b
        return gcd_euclidian(b, remainder)
    
    # a*b = gcd(a,b) * lcm(a,b)
    return int((a*b) / gcd_euclidian(a, b))


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_efficient(a, b))


# def generate_input():
#     return random.randint(1, 2*10**3)
    

# if __name__ == '__main__':
#     # stress test
#     while True:
#         a = generate_input()
#         b = generate_input()
#         print(a, b)
#         result1 = lcm_efficient(a, b)
#         result2 = lcm_naive(a, b)
#         if result1 == result2:
#             print("OK")
#         else:
#             print("ERROR")
#             print(result1, result2) 
#             break

