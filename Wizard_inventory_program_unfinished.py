#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 17:28:56 2023

@author: kaileyslaney
"""

import random

items = ['wooden staff','wizard hat','cloth shoes']

def title():
    print("The Wizard Inventory Program")
    print()

def menu_options():
    print("walk - walk dwon the path")
    print("show - Show all items")
    print("drop - Drop item")
    print ("exit - Exit program")
    print()


def show(items):
    for num,item in enumerate(items, start=1):
        print(f"{num}. {item}")
        
def walk(items):
    # Load items from a text file
    with open('wizard_all_items.txt', 'r') as file:
        all_items = file.readlines()

    # Filter out items already in the wizard's inventory
    new_items = [item.strip() for item in all_items if item.strip() not in items]

    if new_items:
        random_item = random.choice(new_items)
        print(f"You found a {random_item}! Do you want to pick it up? (yes/no)")

        choice = input().lower()
        if choice == 'yes':
            items.append(random_item)
            print(f"{random_item} was added to your inventory.")
        else:
            print(f"You chose not to pick up {random_item}.")
    else:
        print("No new items to pick up.")


def drop_item(items):
    number = int(input("Number: "))
    if number < 1 or number > len(items):
        print("Invalid item number")
        
    else:
        item = items.pop(number-1)
        print(f"{item} Was added")
        
def main():
    title()
    menu_options()
    while True:
        task = input("Command: ")
        if task == 'show'.lower():
            show(items)
        elif task == 'drop'.lower():
            drop_item(items)
        elif task == 'walk'.lower():
            walk(items)
        elif task == 'exit'.lower():
            break
        else:
            print("Not a valid command. Please try again.\n")
    print()
    print("Bye!")

    
if __name__ == '__main__':
    main()