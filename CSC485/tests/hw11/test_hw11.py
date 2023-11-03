import pytest
from CSC485.Project.hw11.hw11 import get_formal_name


def test_valid_input():
    assert get_formal_name('apple') == 'Malus domestica'
    assert get_formal_name('banana') == 'Musa acuminata'

def test_invalid_input():
    with pytest.raises(KeyError):
        get_formal_name('tomato')

def test_missing_input():
        with pytest.raises(KeyError):
             get_formal_name('')

def test_valid_input_with_whitespace():
    assert get_formal_name('  banana  ') == 'Musa acuminata'
    assert get_formal_name('   lemon') == 'Citrus limon'

def test_float_input():
    assert get_formal_name('4.64')
    if TypeError:
        assert True
    else:
        assert False

def test_multiple_input():
    assert get_formal_name('apple', 'banana')
    assert result

def test_nonalphanumeric_char():
    assert get_formal_name('$@')
    assert result

def test_1valid1invalidinput():
    assert get_formal_name('apple, tomato')
    assert result













