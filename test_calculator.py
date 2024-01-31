# To create unit tests for the calculator program, we'll employ the pytest framework, a built-in component of Python's standard library. 
# These tests aim to validate the functionality of each calculator function (addition, subtraction, multiplication, division) and ensure 
# their proper execution across different scenarios.

import pytest
from calculator import add 
from calculator import subtract
from calculator import multiply
from calculator import divide

# The below defined tests i:e test_addition : Tests that the add function correctly works in each and every case defined including negative integers.
# The below defined tests i:e test_subtraction : Tests that the subtract function correctly works in each and every case defined including negative integers.
# The below defined tests i:e test_multiplication : Tests that the multiply function correctly works in each and every case defined including negative integers.
# The below defined tests i:e test_divide : Tests that the divide function correctly works in each and every case defined including negative integers.



class TestCalculatorFunctions():

    def test_addition(self):
        result = add(4, 5)
        assert result == 9
        result = add(-4, 5)
        assert result == 1 
        result = add(-7, -3)
        assert result ==-10
        

    def test_subtraction(self):
        result = subtract(8, 3)
        assert result == 5
        result = subtract(-8, 3)
        assert result == -11
        result = subtract(8, -3)
        assert result == 11
        result = subtract(-8, -3)
        assert result == -5

    def test_multiplication(self):
        result = multiply(4, 6)
        assert result == 24
        result = multiply(-4, 6)
        assert result == -24
        result = multiply(4, -6)
        assert result == -24
        result = multiply(-4, -6)
        assert result == 24

    def test_division(self):
        result = divide(9, 3)
        assert result == 3
        result = divide(-9, 3)
        assert result == -3
        result = divide(9, -3)
        assert result == -3
        result = divide(-9, -3)
        assert result == 3
        result = divide(0, 3)
        assert result == 0

        result = divide(10, 0)
        assert result == "Infinite result !! Division by zero NOT POSSIBLE"


# Over here the tests defined below i:e 
#   test_non_numeric_input_expected_exception(self), test_multiply_non_numeric_input_expected_exception(self), 
#   test_subtract_non_numeric_input_expected_exception(self) ensures testing when the user enters a non-numeric
#   input for the calculator operation

    def test_non_numeric_input_expected_exception(self):
        with pytest.raises(ValueError):
            add("abc", 5)
    
    def test_multiply_non_numeric_input_expected_exception(self):
        with pytest.raises(ValueError):
            multiply("abc", 5)

    def test_subtract_non_numeric_input_expected_exception(self):
        with pytest.raises(ValueError):
            subtract("abc", 5)
    
if __name__ == "__main__":
   pytest.main() 


## To run the tests we have to make sure that the test_calculator.py , calculator.py and calculator_f.py are in the same directory otherwise
## we would have to provide the specific path where these files are. TO RUN THE TESTS WE CAN WRITE A COMMAND IN THE TERMINAL 
## pytest test_calculator.py This command would trigger the unit tests and we would be able to see if the tests passed or failed.
## The no of dots specified let us know the number of tests passed.
