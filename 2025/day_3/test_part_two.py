from part_two import total_joltage

data = ["987654321111111", "811111111111119", "234234234234278", "818181911112111"]


def test_password_value():
    assert total_joltage(data) == 3121910778619
