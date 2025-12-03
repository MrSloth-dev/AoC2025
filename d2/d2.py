def check_double(s: str):
    length = len(s)
    for i in range(length):
        chunks, chunk_size = len(s), len(s) // (i + 1)
        split = [s[i : i + chunk_size] for i in range(0, chunks, chunk_size)]
        no_repeat = set(split)
        if len(split) != 1 and len(no_repeat) == 1:
            return True
    else:
        return False


def part1():
    print('---part 1---')
    invalid = 0
    with open('hint1.txt') as file:
        data = file.read()
        list = data.split(sep=',')
        for a in list:
            rang = a.split(sep='-')
            for r in range(int(rang[0]), int(rang[1]) + 1):
                string = str(r)
                if string[0 : len(string) // 2] == string[len(string) // 2 :]:
                    invalid += r
                    print(r)
    print(f'part 1 answer is {invalid}')


def part2():
    invalid = 0
    print('---part 2---')
    with open('hint1.txt') as file:
        data = file.read()
        list = data.split(sep=',')
        for a in list:
            rang = a.split(sep='-')
            for r in range(int(rang[0]), int(rang[1]) + 1):
                string = str(r)
                if string[0 : len(string) // 2] == string[
                    len(string) // 2 :
                ] or check_double(string):
                    invalid += r
                    print(r)
    print(f'part 2 answer is {invalid}')


part2()
