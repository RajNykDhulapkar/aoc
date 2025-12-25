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


if __name__ == "__main__":
    data = read_input(day=2)

    print("Part 1:", part1(data), end="\n\n")
