def format_cents(cents: int) -> str:
    sign = "-" if cents < 0 else ""
    cents = abs(cents)
    return f"{sign}${cents // 100}.{cents % 100:02d}"


def average_price(prices: list[int]) -> int:
    return sum(prices) // len(prices)
