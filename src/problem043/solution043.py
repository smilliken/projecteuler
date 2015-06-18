def recur(digits, divisors, seed=''):
    for d in digits:
        sub_digits = [sub_d for sub_d in digits if sub_d != d]
        if len(seed) < 2:
            for x in recur(sub_digits, divisors, d + seed):
                yield x
        elif int(d + seed[0:2]) % divisors[0] == 0:
            if len(divisors) > 1:
                for x in recur(sub_digits, divisors[1:], d + seed):
                    yield x
            else:
                yield int(sub_digits[0] + d + seed)

def main():
    print(sum(recur(list('0123456789'), [17, 13, 11, 7, 5, 3, 2])))

if __name__ == '__main__':
    main()
