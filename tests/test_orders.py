from app.orders import Order, order_total


def test_order_total_empty():
    assert order_total([]) == 0


def test_order_total_sums_amounts():
    orders = [Order("a", 10.0), Order("b", 2.5)]
    assert order_total(orders) == 12.5
