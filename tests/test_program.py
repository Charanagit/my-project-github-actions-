import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import program


def test_add_numbers():
    assert program.add_numbers(2, 3) == 5
    assert program.add_numbers(-1, 1) == 0
    assert program.add_numbers(0, 0) == 0

def test_subtract_numbers():
    assert program.subtract_numbers(5, 3) == 2
    assert program.subtract_numbers(-1, 1) == -2
    assert program.subtract_numbers(0, 0) == 0
