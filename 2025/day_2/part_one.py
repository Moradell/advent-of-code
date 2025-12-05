from pathlib import Path

input_path = Path(__file__).parent / "input.txt"

input_data = input_path.read_text(encoding="utf-8")

data = input_data.split(",")


def get_invalid_code_sum(data):
    sum = 0
    for pair in data:
        [left_id, right_id] = pair.split("-")

        for id in range(int(left_id), int(right_id)):
            stringify_id = str(id)
            if len(stringify_id) % 2 == 1:
                continue

            mid = len(stringify_id) // 2
            left_side, right_side = stringify_id[:mid], stringify_id[mid:]

            if left_side == right_side:
                sum += id

    return sum


print(get_invalid_code_sum(data))
