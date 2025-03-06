from algorithms.fibonacci import fibonacci


def test_fibonacci_0():
    x: int = fibonacci(0)
    assert 0 == x


def test_fibonacci_1():
    x: int = fibonacci(1)
    assert 1 == x


def test_fibonacci_5():
    assert 8 == fibonacci(6)
