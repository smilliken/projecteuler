import itertools
import math
import operator


def is_prime(n):
    return n > 1 and not any(a for a in xrange(2, int(math.sqrt(n)) + 1) if n % a == 0)


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
