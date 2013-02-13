import itertools
import math


def prime_sieve(limit):
    nums = range(2, limit + 1)
    for div in nums[:int(math.sqrt(limit))]:
        for idx, num in enumerate(nums):
            if num > div and num % div == 0:
                nums[idx] = 0
    return [n for n in nums if n > 0]


def main():
    limit = 5e7
    primes = prime_sieve(int(math.sqrt(limit)))

    def gen_seq(power, running):
        return itertools.takewhile(lambda val: val < limit,
            (running + p ** power for p in primes))

    print(len(list(set(
        (c for a in gen_seq(4, 0)
                for b in gen_seq(3, a)
                    for c in gen_seq(2, b))))))
    return 0

if __name__ == '__main__':
    exit(main())
