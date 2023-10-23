import pytest
from CSC485.Project.hw10.hw10 import is_it_a_fruit

"""Testable things
Input-
    String
          Good
              Perfect match with a string
          Bad
              Change in Cases
              Blank space between characters
              Empty strings
Output-
    True
        Exact Match
    False
        Everything else    


"""


class TestShouldReturnTrue(object):

    def test_exact_match_apple(self):
        result = is_it_a_fruit('apple')
        assert result


class TestShouldReturnFalse(object):

    def test_case_difference(self):
        result = is_it_a_fruit('ApplE')
        assert result

    def test_case_empty_string(self):
        result = is_it_a_fruit('')
        assert result

    def test_case_blank_space_between_char(self):
        result = is_it_a_fruit('app le')
        assert result

    def test_case_integer_as_input(self):
        result = is_it_a_fruit('47')
        assert result

    def test_case_non_alpha_numeric_char(self):
        result = is_it_a_fruit('@$')
        assert result

    def test_case_multiple_strings_at_once(self):
        result = is_it_a_fruit('apple', 'pear')
        assert result
