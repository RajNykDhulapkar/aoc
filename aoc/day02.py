from aoc.utils import read_input, debug


def part1(data: str) -> int:
    def is_invalid(n: int) -> bool:
        s = str(n)
        mid = len(s) // 2
        return len(s) % 2 == 0 and s[:mid] == s[mid:]

    sum = 0
    for span in data.strip().split(","):
        lower, upper = map(int, span.split("-"))
        debug(f"Range: {lower} - {upper}")

        for num in range(lower, upper + 1):
            if is_invalid(num):
                sum += num
                debug(f"  Invalid number: {num}, current sum: {sum}")

    return sum


def part2(data: str) -> int:
    def is_invalid(num: int) -> bool:
        s = str(num)
        n = len(s)

        for d in range(2, n + 1):
            if n % d != 0:
                continue

            d_size = n // d
            first = s[0:d_size]

            if all(s[i * d_size : (i + 1) * d_size] == first for i in range(d)):
                return True

        return False

    sum = 0

    for span in data.strip().split(","):
        lower, upper = map(int, span.split("-"))
        debug(f"Range: {lower} - {upper}")

        for num in range(lower, upper + 1):
            if is_invalid(num):
                sum += num
                debug(f"  Invalid number: {num}, current sum: {sum}")

    return sum


if __name__ == "__main__":
    data = read_input(day=2)

    print("Part 1:", part1(data), end="\n\n")
    print("Part 2:", part2(data), end="\n\n")
