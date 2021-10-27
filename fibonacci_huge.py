# Uses python3
import sys, random

# # return nth fibonacci number modulo m
# def get_fibonacci_huge_naive(n, m):
#     if n <= 1:
#         return n

#     previous = 0
#     current  = 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current

#     return current % m


# complexity O(m^2)
def get_fibonacci_huge(n, m):
    if n <= 1:
        return n

    # complexity O(m^2)
    def generate_pisano_seq(m):
        pisano_seq = [0, 1, 1]
        current_fib, prev_fib = 2, 1
        # smallest possible pisano period is 3, largest is m**2
        for _ in range(3, m**2 + 1):
            current_pisano = current_fib % m
            if current_pisano == 1 and pisano_seq[-1] == 0:
                return pisano_seq[:-1]
            # calculate next pair in fibonacci sequence
            current_fib, prev_fib = current_fib + prev_fib, current_fib
            pisano_seq.append(current_pisano)

    pisano_seq = generate_pisano_seq(m)
    # length of pisano sequence is pisano period
    remainder = n % len(pisano_seq)
    return pisano_seq[remainder]


if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))

# def generate_input(a, b):
#     return random.randint(a, b)
    

# if __name__ == '__main__':
#     # stress test
#     while True:
#         a = generate_input(1, 1000)
#         b = generate_input(2, 100)
#         print(a, b)
#         result1 = get_fibonacci_huge(a, b)
#         result2 = get_fibonacci_huge_naive(a, b)
#         if result1 == result2:
#             print("OK")
#         else:
#             print("ERROR")
#             print(result1, result2) 
#             break

