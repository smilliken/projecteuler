def main():
    codes = [code.strip() for code in open('keylog.txt').read().split('\n') if code]
    tails = {}
    for code in codes:
        for idx, char in enumerate(code):
            tails[char] = tails.get(char, []) + list(code[:idx])
    answ = sorted(tails.keys(), key=lambda x: len(set(tails[x])))
    print(''.join(answ))

if __name__ == '__main__':
    main()