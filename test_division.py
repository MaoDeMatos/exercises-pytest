import pytest

def divide(a, b):
  if (b == 0):
    return ZeroDivisionError
  return a / b

# @pytest.mark.current
def test_divide_param_type(a = 6, b = 3):
  assert type(a) is int
  assert type(b) is int

def test_divide_success_a(a = 6, b = 2):
  assert divide(a, b) == 3

@pytest.mark.skip(reason="Broken test")
def test_divide_success_b(a = 1922, b = 62):
  assert divide(a, b) == 39

def test_divide_fail(a = 6, b = 3):
  assert divide(a, b) != 3

def test_divide_by_zero(a = 645, b = 0):
  assert divide(a, b) is ZeroDivisionError
