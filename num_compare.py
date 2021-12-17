#!/usr/bin/env python3
# Created by: Jedidiah
# Created on: Dec. 15, 2021
# This program asks the user for three numbers.
# It then displays the greatest number.


def main():

    # get input
    user_number = input("Enter your first number: ")
    # error checking
    try:
        user_number_int = int(user_number)
    except Exception:
        print("Invalid input, not a number")
        quit()

    user_numberII = (input("Enter your second number: "))
    try:
        user_numberII_int = int(user_numberII)
    except Exception:
        print("Invalid input, not a number")
        quit()

    user_numberIII = (input("Enter your third number: "))
    try:
        user_numberIII_int = int(user_numberIII)
    except Exception:
        print("Invalid input, not a number")
        quit()

    if user_number_int > user_numberII_int and user_numberIII_int:
        print("The first number was larger")

    elif user_numberII_int > user_number_int and user_numberIII_int:
        print("The second number was larger")

    elif user_numberIII_int > user_number_int and user_numberII_int:
        print("The third number was larger")

    return main()


if __name__ == "__main__":
    main()
