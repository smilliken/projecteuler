import itertools


def check(die1, die2, targets):
    for (digit1, digit2) in targets:
        if (digit1 not in die1 or digit2 not in die2)\
                and (digit2 not in die1 or digit1 not in die2):
            return False
    return True


def gen_dies():
    for die in itertools.combinations(range(10), 6):
        die = list(die)
        if 6 in die:
            die.append(9)
        if 9 in die:
            die.append(6)
        yield die


def main():
    targets = ['%02d' % x ** 2 for x in range(1, 10)]
    targets = [(int(d1), int(d2)) for (d1, d2) in targets]
    dies = list(gen_dies())
    print(len([1 for idx, die1 in enumerate(dies) for die2 in dies[idx:]\
        if check(die1, die2, targets)]))


if __name__ == '__main__':
    main()
