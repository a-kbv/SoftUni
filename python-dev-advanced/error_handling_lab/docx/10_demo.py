class Error(Exception):
    # Base class for other exceptions
    pass

class Four_Digit_Error(Error):
    # Raised when number is less or more than 4 digits
    pass

class Number_Have_Alpha_Error(Error):
    # Raised when the number have letters in it
    pass

class Digit_All_Different_Error(Error):
    # Raised when the digits duplicate
    pass

class First_Digit_Zero_Error(Error):
    # Raised when the first digit is zero
    pass

def check_number(word):

    while True:

        try:
            number_i = input(f"Enter a {word} number: ")

            if not number_i.isnumeric():
                raise Number_Have_Alpha_Error

            number = [int(el) for el in number_i]

            if len(number) != 4:
                raise Four_Digit_Error

            elif len(list(set(number))) != len(number):
                raise Digit_All_Different_Error

            elif number[0] == 0:
                raise First_Digit_Zero_Error

            break

        except Number_Have_Alpha_Error:
            print("Number must contain only digits!")
            print()

        except Four_Digit_Error:
            print("You must write a 4-digit number!")
            print()

        except Digit_All_Different_Error:
            print("The digits must be all different!")
            print()

        except First_Digit_Zero_Error:
            print("The number cannot start with Zero!")
            print()

    return number