import sys
import os

# Add the ../src directory to the import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from rotation_function import strip_rotation

def test_100_returns_100():
    """Simple test case for to make sure the strip rotation function works"""
    rotation_number = strip_rotation(100)
    assert rotation_number == 100

def test_460_returns_100():
    """Simple test case for to make sure the strip rotation function works for numbers above 360"""
    rotation_number = strip_rotation(460)
    assert rotation_number == 100
    

# def test_820_returns_100():
#     pass

# def test_negative_100_returns_260():
#     pass

# def test_negative_460_returns_260():
#     pass

# def test_negative_820_returns_260():
#     pass

# def test_non_numeric_catches_exception():
#     pass