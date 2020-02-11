# Name: Jack Walmsley
# Date: 2019-02-10
# Filename: JackWalmsleyPolls.py
# Purpose: To create a user poll with three questions and error-checking, which gives the user some interesting data
# based on their answers

# Percentages for different answers
enjoysMathStats = {True: 63, False: 12} # Do you enjoy math?
englishFirstLangStats = {True: 94, False: 6}    # Is english your first language?
generationStats = {14: 15.8,
                   24: 11.5,
                   54: 40.5,
                   64: 14.1,
                   130: 18.1}   # How old are you? Keys are maximum ages for each generation (eg. 0-14, 15-24, etc.)


def getInputOfType(message, failMessage, desiredType, minVal=None, maxVal=None):
    """
    Loops until the user provides an input of desired type
    Params:
        message - the prompt for the user input
        failMessage - the message to give when input is of wrong type
        desiredType - the type of user input expected
        min - the minimum value, only used if the desired type is a number
        max - the maximum value, only used if the desired type is a number
    Returns:
        userInput - the user's input that was the correct type
    """
    while True:
        userInput = input(message + ' ') # Add a space to the end of the question for readability
        if desiredType == int:
            try:
                userInput = int(userInput)
                # If the value is outside of the min and max
                if minVal is not None and maxVal is not None:
                    if not (maxVal >= userInput >= minVal):
                        raise ValueError
            except ValueError:
                print(failMessage)
                continue
            else:
                # Input is correct type and within min and max
                return int(userInput)

        elif desiredType == bool:
            # Boolean input is in terms of 'yes' or 'no' for user-friendliness
            if userInput.lower() == 'yes':
                return True
            elif userInput.lower() == 'no':
                return False
            else:
                print(failMessage)
                continue
        else:
            # The desired type is not one of the expected ones (int, bool)
            raise ValueError


# Poll questions
print('Welcome to the fun poll thingy')
print('Data sources: 2018 Peel Student Census, 2016 Canadian Census')

enjoysMath = getInputOfType('Do you enjoy math?', 'Sorry, please respond with yes or no', bool)
if enjoysMath:
    print('63% of PCSS students agree with you!')
else:
    print('12% of PCSS students agree with you!')

englishFirstLang = getInputOfType('Do you speak english as your first language?',
                                  'Sorry, please respond with yes or no', bool)
if englishFirstLang:
    print('So does 94% of the school!')
else:
    print('6% of the school doesn\'t either!')

# Max age 130, the oldest person ever was 122
userAge = getInputOfType('How old are you?', 'Sorry, please provide a whole number from 0 to 130', int, 0, 130)
for age in generationStats:
    if userAge <= age:
        print(generationStats[age], 'percent of Canadians are in the same generation as you!')
        # Stop the loop so it doesn't print every generation above the correct one
        break

print('Thanks for using the fun poll thingy, come again!')
