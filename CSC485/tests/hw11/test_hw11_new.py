import pytest
from CSC485.Project.hw11.hw11new import get_scientific_name


def test_invalid_input_type():
    with pytest.raises(TypeError):
        get_scientific_name(123)

    with pytest.raises(TypeError):
        get_scientific_name(['apple'])

    with pytest.raises(TypeError):
        get_scientific_name({'fruit': 'apple'})

def test_unknown_fruit():
    with pytest.raises(KeyError):
        get_scientific_name('nonexistent_fruit')

def test_case_insensitive_lookup():
    assert get_scientific_name('ApPlE') == 'Malus domestica'
    assert get_scientific_name('OrAnGe') == 'Citrus × sinensis'

def test_get_scientific_name_with_whitespace():
    with pytest.raises(KeyError):
        get_scientific_name(' apple ')
    with pytest.raises(KeyError):
        get_scientific_name(' orange')

    with pytest.raises(KeyError):
        get_scientific_name(' grapefruit ')
