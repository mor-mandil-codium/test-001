import pytest

from app.discounts import apply_codes, apply_discount, discount_ratio
from app.orders import Order


def test_apply_discount():
    assert apply_discount(Order("a", 100.0), 10) == 90.0


@pytest.mark.parametrize("percent", ["ten", -5, 150])
def test_apply_discount_rejects_invalid_percent(percent):
    with pytest.raises(ValueError):
        apply_discount(Order("a", 100.0), percent)


def test_apply_codes():
    assert apply_codes(Order("a", 100.0), ["WELCOME10", "VIP25"]) == 67.5


def test_apply_codes_rejects_unknown_code():
    with pytest.raises(ValueError):
        apply_codes(Order("a", 100.0), ["NOPE"])


def test_discount_ratio():
    assert discount_ratio(100.0, 75.0) == 0.25
    assert discount_ratio(0.0, 0.0) == 0.0
