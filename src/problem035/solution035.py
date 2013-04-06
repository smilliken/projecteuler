import math


def is_prime(n):
    return not any(a for a in xrange(2, int(math.sqrt(n)) + 1) if n % a == 0)


def main():
    primes = set([str(x) for x in xrange(2, int(1e6) + 1) if is_prime(x)])
    print(len([p for p in primes if
        all([(p[i:] + p[:i]) in primes for i in xrange(1, len(p))])]))

if __name__ == '__main__':
    exit(main())
