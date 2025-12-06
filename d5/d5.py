def jart1():
    print('----part one----')
    with open('hint1.txt') as f:
        lines = 'not empty'
        ranges = []
        while lines:
            lines = f.readline().strip()
            if lines:
                interval = lines.split(sep='-')
                ranges.append([int(interval[0]), int(interval[1])])
            else:
                break
        lines = 'srcond part'
        count = 0
        while lines:
            lines = f.readline().strip()
            if lines:
                for number in ranges:
                    if int(lines) >= number[0] and int(lines) <= number[1]:
                        count += 1
                        break
        print(f'count is {count}')


# part1()
def part2():
    print('----part two----')
    with open('hint1.txt') as f:
        lines = 'not empty'
        ranges = []
        while lines:
            lines = f.readline().strip()
            if lines:
                interval = lines.split(sep='-')
                ranges.append([int(interval[0]), int(interval[1])])
            else:
                break
        ranges.sort()

        merged = []
        for interval in ranges:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        total = sum(end - start + 1 for start, end in merged)
        print(f'count is {total}')


part2()
