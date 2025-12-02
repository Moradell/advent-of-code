import pytest
from part_one import pass_checker


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("L68 L30 R48 L5 R60 L55 L1 L99 R14 L82", 3),
        ("L50 R100 R48 L5 R60", 2),
        ("L50", 1),
        ("L49 R33 R48 L5 R60", 0),
    ],
)
def test_password_value(input_str, expected):
    assert pass_checker(input_str) == expected
