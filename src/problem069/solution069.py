"""
The ratio n / phi(n) is maximized when n is a product of the smallest primes
since a smaller prime will disqualify more numbers from being relatively prime
to n than a larger prime.
"""
import math


def primes():
    for n in xrange(2, 2 ** 32):
        if not any(p for p in xrange(2, int(math.sqrt(n) + 1)) if n % p == 0):
            yield n


def main():
    ans = 1
    for p in primes():
        if ans * p > 1000000:
            break
        ans *= p
    print(ans)


if __name__ == '__main__':
    main()
