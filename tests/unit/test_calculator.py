# test_calculator.py

# Assert statements
# https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug

# python3 -m unittest test_calculator.py

import unittest
import tests.calculator as calc

class TestCalculator(unittest.TestCase):  #test class
    
import app

def  test_calculate_top_area(): 
    """
    GIVEN a user enters 180 as the radius 
    WHEN that radius is passed to this function 
    THEN the user's top area is accurately created
    """
    assert app.calculate_top_area(180)== 101736

def  test_calculate_side_area(): 
    """
    GIVEN a user enters 180 as the radius and 360 as height
    WHEN that radius and height is passed to this function 
    THEN the user's side area is accurately created
    """
    assert app.calculate_side_area(180,360)== 406944
