from converters.roman import Roman
import pytest

# TODO: add test case(s) to cover bad input
@pytest.mark.parametrize('test_input,expected', [
    ('I', 1),
])
def test_to_int(test_input, expected):
    """Test to_int() returns an integer given roman numerals."""
    converter = Roman()
    assert converter.to_int(test_input) == expected

@pytest.mark.parametrize('test_input,expected', [
    (1, 'I'),
])
@pytest.mark.skip(reason="Method not yet implemented")
def test_from_int(test_input, expected):
    """Test from_int() returns roman numerals given an integer."""
    assert Roman.from_int(test_input) == expected

@pytest.mark.parametrize('test_input,expected', [
    ('IV', True),
    ('IIII', False),
])
@pytest.mark.skip(reason="Method not yet implemented")
def test_validate(test_input, expected):
    """Test validate() returns the appropriate boolean."""
    assert Roman.validate(test_input) == expected
