def is_curious_fraction(num, denom):
    if num % 10 == denom % 10 == 0:
        return False # trivial case
    num_factors, denom_factors = list(str(num)), list(str(denom))
    for f in denom_factors:
        if f in num_factors:
            num_factors.remove(f)
            denom_factors.remove(f)
    return denom_factors and\
        int(''.join(denom_factors)) != 0 and\
        num != int(''.join(num_factors)) and\
        num / float(denom) == int(''.join(num_factors)) / float(''.join(denom_factors))

def simplify(numerator, denominator):
    for f in xrange(2, min(numerator, denominator)/2):
        while numerator % f == 0 and denominator % f == 0:
            numerator /= f
            denominator /= f
    return numerator, denominator

def main():
    curious_fractions = [(num, denom) for denom in xrange(10, 100) for num in xrange(10, denom) if is_curious_fraction(num, denom)]
    numerator, denominator = reduce(lambda x, y: (x[0] * y[0], x[1] * y[1]), curious_fractions)
    print(simplify(numerator, denominator)[1])

if __name__ == '__main__':
    main()