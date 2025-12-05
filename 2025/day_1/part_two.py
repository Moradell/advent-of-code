import math
from pathlib import Path

input_path = Path(__file__).parent / "input.txt"
input_data = input_path.read_text(encoding="utf-8")


def pass_checker(input):
    steps = input.split()

    password = 0
    current_point = 50

    for step in steps:
        direction = step[0]
        distance = int(step[1:])

        old_point = current_point

        if direction == "R":
            new_point = current_point + distance
        else:
            new_point = current_point - distance

        low = min(old_point, new_point)
        high = max(old_point, new_point)

        first_multiple = math.ceil(low / 100) * 100
        if first_multiple <= high:
            count = (high - first_multiple) // 100 + 1
        else:
            count = 0

        if old_point % 100 == 0:
            count -= 1

        password += count
        current_point = new_point

    return password


print(pass_checker(input_data))
