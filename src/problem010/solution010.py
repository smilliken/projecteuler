import math


def is_prime(n):
    return not any(a for a in xrange(2, int(math.sqrt(n)) + 1) if n % a == 0)


def solve():
    return sum((x for x in xrange(2, 2000000) if is_prime(x)))

if __name__ == '__main__':
    print(solve())
