def proper_divisors(n):
    for i in xrange(1, n / 2 + 1):
        if n % i == 0:
            yield i


def main():
    ceiling = 28123
    abundant_nums = [i for i in xrange(2, ceiling) if i < sum(proper_divisors(i))]
    abundant_sums = set((a + b for a in abundant_nums for b in abundant_nums if a + b < ceiling))
    print(sum(set(range(1, ceiling)).difference(abundant_sums)))

if __name__ == '__main__':
    main()
