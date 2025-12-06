def part1():
    print('----part one----')
    sum = 0
    with open('hint1.txt') as f:
        lines = 'not empty'
        while lines:
            max = 0
            lines = f.readline().strip()
            if not lines:
                break
            length = len(lines)
            j = 0
            for i in range(length):
                j = i + 1
                while j < length:
                    curr = int(lines[i]) * 10 + int(lines[j])
                    if curr > max:
                        max = curr
                    j += 1
            sum += max
            print(f'local max is {max}')
    print(f'sum of max is {sum}')

# part1()
def part2():
    print('----part two----')
    total = 0

    def generate_combinations(n, k):
        # Generate all combinations of k elements from range(n)
        if k > n or k < 0:
            return

        # Initialize first combination [0, 1, 2, ..., k-1]
        combo = list(range(k))

        while True:
            yield combo[:]

            # Find the rightmost element that can be incremented
            i = k - 1
            while i >= 0 and combo[i] == n - k + i:
                i -= 1

            # If no element can be incremented, we're done
            if i < 0:
                break

            # Increment this element and reset all elements to its right
            combo[i] += 1
            for j in range(i + 1, k):
                combo[j] = combo[j - 1] + 1

    with open('hint1.txt') as f:
        lines = 'not empty'
        while lines:
            max_val = 0
            lines = f.readline().strip()
            if not lines:
                break
            length = len(lines)
            num_to_skip = length - 12

            for skip_indices in generate_combinations(length, num_to_skip):
                skip_set = set(skip_indices)
                result_digits = [lines[i] for i in range(length) if i not in skip_set]
                curr = int(''.join(result_digits))
                if curr > max_val:
                    max_val = curr
            total += max_val
            print(f'local max is {max_val}')
    print(f'sum of max is {total}')

part2()
