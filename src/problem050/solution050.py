import math


def is_prime(n):
    return not any(a for a in xrange(2, int(math.sqrt(n)) + 1) if n % a == 0)


def main():
    limit = int(1e6)
    primes = [x for x in xrange(2, limit) if is_prime(x)]
    candidates = []
    max_len = 0
    for b in xrange(len(primes)):
        for a in range(b - max_len - 1)[::-1]:
            candidate = sum(primes[a:b])
            if candidate > limit or candidate in primes:
                max_len = max((b - a), max_len)
            if candidate > limit:
                break
            if candidate in primes:
                candidates.append((b - a, candidate))
    print(max(candidates)[1])

if __name__ == '__main__':
    exit(main())
