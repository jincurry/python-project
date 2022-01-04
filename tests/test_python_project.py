from python_project import __version__
from python_project.math import multiply_two_numbers


def test_version():
    assert __version__ == "0.1.0"


def test_multiply_two_numbers():
    result = multiply_two_numbers(2, 3)
    assert result == 6
