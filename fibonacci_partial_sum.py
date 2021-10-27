# Uses python3
import sys, random

# def fibonacci_partial_sum_naive(from_, to):
#     _sum = 0

#     current = 0
#     _next  = 1

#     for i in range(to + 1):
#         if i >= from_:
#             _sum += current

#         current, _next = _next, current + _next

#     return _sum % 10

def fibonacci_partial_sum(from_, to):
    def fibonacci_sum(n):
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

        # last digit of S(i) is equal to last digit of F(i+2) - 1
        temp = get_fibonacci_huge(n+2, 10)  # constant O(100) complexity
        if temp != 0:
            return temp - 1
        else:
            return 9

    # PS(from, to) = S(to) - S(from-1)
    last_digit_lower_sum = fibonacci_sum(from_-1)
    last_digit_upper_sum = fibonacci_sum(to)
    # correct for possibility difference is negative 
    return ((10 + last_digit_upper_sum) - last_digit_lower_sum) % 10

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))


# def generate_input(a, b):
#     return random.randint(a, b)
    

# if __name__ == '__main__':
#     # stress test
#     while True:
#         a = generate_input(1, 10000)
#         b = generate_input(a, 20000)
#         print(a, b)
#         result1 = fibonacci_partial_sum(a, b)
#         result2 = fibonacci_partial_sum_naive(a, b)
#         if result1 == result2:
#             print("OK")
#         else:
#             print("ERROR")
#             print(result1, result2) 
#             break
