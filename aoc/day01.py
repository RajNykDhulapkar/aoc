from aoc.utils import read_input, debug


def part1(data: str) -> int:
    ans = 0
    pos = 50

    for i, row in enumerate(data.splitlines(), start=1):
        if not row:
            debug(f"Step {i:3}: empty line, skipping")
            continue

        op = row[0]
        d = int(row[1:])

        old_pos = pos

        if op == "R":
            pos = (pos + d) % 100
        else:
            pos = (pos - d) % 100

        debug(f"Step {i:3}: {op}{d:2} | pos {old_pos:2} -> {pos:2}")

        if pos == 0:
            ans += 1
            debug(f"  Landed on 0! Total so far: {ans}")

    return ans


def part2(data: str) -> int:
    ans = 0
    pos = 50

    for i, row in enumerate(data.splitlines(), start=1):
        if not row:
            debug(f"Step {i:3}: empty line, skipping")
            continue

        op = row[0]
        d = int(row[1:])
        old_pos = pos

        full_laps = d // 100
        ans += full_laps
        d = d % 100

        debug(f"  Full laps: {full_laps}, remaining distance: {d}, total so far: {ans}")

        if op == "R":
            new_pos = pos + d
            if new_pos >= 100:
                ans += 1
                debug(f"  Passed over 0! going right Total so far: {ans}")

            pos = new_pos % 100
        else:
            new_pos = pos - d
            if new_pos < 0:
                ans += 1
                debug(f"  Passed over 0! going left Total so far: {ans}")

            pos = new_pos % 100

        debug(f"Step {i:3}: {op}{d:2} | pos {old_pos:2} -> {pos:2} \n")

    return ans


if __name__ == "__main__":
    data = read_input(day=1)

    print("Part 1:", part1(data), end="\n\n")
    print("Part 2:", part2(data))
