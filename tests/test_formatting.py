from app.formatting import format_cents


def test_format_cents():
    assert format_cents(1234) == "12.34 USD"
