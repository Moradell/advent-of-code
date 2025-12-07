from pathlib import Path

input_path = Path(__file__).parent / "input.txt"

input_data = input_path.read_text(encoding="utf-8")

ranges_part, ids_part = input_data.strip().split("\n\n")
ranges = sorted([list(map(int, r.split("-"))) for r in ranges_part.strip().split("\n")])
ids = [int(id) for id in ids_part.strip().split("\n")]


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    output = [intervals[0]]

    for idx in range(1, len(intervals)):
        start, end = intervals[idx]
        last_interval = output[-1]
        last_end = last_interval[1]

        if start > last_end:
            output.append(intervals[idx])
        else:
            last_interval[1] = max(last_end, end)

    return output


def available_ids(ranges):
    count = 0
    merged_intervals = merge_intervals(ranges)

    for interval in merged_intervals:
        count += (interval[1] - interval[0]) + 1

    return count


print(available_ids(ranges))
