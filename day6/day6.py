class Lanternfish():
    def __init__(self, _days: int):
        self.days = _days

    def simulate_day(self):
        if self.days <= 0:
            self.days = 6
            return 8
        else:
            self.days -= 1


if __name__ == '__main__':
    data = list(
            map(
                int, open(
                    "day6/input.txt", encoding="utf-8", mode="r"
                    ).read().split(','))
        )

    lanternfish_school = []

    for day in data:
        lanternfish_school.append(Lanternfish(day))
    
    for x in range(256):
        for lanternfish in lanternfish_school:
            new_lanternfish = lanternfish.simulate_day()
            if new_lanternfish == 8:
                lanternfish_school.append(Lanternfish(new_lanternfish + 1))

    for x in lanternfish_school:
        print(x.days)
    
    print('fish:', len(lanternfish_school))