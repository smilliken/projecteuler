import itertools

MONTH_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


class Calendar:

    def __init__(self, year, month, day, day_of_week):
        """month, day, and day_of_week are 1-indexed"""
        self.year = year
        self.month = month
        self.day = day
        self.day_of_week = day_of_week

    def next(self):
        days_in_month = MONTH_DAYS[self.month - 1]
        if self.month == 2 and self.year % 4 == 0 and \
                (not self.year % 100 == 0 or self.year % 400 == 0):
            days_in_month = 29  # leap year
        if self.day < days_in_month:
            self.day += 1
        else:
            self.day = 1
            if self.month < 12:
                self.month += 1
            else:
                self.month = 1
                self.year += 1
        self.day_of_week = (self.day_of_week % 7) + 1

    def __iter__(self):
        while True:
            yield (self.year, self.month, self.day, self.day_of_week)
            self.next()


def main():
    print(len([1 for (year, month, day, day_of_week) in\
        itertools.takewhile(
            lambda date: date[0] <= 2000,
            Calendar(1900, 1, 1, 2)
        ) if year > 1900 and day_of_week == 1 and day == 1
    ]))


if __name__ == '__main__':
    main()
