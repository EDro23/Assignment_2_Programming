#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 17:40:36 2023

@author: ethandrover
The Prime Number Checker Program!

"""

def is_prime(number):
    """
    

    Parameters
    ----------
    number : integer
        Checks if the user has entered a prime number.
        Must be an integer.

    Returns
    -------
    Returns either true for prime number or false if it has factors.

    """
    if int(number) < 2:
        return False # Returns false if the number is greater than 2
    for i in range(2, int(float(number)**0.5) + 1):
        if int(float(number)) % i == 0:
            return False
    return True

def list_factors(number):
    """
    

    Parameters
    ----------
    number : integer,float
        Lists the factors of the number if not prime.

    Returns
    -------
    returns the factors list.

    """
    factors = []
    for i in range(1, int(float(number)) + 1):
        if int(float(number)) % i == 0:
            factors.append(i)
    return factors

def main():
    """
    Main function to program that returns result to what the user enters.

    Returns
    -------
    Result of the number and asks the user if they would like to try again.

    """
    print("Prime Number Checker\n")

    while True:
        input_number = input("Please enter an integer between 1 and 5000: ")

        if not input_number.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        input_number = int(input_number)

        if 1 <= input_number <= 5000:
            if is_prime(input_number):
                print(f"{input_number} is a prime number.")
            else:
                factors = list_factors(input_number)
                print(f"{input_number} is NOT a prime number.\nIt has {len(factors)} factors: {', '.join(map(str, factors))}")
        else:
            print("\nPlease enter a number between 1 and 5000.")

        try_again = input("\nTry again? (y/n): ").lower()
        print()
        if try_again != 'y':
            break

    print("Bye!")

if __name__ == "__main__":
    main()