def task_1(crabs):
    fuel_consumed = sum(crabs)  # some impossibly large number

    for pos in range(min(crabs), max(crabs)+1):
        fuel_consumed_next = 0

        for x in crabs:
            fuel_consumed_next += abs(x - pos)

        if fuel_consumed_next < fuel_consumed:
            fuel_consumed = fuel_consumed_next

    print(fuel_consumed)


def task_2(crabs):
    fuel_consumed = float('inf')  # some impossibly large number

    for pos in range(min(crabs), max(crabs)+1):
        fuel_consumed_next = 0

        for x in crabs:
            fuel_consumed_next += fuel_cost(abs(x - pos))

        if fuel_consumed_next <= fuel_consumed:
            fuel_consumed = fuel_consumed_next

    print(fuel_consumed)


def fuel_cost(n):
    return sum(range(n+1))


if __name__ == '__main__':
    path = "day7/input.txt"
    file = map(int, open(path, encoding="utf-8", mode="r").read().split(','))
    data = list(file)

    task_1(data)
    task_2(data)
