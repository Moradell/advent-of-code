from part_two import total_removed_rolls

data = [
    list("..@@.@@@@."),
    list("@@@.@.@.@@"),
    list("@@@@@.@.@@"),
    list("@.@@@@..@."),
    list("@@.@@@@.@@"),
    list(".@@@@@@@.@"),
    list(".@.@.@.@@@"),
    list("@.@@@.@@@@"),
    list(".@@@@@@@@."),
    list("@.@.@@@.@."),
]


def test_password_value():
    assert total_removed_rolls(data) == 43
