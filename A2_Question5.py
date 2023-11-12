#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 18:17:57 2023

@author: ethandrover

Contact Manager Program with CSV file.

"""

import csv
import os

def title():
    
    """
    Title for program.

    """
    print("Contact Manager\n")
    
    
def menu_options():
    
    """
    Menu options for the user to pick from.

    """
    print("COMMAND MENU")
    print("list - Display all contacts\nview - View a contact ")
    print("add - Add a contact\ndel - Delete a contact")
    print("exit - Exit program\n")
    

def read_contacts():
    
    """
    Reads the contacts file from the operating system.

    Returns
    -------
    
        Returns the contact list that is provided in the file path.

    """
    
    file_path = 'contacts.csv'
    contacts = []

    # Check if the file exists using os.path.isfile()
    
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            contacts = [row for row in reader]

    return contacts


def write_contacts(contacts):
    
    """
    
    Write contacts to the 'contacts.csv' file.
    
    ----------
    A list of contacts to be written to the file.

    Returns
    -------
    None.

    """
    with open('contacts.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(contacts)
        
        # Writes each contact in a row instead of on one line.
        

def add_c(contacts):
    """
    Function for adding contacts to the 'contacts.csv' file.

    
    ----------

    Returns
    -------
    Contact to 'contacts.csv' using the write_contacts function.

    """
    name = input("Name: ")
    email = input("Email: ")
    phone_n = input("Phone: ")
    new_contact = [name, email, phone_n]
    contacts.append(new_contact)
    write_contacts(contacts)
    print(f"{name} was added.")
    

def delete_c(contacts):
    """
    Deletes a contact from the 'contacts.csv file.'
    ----------

    """
    list_c(contacts)
    if contacts:
        number = int(input("Number: "))
        if 1 <= number <= len(contacts):
            deleted_contact = contacts.pop(number - 1)
            write_contacts(contacts)
            print(f"{deleted_contact[0]} was deleted.")
        else:
            print("Invalid Selection.")
    else:
        print("No contacts to delete.")
        

def list_c(contacts):
    """
    Grabs the contents from 'contacts.csv' and lists them for the user.
    ----------

    Returns
    -------
    Returns a list of the contacts from the 'contatcs.csv file.'

    """
    
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact[0]}")

def view_c(contacts):
    """
    Displays a specific contact and its contents based on the users choice,
    and takes that information form the 'contatcs.csv' file.
    ----------

    Returns
    -------
    Returns contact information from a number in the list.

    """
    contact_number = int(input("Number: "))
    if 1 <= contact_number <= len(contacts):
        contact = contacts[contact_number - 1]
        print(f"Name: {contact[0]}\nEmail: {contact[1]}\nPhone: {contact[2]}")
    else:
        print("Invalid selection. Please try again.")



def main():
    
    """
    Main function for running the Prime Number Check program.

    """
    
    contacts = read_contacts()
    title()
    menu_options()
    while True:
        command = input("\nCommand: ").lower()
        if command == 'list':
            list_c(contacts)
        elif command == 'view':
            view_c(contacts)
        elif command == 'add':
            add_c(contacts)
        elif command == 'del':
            delete_c(contacts)
        elif command == 'exit':
            print("\nBye!")
            break
        else:
            print("Invalid command. Please enter a valid command.")

if __name__ == '__main__':
    main()