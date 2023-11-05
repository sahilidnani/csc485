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
    with pytest.raises(KeyError):
        get_formal_name('ban an a')



def test_float_input():
    with pytest.raises(KeyError):
        get_formal_name('4.64')



def test_multiple_input():
    with pytest.raises(KeyError):
        get_formal_name('apple', 'banana')


def test_nonalphanumeric_char():
    with pytest.raises(KeyError):
            get_formal_name('$@')


def test_1valid1invalidinput():
    with pytest.raises(TypeError):
        get_formal_name('apple', 'tomato')
