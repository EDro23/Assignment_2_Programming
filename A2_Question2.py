#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 20:24:48 2023

@author: ethandrover
"""

def title():
    print("Contact Manager\n")
    
def menu_options():
    print("COMMAND MENU")
    print("list - Display all contacts\nview - View a contact ")
    print("add - Add a contact\ndel - Delete a contact")
    print("exit - Exit program\n")
    
def list_c(contacts):
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact[0]}")
         
def view_c(contacts):
    contact_number = int(input("Number: "))
    if 1 <= contact_number <= len(contacts):
            contact = contacts[contact_number - 1]
            print(f"Name: {contact[0]}\nEmail: {contact[1]}\nPhone: {contact[2]}")
    else:
        print("Invalid selection. Please try again.")

def add_c(contacts):
    name = input("Name: ")
    email = input("Email: ")
    phone_n = input("Phone: ")
    contacts.append([name,email,phone_n])
    print(f"{name} Was added.")

def delete_c(contacts):
    number = int(input("Number: "))
    if number <1 or number > len(contacts):
        print("Invalid Selection \n")
    else:
        contact = contacts.pop(number-1)
        print(f"{contact[0]} was deleted.")
    
def main():
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