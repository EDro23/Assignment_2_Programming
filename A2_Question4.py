#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 11:44:48 2023

@author: ethandrover

The Wizard Program

"""

import random
import os


def title():
    """
    Title for the program.

    """
    print("The Wizard Inventory program")
    print()


def menu_options():
    """
    Menu options for the user to choose from.

    """
    print("walk - Walk down the path")
    print("show - Show all items")
    print("drop - Drop item")
    print("exit - Exit program")


def show(items):
    """
    Creates each item in the list and formats them in a visible list for the user.
    ----------

    Returns
    -------
    Returns a numbered list of items in the wizards inventory.

    """
    for num, item in enumerate(items, start=1):
        print(f"{num}. {item}")


def file_exists(file_path):
    """
    Checks to see if the file exists.

    """
    return os.path.isfile(file_path)


def load_items_from_file(file_path):
    """
    Checks to see if the file exists before attempt opening.

    """
    file_content = []
    if file_exists(file_path):
        with open(file_path, 'r') as file:
            file_content = [line.strip() for line in file.readlines()]
    return file_content


def save_items_to_file(file_path, items):
    """
    

    Parameters
    ----------
    file_path : TYPE
        DESCRIPTION.
    items : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    with open(file_path, 'w') as file:
        for item in items:
            file.write(item + '\n')


def walk(items):
    """
    Load items from 'wizard_all_items.txt',
    filter out items already in the wizards inventory.

    Returns
    -------
    Returns a random item and asks the user if they want to pick it up.

    """

    all_items = load_items_from_file('wizard_all_items.txt')

    new_items = [item for item in all_items if item not in items]

    if new_items:
        random_item = random.choice(new_items)
        print(
            f"While walking down a path, you see a {random_item}. Do you want to grab it? (y/n): ")

        choice = input().lower()
        if choice == 'y':
            if len(items) >= 4:
                print("You can't carry more items. Drop something first.")
            else:
                items.append(random_item)
                print(f"{random_item} was added to your inventory.")
                save_items_to_file('wizard_inventory.txt', items)
        else:
            print(f"You chose not to pick up {random_item}.")
    else:
        print("No new items to pick up.")


def drop_item(items):
    """
    A function to drop an item from the wizards inventory.

    Returns
    -------
    Returns the wizards inventory with the item removed.

    """
    number = int(input("Number: "))
    if number < 1 or number > len(items):
        print("Invalid item number")
    else:
        item = items.pop(number - 1)
        print(f"{item} was dropped.")
        save_items_to_file('wizard_inventory.txt', items)


def main():
    """
    Main function for running the program.

    """
    # Load items from 'wizard_inventory.txt' at the start
    wizard_inv = load_items_from_file('wizard_inventory.txt')

    title()
    menu_options()

    while True:
        print()
        task = input("Command: ")
        if task == 'show'.lower():
            show(wizard_inv)
        elif task == 'drop'.lower():
            drop_item(wizard_inv)
        elif task == 'walk'.lower():
            walk(wizard_inv)
        elif task == 'exit'.lower():
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")


if __name__ == '__main__':
    main()
