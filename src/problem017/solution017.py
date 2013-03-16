names = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
    8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
    17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty',
    30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy',
    80: 'eighty', 90: 'ninety', 100: 'hundred', 1000: 'thousand'
}


def to_english(num):
    words = []
    if num >= 1000:
        words.append('%s %s' % (to_english(num / 1000), names[1000]))
        num %= 1000
    if num >= 100:
        words.append('%s %s' % (to_english(num / 100), names[100]))
        num %= 100
    if num and words:
        words.append('and')
    if num >= 20:
        words.append('%s-' % names[(num / 10) * 10])
        num %= 10
    if num:
        words.append(names[num])
    return ' '.join(words).replace('- ', '-').strip('-')


def main():
    english_nums = [to_english(n) for n in xrange(1, 1000 + 1)]
    print(sum([len([c for c in eng if c.isalpha()]) for eng in english_nums]))


if __name__ == '__main__':
    main()
