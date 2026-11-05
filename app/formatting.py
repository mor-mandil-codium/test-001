"""Money formatting helpers."""


def format_cents(cents: int, currency: str = "USD") -> str:
    """Format an integer amount of cents as a human-readable price, e.g. 1234 -> '12.34 USD'."""
    return f"{cents / 100:.2f} {currency}"
