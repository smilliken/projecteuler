import itertools
from collections import defaultdict

RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']


def rank_cmp(x, y):
    def _internal_cmp(x_, y_):
        return cmp(RANKS.index(x_), RANKS.index(y_))
    if hasattr(x, '__iter__'):
        for x_, y_ in itertools.izip(x, y):
            cmp_ = _internal_cmp(x_, y_)
            if cmp_ != 0:
                return cmp_
        return 0
    return _internal_cmp(x, y)


def rank_sort(ranks):
    return sorted(ranks, cmp=rank_cmp)


def high_card(hand):
    return rank_sort(get_ranks(hand))[-1]


def get_ranks(hand):
    return rank_sort([card[:-1] for card in hand])


def pred_cmp(pred, hand1, hand2, tiebreaker=None):
    val1, val2 = pred(hand1), pred(hand2)
    if val1 and val2:
        return tiebreaker(hand1, hand2) if tiebreaker else 0
    if val1 and not val2:
        return 1
    if not val1 and val2:
        return -1


def matching_kind(hand, multiplicity):
    rank_groups = itertools.groupby(rank_sort(get_ranks(hand)))
    return rank_sort([rank for rank, group in rank_groups if len(list(group)) == multiplicity])


def is_one_pair(hand):
    return len(matching_kind(hand, 2)) == 1


def is_two_pair(hand):
    return len(matching_kind(hand, 2)) == 2


def is_straight(hand):
    lowest_rank = rank_sort(get_ranks(hand))[0]
    lowest_rank_idx = RANKS.index(lowest_rank)
    return rank_sort(RANKS[lowest_rank_idx:lowest_rank_idx + 5]) == rank_sort(get_ranks(hand))


def is_flush(hand):
    suites = [card[-1:] for card in hand]
    return all([suit == suites[0] for suit in suites])


def is_full_house(hand):
    return is_one_pair(hand) and any(matching_kind(hand, 3))


def is_straight_flush(hand):
    return is_straight(hand) and is_flush(hand)


def is_royal_flush(hand):
    return get_ranks(hand) == rank_sort(RANKS[-5:]) and is_flush(hand)


def cmp_n_of_kind(hand1, hand2, n):
    return pred_cmp(lambda hand: matching_kind(hand, n), hand1, hand2, tiebreaker=lambda h1, h2: rank_cmp(matching_kind(h1, n)[0], matching_kind(h2, n)[0]))


def cmp_high_card(hand1, hand2):
    return rank_cmp(high_card(hand1), high_card(hand2))


def cmp_one_pair(hand1, hand2):
    return cmp_n_of_kind(hand1, hand2, 2)


def cmp_two_pair(hand1, hand2):
    return pred_cmp(is_two_pair, hand1, hand2, tiebreaker=lambda h1, h2: rank_cmp(matching_kind(h1, 2), matching_kind(h2, 2)))


def cmp_three_of_kind(hand1, hand2):
    return cmp_n_of_kind(hand1, hand2, 3)


def cmp_straight(hand1, hand2):
    return pred_cmp(is_straight, hand1, hand2, tiebreaker=cmp_high_card)


def cmp_flush(hand1, hand2):
    return pred_cmp(is_flush, hand1, hand2, tiebreaker=cmp_high_card)


def cmp_full_house(hand1, hand2):
    return pred_cmp(is_full_house, hand1, hand2, tiebreaker=lambda h1, h2: cmp_three_of_kind(h1, h2) or cmp_n_of_kind(h1, h2, 2))


def cmp_four_of_kind(hand1, hand2):
    return cmp_n_of_kind(hand1, hand2, 4)


def cmp_straight_flush(hand1, hand2):
    return pred_cmp(is_straight_flush, hand1, hand2, tiebreaker=cmp_high_card)


def cmp_royal_flush(hand1, hand2):
    return pred_cmp(is_royal_flush, hand1, hand2)


def winner(hand1, hand2):
    for hand_cmp in HAND_COMPARERS:
        win = hand_cmp(hand1, hand2)
        if win is not None:
            return win
    return 0


HAND_COMPARERS = [
    cmp_royal_flush,
    cmp_straight_flush,
    cmp_four_of_kind,
    cmp_full_house,
    cmp_flush,
    cmp_straight,
    cmp_three_of_kind,
    cmp_two_pair,
    cmp_one_pair,
    cmp_high_card
]

def main():
    totals = defaultdict(lambda: 0)
    with open('poker.txt') as deals_fp:
        for deal in deals_fp:
            deal = deal.strip()
            cards = deal.split()
            hand1, hand2 = cards[:5], cards[5:]
            totals[winner(hand1, hand2)] += 1
    print(totals[1])


if __name__ == '__main__':
    main()
