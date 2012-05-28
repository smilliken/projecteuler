import itertools

def proper_divisors(n):
    for i in xrange(1, n/2 + 1):
        if n % i == 0:
            yield i

def main():
    ceiling = 28123
    proper_divisor_sums = [sum(proper_divisors(i)) for i in xrange(ceiling)]
    abundant_nums = [i for i, x in enumerate(proper_divisor_sums) if x > i]
    abundant_sums = set((a + b for a, b in itertools.product(abundant_nums, abundant_nums) if a + b <= ceiling))
    holes = set(range(1, ceiling)).difference(abundant_sums)
    print(sum(holes))

if __name__ == '__main__':
    main()