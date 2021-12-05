from pathlib import Path

def part1(input: list[int]):
    counter = 0
    previous_number = input[0]

    for number in input:
        if number > previous_number:
            counter += 1

        previous_number = number

    return counter

def part2(input: list[int]):
    counter = 0
    triplets = sliding_depth_window(input, 3)
    previous_number = triplets[0]

    for number in triplets:
        if number > previous_number:
            counter += 1

        previous_number = number

    return counter


def sliding_depth_window(data: list, window: int):
        return [sum(data[i:i + window:]) for i, v in enumerate(data[:1 - window:])]

if __name__ == '__main__':
    input = []

    with open(Path('./input.txt'), encoding='utf-8', mode='r') as f:
        for line in f:
            input.append((int) (line))


    #print(part1(input))
    print(part2(input))
    #print(sliding_depth_window(input, 3))

