from pathlib import Path

input_path = Path(__file__).parent / "input.txt"

input_data = input_path.read_text(encoding="utf-8")

data = input_data.split()


def get_max_pair(s: str) -> int:
    for tens in range(9, 0, -1):
        for units in range(9, 0, -1):
            candidate = tens * 10 + units

            tens_str = str(tens)
            units_str = str(units)

            tens_pos = s.find(tens_str)

            if tens_pos == -1:
                continue

            units_pos = s.find(units_str, tens_pos + 1)
            if units_pos != -1:
                return candidate
    return 0


def total_joltage(data: list[str]) -> int:
    sum = 0

    for row in data:
        sum += get_max_pair(row)

    return sum


print(total_joltage(data))
