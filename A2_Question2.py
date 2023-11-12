#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 20:24:48 2023

@author: ethandrover

Contact Manager Program!

"""

def title():
    
    """
    Title for the contacts program.

    """
    print("Contact Manager\n")
    
    
def menu_options():
    
    """
    

    Displays menu options for the user to choose from.

    """
    print("COMMAND MENU")
    print("list - Display all contacts\nview - View a contact ")
    print("add - Add a contact\ndel - Delete a contact")
    print("exit - Exit program\n")
    
    
def list_c(contacts):
    
    """
    List the contacts that are in the contact list.

    Returns
    -------
    Returns the list of contacts, numbered and in order.

    """
    
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact[0]}")
        
        
         
def view_c(contacts):
    
    """
    Displays the contact details depending on which contact the user chooses.
    ----------
    
    Returns
    -------
    Contact information.

    """
    
    contact_number = int(input("Number: "))
    if 1 <= contact_number <= len(contacts):
            contact = contacts[contact_number - 1]
            print(f"Name: {contact[0]}\nEmail: {contact[1]}\nPhone: {contact[2]}")
    else:
        print("Invalid selection. Please try again.")
        
        

def add_c(contacts):
    
    """
   Function for adding a contact to the list of contacts.
    ----------

    Returns
    -------
    Returns the contact the user adds to the lists of contacts.

    """
    name = input("Name: ")
    email = input("Email: ")
    phone_n = input("Phone: ")
    contacts.append([name,email,phone_n])
    print(f"{name} Was added.")
    
    

def delete_c(contacts):
    
    """
   Deletes a contact from the list of contacts.
    ----------

    Returns
    -------
    Returns the list with the selected contact deleted.

    """
    
    number = int(input("Number: "))
    if number <1 or number > len(contacts):
        print("Invalid Selection \n")
    else:
        contact = contacts.pop(number-1)
        print(f"{contact[0]} was deleted.")
        
        
    
def main():
    
    """
    The main function to run the program.

    """
    
    contacts = [['Eric Idle','eric@ericidle.com','+44 20 7946 0958'],['Guido van Rossum','Guido@vanrossum.com','+66 40 8547 2035']]
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