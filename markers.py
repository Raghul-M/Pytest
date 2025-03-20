import pytest
import sys

@pytest.mark.skip(reason="Feature not implemented yet")
def test_not_ready():
    assert False

@pytest.mark.xfail(reason="Bug #123, Fix in progress")
def test_known_bug():
    assert 1 + 1 == 3


@pytest.mark.parametrize("x, y, result", [
    (1, 2, 3),
    (2, 3, 5),
    (5, 5, 10)
])
def test_addition(x, y, result):
    assert x + y == result


@pytest.mark.skipif(sys.version_info < (3, 10), reason="Requires Python 3.10 or higher")
def test_new_feature():
    assert True
