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



