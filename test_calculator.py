from calculator import Calculator
import converters.roman as roman
import pytest

@pytest.mark.parametrize('test_input,expected', [
    ('I+II', ['I', '+', 'II']),   # Base case
    ('I + II', ['I', '+', 'II']), # Whitespace insensitive
    ('i + iI', ['i', '+', 'iI']), # Tokenize is converter-agnostic
])
def test_tokenize(test_input, expected):
    """Test tokenize() properly parses input strings.
    TODO: Should number validation happen in tokenize?
    """
    calculator = Calculator(roman)
    assert calculator.tokenize(test_input) == expected


@pytest.mark.parametrize('test_input,expected', [
    (['I', '+', 'II'], ['1', '+', '2']), # Base case
    (['i', '+', 'iI'], ['1', '+', '2']), # Doublecheck converter is case-insensitive
])
def test_convert(test_input, expected):
    """Test convert() returns list of terms with roman numerals
    replaced by their integer equivalents.
    """
    calculator = Calculator(roman)
    assert calculator.convert(test_input) == expected

@pytest.mark.parametrize('test_input,expected', [
    ('I+I', 'II'),      # +
    ('II*III', 'VI'),   # *
    ('VI/II', 'III'),   # /
    ('III-I', 'II'),    # -
    ('II**III', 'VIII') # **
])
def test_calculate_simple(test_input, expected):
    """Test calculate() performs basic math from string expression."""
    calculator = Calculator(roman)
    assert calculator.calculate(test_input) == expected

@pytest.mark.parametrize('test_input,expected', [
    ('III+V/II*II', 'II'), # multiplication then division then addition
    ('(III+V/II)*II', 'VIII') # inside parens then outside parens
])
@pytest.mark.skip(reason="Method not implemented yet")
def test_calculate_complex(test_input, expected):
    """Test calculate() observes order of operations."""
    calculator = Calculator(roman)
    assert calculator.calculate(test_input) == expected
