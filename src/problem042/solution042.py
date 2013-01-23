import math


def digitsum(str_):
    return sum([ord(chr_) - 64 for chr_ in str_])


def is_triangle_num(num):
    idx = (-1 + math.sqrt(1 + 8 * num)) / 2
    return idx >= 0 and int(idx) == idx


def main():
    words = open('words.txt').read().split(',')
    wordvals = [digitsum(word.strip('"')) for word in words]
    print(len([val for val in wordvals if is_triangle_num(val)]))

if __name__ == '__main__':
    main()
