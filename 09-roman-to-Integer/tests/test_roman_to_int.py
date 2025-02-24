# test_calculadora.py
import pytest
from main import Solution


# Configuración común para todos los tests
@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "roman_number, expected",
    [
        ("", False),
        ("I", True),
        ("MD", True),
        ("MMMMMMMMMMMMMMM", True),  # 15 caracteres válidos
        ("MMMMMMMMMMMMMMMMM", False),  # 16 caracteres válidos
    ],
)
def test_validate_roman_number_lenth(solution, roman_number, expected):
    result = solution.validate_roman_number_lenth(roman_number)
    assert result == expected


@pytest.mark.parametrize(
    "roman_number, expected",
    [
        ("MD", True),
        ("JMD", False),
        ("MCMXCIV", True),
        ("ABC", False),
        ("", False),  # Cadena vacía es válida en términos de caracteres
    ],
)
def test_validate_roman_number_caracters(solution, roman_number, expected):
    result = solution.validate_roman_number_caracters(roman_number)
    assert result == expected


@pytest.mark.parametrize(
    "roman_number, expected",
    [
        ("III", 3),
        ("IV", 4),
        ("IX", 9),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
    ],
)
def test_roman_to_integer(solution, roman_number, expected):
    result = solution.roman_to_integer(roman_number)
    assert result == expected
