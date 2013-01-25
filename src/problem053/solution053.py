import math

def choose(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

def main():
    print(len([1 for n in xrange(1, 101) for k in xrange(0, n + 1) if choose(n, k) >= 1000000]))

if __name__ == '__main__':
    main()
