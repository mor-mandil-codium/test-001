from app.discounts import apply_codes, apply_discount, discount_ratio
from app.orders import Order


def test_apply_discount():
    assert apply_discount(Order("a", 100.0), 10) == 90.0


def test_apply_codes():
    assert apply_codes(Order("a", 100.0), ["WELCOME10"]) == 90.0


def test_discount_ratio():
    assert discount_ratio(100.0, 75.0) == 0.25
