"""Discount helpers for orders."""

from app.orders import Order

DISCOUNT_CODES = {
    "WELCOME10": 10,
    "VIP25": 25,
}


def apply_discount(order: Order, percent: float) -> float:
    """Return the order amount after a percentage discount in [0, 100]."""
    if isinstance(percent, bool) or not isinstance(percent, (int, float)) or not 0 <= percent <= 100:
        raise ValueError(f"Discount percent must be a number between 0 and 100, got {percent!r}")
    return order.amount - order.amount * percent / 100


def apply_codes(order: Order, codes: list[str] | None = None) -> float:
    """Apply known discount codes in sequence; raise ValueError for an unknown code."""
    amount = order.amount
    for code in codes or []:
        if code not in DISCOUNT_CODES:
            raise ValueError(f"Unknown discount code: {code}")
        amount -= amount * DISCOUNT_CODES[code] / 100
    return amount


def discount_ratio(original: float, discounted: float) -> float:
    """Return the discounted fraction of `original`, or 0.0 when original is zero."""
    if original == 0:
        return 0.0
    return (original - discounted) / original
