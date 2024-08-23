import pytest
from src.sample import add

def test_sample():
    assert add(5, 5) == 10
