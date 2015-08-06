import itertools
import operator
import random


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


def diags():
    yield 1
    for r in xrange(2, 2 ** 31):
        for d in xrange(4):
            yield 4 * r ** 2 - 10 * r + 7 + 2 * r * d - 2 * d


def scan(func, seq, acc=None):
    for item in seq:
        acc = func(acc, item)
        yield acc


def main():
    i, _ = itertools.dropwhile(
        lambda (i, primes): i < 2 or 10 * primes > i,
        enumerate(scan(operator.add, itertools.imap(
            lambda n: 1 if is_prime(n) else 0, diags()), 0), start=1)).next()
    print(i / 2 + 1)


if __name__ == '__main__':
    main()
