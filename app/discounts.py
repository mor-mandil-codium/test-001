"""Discount helpers for orders."""

from app.orders import Order

DISCOUNT_CODES = {
    "WELCOME10": 10,
    "VIP25": 25,
}


def _validate_percent(percent: float) -> float:
    """Return `percent` as a float, raising ValueError if it is not a number in [0, 100]."""
    if isinstance(percent, bool) or not isinstance(percent, (int, float)):
        raise ValueError(f"Discount percent must be a number, got {percent!r}")
    if not 0 <= percent <= 100:
        raise ValueError(f"Discount percent must be between 0 and 100, got {percent}")
    return float(percent)


def apply_discount(order: Order, percent: float) -> float:
    """Return the order amount after applying a percentage discount."""
    percent = _validate_percent(percent)
    return order.amount - order.amount * percent / 100


def apply_codes(order: Order, codes: list[str] | None = None) -> float:
    """Apply every discount code in `codes` to the order, in sequence.

    Raises ValueError for an unknown code.
    """
    amount = order.amount
    for code in codes or []:
        if code not in DISCOUNT_CODES:
            raise ValueError(f"Unknown discount code: {code}")
        percent = DISCOUNT_CODES[code]
        amount = amount - amount * percent / 100
    return amount


def discount_ratio(original: float, discounted: float) -> float:
    """Return the fraction of the original amount that was discounted (0.0 for a zero original)."""
    if original == 0:
        return 0.0
    return (original - discounted) / original
