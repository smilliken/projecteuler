import random
import itertools
from collections import OrderedDict


def rabin_test(a, n):
    b = [int(char) for char in '{0:b}'.format(n - 1)][::-1]
    d = 1
    for i in xrange(len(b) - 1, -1, -1):
        x = d
        d = (d * d) % n
        if d == 1 and x != 1 and x != n - 1:
            return True
        if b[i] == 1:
            d = (d * a) % n
    return d != 1


def is_prime(n, s=7):
    '''Returns True if n is prime with certainty 1 - 2^-s using Miller-Rabin.'''
    return n > 1 and not any(rabin_test(random.randint(1, n - 1), n) for j in xrange(1, s + 1))


def check(n, m):
    n, m = str(n), str(m)
    return is_prime(int(m + n)) and is_prime(int(n + m))


def search(size=5):
    groups = []
    for p in (n for n in xrange(2 ** 31) if is_prime(n)):
        for group in groups:
            if all(check(p, m) for m in group):
                group.add(p)
            if len(group) >= size:
                print(group)
                return sum(group)
        groups.append(set([p]))


def search(size=2):
    primes = OrderedDict()
    for p in (n for n in xrange(2 ** 31) if is_prime(n)):
        primes[p] = ps = set([q for q in primes if check(p, q)])
        [primes[q].add(p) for q in ps]
        candidates = [
            reduce(lambda a, b: a.intersection(b), groups)
            for groups in itertools.combinations((primes[q].union([q]) for q in ps), size - 1)]
        candidates = [c for c in candidates if len(c) >= size]
        if candidates:
            return min(candidates, key=sum)


def main():
    print(sum(search(5)))


if __name__ == '__main__':
	main()