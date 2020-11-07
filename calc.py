# imports
import os
import subprocess

#***********************************#
#     Author: Katelynn Heasley      #
#       Date: 11/07/20              #
#***********************************#

# global vars
opc = ""

#******************** functions *******************#

# Function to print calculator menu


def print_menu():
    print('******************')
    print(' Welcome - PyCalc ')
    print('******************')

    print('[1] Add')
    print('[2] Subtract')
    print('[3] Multiply')
    print('[4] Divide')

    print('[5] Calculate age')

    print('[x] Exit')
    print('-' * 20)  # Print '*' 20 times


# Function to clear console
def clear():
    if os.name in ('nt', 'dos'):
        subprocess.call("cls")
    elif os.name in ('linux', 'osx', 'posix'):
        subprocess.call("clear")


# Function to perform calculations until 'exit'
while(opc != 'x'):

    print_menu()
    # Get User Input
    opc = input("Please select an option: ")

    if(opc == '1' or opc == '2' or opc == '3' or opc == '4'):
        # Get numbers
        number1 = float(input("What is the first number? "))
        number2 = float(input("What is the second number? "))
        # Check for division by zero error
        if(opc == '4' and number2 == 0):
            while(number2 == 0):
                number2 = float(
                    input("ERROR. Unable to divide by zero, provide a different second number: "))

        # Execute correct user choice
        # Remember that input() only takes a string!!!!
        if(opc == '1'):
            sum = number1 + number2
            print(str(number1) + " + " +
                  str(number2) + " = " + str(sum) + ". ")
        elif(opc == '2'):
            sub = number1 - number2
            print(str(number1) + " - " +
                  str(number2) + " = " + str(sub) + ". ")
        elif(opc == '3'):
            mul = number1 * number2
            print(str(number1) + " x " +
                  str(number2) + " = " + str(mul) + ". ")
        elif(opc == '4'):
            div = number1 / number2
            print(str(number1) + " / " +
                  str(number2) + " = " + str(div) + ". ")
    elif(opc == '5'):
        # Get age
        year = int(input("What year were you born? "))
        age = 2020 - year
        print("You are " + str(age) + " years old!")

    # Wait for user to see answer, then choose to continue or exit
    answer = input("Would you like to choose the main again? Y/N:  ")
    if(answer == 'Y' or answer == 'y'):
        clear()
    else:
        clear()
        break

# Message on program exit
print("~Thank You! Good byte!~")
