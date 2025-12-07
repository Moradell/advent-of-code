from part_one import available_ids

ranges = [[3, 5], [10, 14], [12, 18], [16, 20]]
ids = [1, 5, 8, 11, 17, 32]


def test_available_ids():
    assert available_ids(ranges, ids) == 3
