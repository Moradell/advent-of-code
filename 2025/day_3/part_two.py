from pathlib import Path

input_path = Path(__file__).parent / "input.txt"

input_data = input_path.read_text(encoding="utf-8")

data = input_data.split()


def max_numbers(s: str) -> int:
    stack = []
    k = len(s) - 12

    for digit in s:
        while stack and k > 0 and stack[-1] < digit:
            stack.pop()
            k -= 1
        stack.append(digit)

    while k > 0:
        stack.pop()
        k -= 1

    return int("".join(stack))


def total_joltage(data: list[str]) -> int:
    sum = 0

    for row in data:
        sum += max_numbers(row)

    return sum


print(total_joltage(data))
