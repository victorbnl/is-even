__version__ = "1.0.7"


def is_even(number: int) -> bool:
    """Return whether `number` is even."""

    return number & 1 == 0
