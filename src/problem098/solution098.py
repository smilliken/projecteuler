import math

def find_anagrams():
    words = [word.strip('"') for word in open('words.txt').read().split(',')]
    words.sort(key=len)
    words = [(sorted(word), word) for word in words]
    return [(word1, word2) for idx, (key1, word1) in enumerate(words) for (key2, word2) in words[idx + 1:] if key1 == key2]

def get_charmap(word, num):
    charmap, intmap = {}, {}
    for charidx, char in enumerate(word):
        if char not in charmap:
            charmap[char] = num[charidx]
        if num[charidx] not in intmap:
            intmap[num[charidx]] = char
        if charmap[char] != num[charidx] or intmap[num[charidx]] != char:
            return
    return charmap

def main():
    maxsquare = 0
    anagrams = find_anagrams()
    maxlen = max([len(anagram[0]) for anagram in anagrams])
    for word1num in xrange(10 ** (maxlen / 2)):
        word1sq = str(word1num ** 2)
        for word1, word2 in [anagram for anagram in anagrams if len(anagram[0]) == len(word1sq)]:
            charmap = get_charmap(word1, word1sq)
            if not charmap or charmap.get(word2[0]) == '0':
                continue
            word2sq = int(''.join([charmap[char] for char in word2]))
            word2num = math.sqrt(word2sq)
            if word2num == math.floor(word2num):
                maxsquare = max(int(word1sq), word2sq, maxsquare)        
    print(maxsquare)

if __name__ == '__main__':
    main()