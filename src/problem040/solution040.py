"""
Take advantage of the fact that there are 9 1-digit ints, 90 2-digit ints,
900 3-digit ints (etc) to seek directly to the number without calculating
the entire string.
"""
import operator


def get_digit(target):
    cursor = 1
    num_digits = 1
    while cursor < target:
        cursor += 9 * 10 ** (num_digits - 1) * num_digits
        num_digits += 1
    num_digits = (num_digits - 1) or 1
    num = target - (cursor - target) / num_digits
    return int(str(num)[(cursor - target) % num_digits])


def main():
    print(reduce(operator.mul, [get_digit(10 ** i) for i in xrange(7)]))

if __name__ == '__main__':
    main()
