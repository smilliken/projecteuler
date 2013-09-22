import functools

def row_reduce(row):
    return [max(x1, x2) for (x1, x2) in zip(row, row[1:])]

def foldl_rows(row1, row2):
    return [x1 + x2 for (x1, x2) in zip(row2, row_reduce(row1))]

def main():
    rows = [map(int, line.split()) for line in open('triangle.txt').readlines()]
    return max(functools.reduce(foldl_rows, rows[::-1]))

if __name__ == '__main__':
    print(main())
