import pytest

from app.formatting import format_cents


@pytest.mark.parametrize(
    ("cents", "expected"),
    [(0, "0.00 USD"), (100, "1.00 USD"), (1234, "12.34 USD"), (1205, "12.05 USD"), (5, "0.05 USD"), (-150, "-1.50 USD"), (-1, "-0.01 USD")],
)
def test_format_cents(cents, expected):
    assert format_cents(cents) == expected


def test_format_cents_custom_currency():
    assert format_cents(100, "EUR") == "1.00 EUR"
