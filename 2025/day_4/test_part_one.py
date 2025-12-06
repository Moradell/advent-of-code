from part_one import total_accesed_rolls

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
    assert total_accesed_rolls(data) == 13
