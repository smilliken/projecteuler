import math

def main():
    perimeter_limit = 1000
    perimeter_solns = {}
    for a in xrange(1, perimeter_limit):
        for b in xrange(1, perimeter_limit - a):
            c = math.sqrt(a ** 2 + b ** 2)
            perimeter = int(a + b + c)
            if c == int(c) and a + b + c <= perimeter_limit:
                perimeter_solns[perimeter] = perimeter_solns.get(perimeter, 0) + 1
    perimeter, count = max(perimeter_solns.items(), key=lambda (k, v): v)
    print(perimeter)

if __name__ == '__main__':
    main()
