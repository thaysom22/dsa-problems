# Uses python3
from sys import stdin
import random

# def fibonacci_sum_squares_naive(n):
#     if n <= 1:
#         return n

#     previous = 0
#     current  = 1
#     sum      = 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current
#         sum += current * current

#     return sum % 10

def fibonacci_sum_squares(n):
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

    fib_last_digit = get_fibonacci_huge(n, 10)
    prev_fib_last_digit = get_fibonacci_huge(n-1, 10)
    # by area of diagram: sum of squares = F(i)*(F(i)+F(i-1))
    return (fib_last_digit*(fib_last_digit+prev_fib_last_digit)) % 10


if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares(n))


# def generate_input(a, b):
#     return random.randint(a, b)
    

# if __name__ == '__main__':
#     # stress test
#     while True:
#         a = generate_input(0, 10000)
#         print(a)
#         result1 = fibonacci_sum_squares(a)
#         result2 = fibonacci_sum_squares_naive(a)
#         if result1 == result2:
#             print("OK")
#         else:
#             print("ERROR")
#             print(result1, result2) 
#             break
