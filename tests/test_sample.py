import pytest
from src.sample import add

def test_sample_success():
    assert add(5, 5) == 10

# def test_sample_failure():
#     assert add(5, 5) == 55
