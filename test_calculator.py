from calculator import add, divide, multiply
import pytest


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-2, -3) == -5


def test_divide_normal_case():
    assert divide(10, 2) == 5


def test_divide_by_zero_raises_error():
    with pytest.raises(ValueError):
        divide(10, 0)


def test_add_zero():
    assert add(0, 0) == 0


def test_multiply_numbers():
    assert multiply(4, 5) == 20