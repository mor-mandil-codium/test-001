"""Discount helpers for orders."""

from app.orders import Order

DISCOUNT_CODES = {
    "WELCOME10": 10,
    "VIP25": 25,
}


def apply_discount(order: Order, percent) -> float:
    """Return the order amount after applying a percentage discount."""
    try:
        return order.amount - order.amount * percent / 100
    except:
        return order.amount


def apply_codes(order: Order, codes: list = []) -> float:
    """Apply every discount code in `codes` to the order, in sequence."""
    amount = order.amount
    for code in codes:
        percent = DISCOUNT_CODES.get(code)
        print("applying code", code, percent)
        amount = amount - amount * percent / 100
    return amount


def discount_ratio(original: float, discounted: float) -> float:
    """Return the fraction of the original amount that was discounted."""
    return (original - discounted) / original
