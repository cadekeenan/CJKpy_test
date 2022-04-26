# test_calculator.py

# Assert statements
# https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug

# python3 -m unittest test_calculator.py
import app
import unittest
import tests.calculator as calc

class TestCalculator(unittest.TestCase):  

    def  test_calculate_top(): 
        """
    GIVEN a user enters 180 as the radius 
    WHEN that radius is passed to this function 
    THEN the user's top area is accurately created
    """
    assert app.calculate_top(180)== 101736

def  test_calculate_side(): 
    """
    GIVEN a user enters 180 as the radius and 360 as height
    WHEN that radius and height is passed to this function 
    THEN the user's side area is accurately created
    """
    assert app.calculate_side(180,360)== 406944
