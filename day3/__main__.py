from pathlib import Path


def task_1(diagnostic_report: list[list[str]]):
    gamma = ''

    for col in range(len(diagnostic_report[0])):
        zero_counter = 0
        one_counter = 0

        for row in diagnostic_report:
            match row[col]:
                case '0':
                    zero_counter += 1
                case '1':
                    one_counter += 1

        if zero_counter > one_counter:
            gamma += '0'
        else:
            gamma += '1'

    epsilon = ''

    for col in range(len(diagnostic_report[0])):
        zero_counter = 0
        one_counter = 0

        for row in diagnostic_report:
            match row[col]:
                case '0':
                    zero_counter += 1
                case '1':
                    one_counter += 1

        if zero_counter < one_counter:
            epsilon += '0'
        else:
            epsilon += '1'

    gammaanswer = int(gamma, 2)
    epsilonanswer = int(epsilon, 2)

    print(epsilonanswer)
    print(gammaanswer)
    print(gammaanswer * epsilonanswer)


def task_2(diagnostic_report: list[list[str]]):

    for col in range(len(diagnostic_report[0])):
        zero_counter = 0
        one_counter = 0

        for row in diagnostic_report:
            match row[col]:
                case '0':
                    zero_counter += 1
                case '1':
                    one_counter += 1

        if zero_counter < one_counter:
            epsilon += '0'
        else:
            epsilon += '1'

    print()


if __name__ == '__main__':
    diagnostic_report = []

    with open(Path('./input.txt'), encoding='utf-8', mode='r') as f:
        for line in f:
            diagnostic_report.append(list(line.rstrip()))

    task_1(diagnostic_report=diagnostic_report)
    task_2(diagnostic_report=diagnostic_report)
