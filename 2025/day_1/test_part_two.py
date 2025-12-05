import pytest
from part_two import pass_checker


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("L49", 0),
        ("L50", 1),
        ("L68", 1),
        ("L50 R300 R48 L5", 4),
        ("L50 R300 R48 L5 L33 R25 L33 L2 L122", 6),
    ],
)
def test_password_value(input_str, expected):
    assert pass_checker(input_str) == expected
