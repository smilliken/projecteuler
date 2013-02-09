import itertools


def yield_solutions(seed, candidate_groups):
    for next_ in candidate_groups:
        if len(seed) == 4:
            yield seed + [next_]
        else:
            next_candidates = [group for group in candidate_groups if len(set(next_).intersection(set(group))) == 0\
                or (len(set(next_).intersection(set(group))) == 1 and (next_[-1] == group[1] or not seed and next_[1] == group[-1]))]
            if next_candidates:
                for solution in yield_solutions(seed + [next_], next_candidates):
                    yield solution            


def main():
    solutions = []
    groups = list(itertools.permutations(range(1, 11), 3))
    for sum_ in xrange(max([sum(group) for group in groups]) + 1):
        for candidate in yield_solutions([], [group for group in groups if sum(group) == sum_]):
            if not any([set(candidate) == set(solution) for solution in solutions]):
                solutions.append(candidate)
    solutions = [''.join([''.join([str(n) for n in group]) for group in solution]) for solution in solutions]
    solutions = [int(solution) for solution in solutions if len(solution) == 16]
    print(max(solutions))

if __name__ == '__main__':
    main()
