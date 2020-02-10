# Name: Jack Walmsley
# Date: 2019-02-10
# Filename: Project1-Poll.py
# Purpose: To create a user poll with three questions and error=checking

# Statistics
enjoysMathStats = {True: 63, False: 12}
englishFirstLangStats = {True: 94, False: 6}
gradeTookOssltStats = {9: 8, 10: 92, 11: 0, 12: 0}

def getInputOfType(message, failMessage, desiredType, min = None, max = None):
    """
    Loops until the user provides an input of desired type
    Params:
        message - the prompt for the user input
        failMessage - the message to give when input is of wrong type
        desiredType - the type of user input expected
    Returns:
        userInput - the user's input thaty was the correct type
    """
    while True:
        userInput = input(message)
        if desiredType == int:
                try:
                    userInput = int(userInput)
                    if min and max:
                        if not (userInput >= min and userInput <= max):
                            raise ValueError
                except ValueError:
                    print(failMessage)
                else:
                    return int(userInput)
        elif desiredType == float:
            try:
                float(userInput)
            except ValueError:
                print(failMessage)
            else:
                return float(userInput)
        elif desiredType == bool:
            if(userInput.lower() == 'yes'):
                return True
            elif userInput.lower() == 'no':
                return False
            else:
                print(failMessage)
        else:
            print("ERROR: That type isn't implemented yet.")
            return False

# Poll questions
# enjoysMath = getInputOfType('Do you enjoy math?', 'Sorry, please respond with yes or no', bool)
# if enjoysMath == True:
#     print('63% of students agree with you!')
# else:
#     print('12% of students agree with you!')
#
# englishFirstLang = getInputOfType('Do you speak english as your first language?', 'Sorry, please respond with yes or no', bool)
# if englishFirstLang == True:
#     print('So does 94% of the school!')
# else:
#     print('6% of the school doesn\'t either!')

gradeTookOsslt = getInputOfType('In what grade did you take the OSSLT?', 'Sorry, please respond with a number from 9 to 12', int, 9, 12)


# print('result is', getInputOfType('give me a number: ', 'Try again!', bool))
