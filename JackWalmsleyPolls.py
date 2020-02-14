# Name: Jack Walmsley
# Date: 2019-02-10
# Filename: JackWalmsleyPolls.py
# Purpose: To create a user poll with three questions and error-checking, which gives the user some interesting data
# based on their answers

# Percentages for different answers
enjoysMathStats = {True: 63, False: 12}  # Do you enjoy math?
englishFirstLangStats = {True: 94, False: 6}  # Is english your first language?
generationStats = {14: 15.8,
                   24: 11.5,
                   54: 40.5,
                   64: 14.1,
                   130: 18.1}  # How old are you? Keys are maximum ages for each generation (eg. 0-14, 15-24, etc.)


class InputGetter:
    def __init__(self, prompt, fail_message):
        self.prompt = prompt  # The prompt to ask for input with
        self.fail_message = fail_message  # The error message when the input is of the wrong type

    def get_int(self, min_val=None, max_val=None):
        """
        Loops until the user provides a valid integer from maxVal to minVal

        :param min_val: The minimum input, inclusive (Default None)
        :type min_val: int
        :param max_val: The maximum input, inclusive (Default None)
        :type max_val: int

        :return int: The user's final input
        """
        while True:
            user_in = input(self.prompt + ' ')  # Add a space to the end of the question for readability
            try:
                user_in = int(user_in)
                # If min and max exist and input is not within them, raise ValueError
                if min_val is not None and max_val is not None:
                    if not (max_val >= user_in >= min_val):
                        raise ValueError
            except ValueError:
                print(self.fail_message)
                continue
            else:
                # Input is correct type and within min and max
                return user_in

    def get_bool(self, true_inputs=("yes", "yep", "true", "definitely", "totally"),
                 false_inputs=("no", "false", "nope", "never")):
        """
        Loops until the user provides a bool input, as decided by trueInput and falseInput
        :param true_inputs: The user inputs to be understood as True
        :type true_inputs: list
        :param false_inputs: The user inputs to be understood as False
        :type false_inputs: list

        :return bool: The user's final input
        """

        while True:
            user_in = input(self.prompt + ' ')  # Add a space to the end of the question for readability
            if user_in.lower() in true_inputs:  # lower() to remove capitalization just in case user types "Yes", for example
                return True
            elif user_in.lower() in false_inputs:
                return False
            else:
                print(self.fail_message)
                continue


# Poll questions
print('Welcome to the fun poll thingy!')
print('Data sources: 2017 Math EQAO, 2018 Peel Student Census, 2016 Canadian Census')

# Do you enjoy math?
enjoysMath = InputGetter("Do you enjoy math?",
                         "Sorry, this is a yes or no question").get_bool()
if enjoysMath:
    print('63% of PCSS students agree with you!')
else:
    print('12% of PCSS students agree with you!')

# Is english your first language?
englishFirstLang = InputGetter("Do you speak english as your first language?",
                               "Sorry, this is a yes or no question").get_bool()
if englishFirstLang:
    print('So does 94% of the school!')
else:
    print('6% of the school doesn\'t either!')

# How old are you?
userAge = InputGetter("How old are you?", "Sorry, I need a whole number from 0 to 130").get_int(0, 130)
for age in generationStats:
    if userAge <= age:
        print(generationStats[age], 'percent of Canadians are in the same generation as you!')
        # Stop the loop so it doesn't print every generation above the correct one
        break

print('Thanks for using the fun poll thingy, come again!')
