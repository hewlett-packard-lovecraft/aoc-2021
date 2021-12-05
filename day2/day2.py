from pathlib import Path

def task_1(input: list):
    depth = 0
    horizontal_position = 0

    for instruction in input:
        direction, distance = instruction.split(' ')
        distance = (int) (distance)

        match direction:
            case 'forward':
                horizontal_position += distance
            case 'down':
                depth += distance
            case 'up':
                depth -= distance

    return depth * horizontal_position

def task_2(input: list):
    depth = 0
    horizontal_position = 0
    aim = 0

    for instruction in input:
        direction, distance = instruction.split(' ')
        distance = (int) (distance)

        match direction:
            case 'forward':
                horizontal_position += distance
                depth += (aim * distance)
            case 'down':
                aim += distance
            case 'up':
                aim -= distance

    return depth * horizontal_position


if __name__ == '__main__':
    input = []

    with open(Path('./input.txt'), encoding='utf-8', mode='r') as f:
        for line in f:
            input.append(line.rstrip())

    print(task_2(input))
