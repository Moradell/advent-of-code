from pathlib import Path

input_path = Path(__file__).parent / "input.txt"

input_data = input_path.read_text(encoding="utf-8")

data = input_data.split(",")


def prefix_function(s: str) -> list[int]:
    pi = [0] * len(s)
    j = 0
    i = 1
    while i < len(s):
        if s[i] == s[j]:
            pi[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                pi[i] = 0
                i += 1
            else:
                j = pi[j - 1]

    return pi


def is_periodic_kmp(s: str) -> bool:
    string_len = len(s)
    if string_len == 0:
        return False

    pi = prefix_function(s)

    max_valid_prefix = pi[-1]

    period = string_len - max_valid_prefix

    if max_valid_prefix > 0 and string_len % period == 0:
        return True

    return False


def get_invalid_code_sum(data):
    sum = 0
    for pair in data:
        [left_id, right_id] = pair.split("-")

        for id in range(int(left_id), int(right_id) + 1):
            is_periodic = is_periodic_kmp(str(id))

            if is_periodic:
                sum += id

    return sum
