def solve():
    n = 999
    for i in xrange(2 * n + 1):
        for j in (x for x in xrange(i + 1) if (x + i) % 2 == 0):
            a = int(n - (i - j - 1)/2.0)
            pal = str(a * (a - j))
            if pal == pal[::-1]:
                return pal

if __name__ == '__main__':
    print(solve())