# Name: Jack Walmsley
# Date: 2020-03-09
# Filename: JackWalmsleyCalculator.py
# Purpose: To create a calculator to answer a user's basic math problems
import re

print("Welcome to the calculator")
operator_pattern = re.compile('[+\-/*]')  # Regex to find mathematical operators + - / *


class OperatorException(Exception):
    """
    Raised when the second term in the problem isn't an operator
    """
    pass


# User input testing
while True:
    problem = input("Please type in a math problem(keep terms space-separated): ")
    problemTerms = problem.split(" ")
    # first term (number)
    try:
        number1 = int(problemTerms[0])
    except ValueError:
        print("Sorry, \"", problemTerms[0], "\" is not an accepted number")
        continue
    except IndexError:  # problemTerms is not long enough
        continue

    # second term (operator)
    try:
        if operator_pattern.match(problemTerms[1]):
            operator = problemTerms[1]
        else:
            raise OperatorException
    except OperatorException:
        print("Sorry, \"", problemTerms[1], "\" is not an accepted operator")
        continue
    except IndexError:  # problemTerms is not long enough
        print("Invalid format. Remember, problem terms must be space-separated(eg. 8 + 5 not 8+5)")
        continue

    # third term (number)
    try:
        number2 = int(problemTerms[2])
    except ValueError:
        print('Sorry, \"', problemTerms[2], '\" is not an accepted number')
        continue
    except IndexError:  # problemTerms is not long enough
        continue
    print(eval(problem))
