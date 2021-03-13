import pytest
from pytest import raises as r
# is_under_queen_attack(position, queen_position)
from yandex_testing_lesson import Rectangle

def test_type_1():
    with r(TypeError):
        Rectangle(1, '1')

def test_type_2():
    with r(TypeError):
        Rectangle('s', 1)
    
def test_value_1():
    with r(ValueError):
        Rectangle(12, -2)

def test_value_2():
    with r(ValueError):
        Rectangle(-12, 2)

def test_simple_1():
    assert Rectangle(2, 3).get_area() == 6

def test_simple_2():
    assert Rectangle(2, 3).get_perimeter() == 10