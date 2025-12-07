from part_two import available_ids

ranges = [[3, 5], [10, 14], [12, 18], [16, 20]]


def test_available_ids():
    assert available_ids(ranges) == 14
