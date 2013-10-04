import math

def is_prime(n):
    return n > 3 and not \
        any(a for a in xrange(2, int(math.sqrt(n)) + 1) if n % a == 0)

def main():
    streak = (0, 0)
    for a in xrange(-999, 1000):
        for b in xrange(-999, 1000):
            for n in xrange(0, 2**32):
                if not is_prime(n ** 2 + a * n + b):
                    break
            streak = max((n, a * b), streak)
    print(streak[1])

if __name__ == '__main__':
    main()
