import math

def main():
    max_circum = 1500000
    solns = {}
    for m in xrange(1, int(math.sqrt(max_circum / 2)) + 1):
        for n in xrange(1, m):
            a = m ** 2 - n ** 2
            b = 2 * m * n
            c = m ** 2 + n ** 2
            p = a + b + c
            for k in xrange(1, 1 + max_circum / p):
                solns[p * k] = set(list(solns.get(p * k, set())) + [tuple(sorted((a * k, b * k, c * k)))])
    print(len([1 for circum, triples in solns.items()if len(triples) == 1 and circum <= max_circum]))

if __name__ == '__main__':
    main()