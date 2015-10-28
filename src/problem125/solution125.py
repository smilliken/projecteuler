from itertools import takewhile


def main():
    ceil = 10 ** 8
    sums = [n * (n + 1) * (2 * n + 1) / 6 for n in xrange(int(ceil ** .5))]
    print(sum(set([n - m
        for (i, n) in enumerate(sums)
        for m in takewhile(lambda m: n - m < ceil, sums[:i - 1][::-1])
        if str(n - m) == str(n - m)[::-1]])))

if __name__ == '__main__':
    main()
