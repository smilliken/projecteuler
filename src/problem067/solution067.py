def main():
    rows = [map(int, line.split())for line in open('triangle.txt')]
    row_sum = lambda r0, r1: [a + max(b, c) for (a, b, c) in zip(r1, r0 + [0], [0] + r0)]
    print(max(reduce(row_sum, rows)))

if __name__ == '__main__':
    main()
