import pytest


def multiply(a, b):
    """Return the product of two numbers, or None if either input is not numeric."""
    # bool is a subclass of int in Python, so exclude it explicitly
    if not all(isinstance(x, (int, float)) and not isinstance(x, bool) for x in (a, b)):
        return None
    return a * b


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (3, 4, 12),
        (-9, -4, 36),
        (6, -3, -18),
        (-4, 0, 0),
        (0, 4, 0),
        ("abc", "xyz", None),
    ],
    ids=[
        "two positive numbers",
        "two negative numbers",
        "mix of numbers",
        "zero from the left",
        "zero from the right",
        "non numeric inputs",
    ],
)
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected