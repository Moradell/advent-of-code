from pathlib import Path

input_path = Path(__file__).parent / "input.txt"

input_data = input_path.read_text(encoding="utf-8")

ranges_part, ids_part = input_data.strip().split("\n\n")
ranges = sorted([list(map(int, r.split("-"))) for r in ranges_part.strip().split("\n")])
ids = [int(id) for id in ids_part.strip().split("\n")]


def merge_ranges(ranges: list[list[int]]) -> list[list[int]]:
    output = [ranges[0]]

    for idx in range(1, len(ranges)):
        start, end = ranges[idx]
        last_interval = output[-1]
        last_end = last_interval[1]

        if start > last_end:
            output.append(ranges[idx])
        else:
            last_interval[1] = max(last_end, end)

    return output


def binary_search(list: list[list[int]], item: int) -> bool:
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        left_side, right_side = list[mid]

        if left_side <= item <= right_side:
            return True

        if right_side > item:
            high = mid - 1
        else:
            low = mid + 1

    return False


def available_ids(ranges, ids):
    count = 0
    merged_ranges = merge_ranges(ranges)

    for id in ids:
        is_available = binary_search(merged_ranges, id)

        if is_available:
            count += 1

    return count


print(available_ids(ranges, ids))
