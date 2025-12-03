

def part1():
    start: int = 50
    zero = 0
    print('----part one----')
    with open('hint1.txt') as f:
        lines = 'not empty'
        while lines:
            lines = f.readline().strip()
            if 'L' in lines:
                start = (start - int(lines[1:])) % 100
            elif 'R' in lines:
                start = (start + int(lines[1:])) % 100
            else:
                print('yo wtf')
            if start == 0:
                zero += 1
            print(f'from {lines} we add/sub {lines[1:]} go to {start}')
        print(f'part one {zero}')


def part2():
    print('----part two----')
    start: int = 50
    zero = 0
    with open('hint1.txt') as f:
        lines = 'not empty'
        while lines:
            print(f'starting at {start}', end=' ')
            lines = f.readline().strip()
            if lines:
                to_move = int(lines[1:])
                if 'L' in lines:
                    for _ in range(to_move):
                        start = (start - 1) % 100
                        if start == 0:
                            zero += 1

                    print(f'we move {lines} subbing {lines[1:]} go to {start}, zero at {zero}')
                elif 'R' in lines:
                    for _ in range(to_move):
                        start = (start + 1) % 100
                        if start == 0:
                            zero += 1
                    print(f'we move {lines} we adding {lines[1:]} go to {start}, zero at {zero}')
                else:
                    print('yo wtf')
        print(f'part two {zero}')
