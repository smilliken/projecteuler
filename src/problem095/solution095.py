import math

MAX_VALUE = 1000000

def proper_divisors(num):
    for div in xrange(1, int(math.sqrt(num)) + 1):
        if num % div == 0:
            yield div
            if div > 1:
                yield num / div


def proper_divisor_sum(num):
    return sum(proper_divisors(num))


def get_amicable_chain(seed):
    chain = (seed,)
    next_ = proper_divisor_sum(seed)
    while next_ > seed and next_ <= MAX_VALUE and next_ not in chain:
        chain += (next_,)
        next_ = proper_divisor_sum(next_)
    return chain if next_ == seed else ()


def main():
    longest_chain = (1,)
    seen_nums = set(longest_chain)
    for num in xrange(2, MAX_VALUE):
        if num in seen_nums:
            continue
        chain = get_amicable_chain(num)
        seen_nums = set(chain + tuple(seen_nums))
        longest_chain = chain if len(chain) > len(longest_chain) else longest_chain
    print(min(longest_chain))

if __name__ == '__main__':
    exit(main())