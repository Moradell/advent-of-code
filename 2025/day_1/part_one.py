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

        if direction == "R":
            current_point += int(step[1:])
        else:
            current_point -= int(step[1:])

        current_point = int(math.fmod(current_point, 100))

        if current_point == 0:
            password += 1

    return password


print(pass_checker(input_data))
