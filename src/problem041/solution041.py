import itertools
import math


def is_prime(n):
    return not any(a for a in xrange(2, int(math.sqrt(n)) + 1) if n % a == 0)


def main():
    ans = 0
    for n in xrange(1, 10):
        for digits in itertools.permutations(range(1, n + 1), n):
            num = int(''.join([str(digit) for digit in digits]))
            ans = max(ans, num) if is_prime(num) else ans
    print(ans)

if __name__ == '__main__':
    main()