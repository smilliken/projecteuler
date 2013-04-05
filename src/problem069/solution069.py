"""
The ratio n / phi(n) is maximized when n is a product of the smallest primes
since a smaller prime will disqualify more numbers from being relatively prime
to n than a larger prime.
"""
import math


def is_prime(n):
    return not any(a for a in xrange(2, int(math.sqrt(n)) + 1) if n % a == 0)


def main():
    ans = 1
    for n in xrange(2, 2 ** 32):
        if is_prime(n):
            if ans * n > 1000000:
                break
            ans *= n
    print(ans)

if __name__ == '__main__':
    main()
