"""Order helpers."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Order:
    order_id: str
    amount: float
    currency: str = "USD"


def order_total(orders: list[Order]) -> float:
    """Return the sum of all order amounts."""
    return sum(order.amount for order in orders)
