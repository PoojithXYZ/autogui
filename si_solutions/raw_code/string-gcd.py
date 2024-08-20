def common_divisor(P, Q):
    def is_divisible(string, divisor):
        if len(string) % len(divisor) != 0:
            return False
        return string == divisor * (len(string) // len(divisor))

    if len(P) < len(Q):
        P, Q = Q, P

    max_length = len(Q)
    for length in range(max_length, 0, -1):
        divisor = Q[:length]
        if is_divisible(P, divisor) and is_divisible(Q, divisor):
            return divisor
    return -1
P = input().strip()
Q = input().strip()
print(common_divisor(P, Q))