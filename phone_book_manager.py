import csv
import sys
import os

import os

def clear_screen():
    """
    Clears the terminal screen.
    """
    os.system('clear')

def get_serial_no(file_path):
    """
    Get the serial number for the phone book entry.

    Args:
        file_path (str): The path to the file containing the phone book entries.

    Returns:
        int: The next serial number to be assigned to a new phone book entry.
    """
    if not os.path.exists(file_path) or os.stat(file_path).st_size == 0:    # if file does not exist or empty then return 1
        return 1
    else:
        with open(file_path, 'r') as file:  # open the file in read mode
            reader = csv.reader(file)
            last_row = None 
            for last_row in reader:
                pass
            if last_row and last_row[0].isdigit():  # if last row exists and first column is digit then return the next serial number
                return int(last_row[0]) + 1   # return the next serial number
            return 1

def add_data():
    """
    Adds contact information to the contact book.

    This function prompts the user to enter contact information such as first name, last name, number, email, and address.
    It then saves the information to a CSV file specified by the `file_path` variable.

    Args:
        None

    Returns:
        None
    """
    clear_screen()
    # data adding function

    file_path = "contact.csv"   # file path
    serial_no = get_serial_no(file_path)    # get the serial number
    print("Enter the following information to add into contact book: \n")
    fname= input("First Name: ")
    lname= input("Last Name: ")
    cell = input("Number: ")
    email = input("Email: ")
    address = input("Address: ")
    
    interrupt = input("Do you want to save the contact information? (y/n): ")   # ask for saving the data
    if interrupt.lower() == 'y':
        with open(file_path, 'a', newline='') as file:  # open the file in append mode
            writer = csv.writer(file)
            writer.writerow([serial_no, fname, lname, cell, email, address])    # write the data into the file
        
        print("Data added successfully.")
    else:
        print("Data not saved.")
    
    input("\nPress Enter to continue.") # wait for the user to press enter

import csv

def search_data():
    """
    Search for contact data based on the first name.

    This function prompts the user to enter a first name to search for in the contact data file.
    It reads the data from the "contact.csv" file and compares the entered first name with the first names in the file.
    If a match is found, it prints the corresponding contact information (name, number, email, and address).
    If no match is found, it prints a message indicating that the data was not found.

    Note: This function assumes that the contact data is stored in a CSV file with the following format:
    First Name, Last Name, Number, Email, Address

    Args:
        None

    Returns:
        None
    """
    clear_screen()

    interrupt = input("Enter the first name to search: ")   # ask for the first name to search
    with open("contact.csv", 'r') as file:  # open the file in read mode
        reader = csv.reader(file)
        for row in reader:
            if row[1].lower() == interrupt.lower():   # if first name matches then print the data
                print(f"Name: {row[1]} {row[2]}")
                print(f"Number: {row[3]}")
                print(f"Email: {row[4]}")
                print(f"Address: {row[5]}")
                break
        else:
            print("Data not found.")

    input("\nPress Enter to continue.")   # wait for the user to press enter

import csv

def update_data():
    """
    Updates the contact information in the phone book.

    This function prompts the user to enter the first name of the contact to update.
    It then reads the contact information from a CSV file, displays the current information,
    and prompts the user to enter the updated information. Finally, it updates the CSV file
    with the new information.

    Args:
        None

    Returns:
        None
    """
    clear_screen()

    interrupt = input("Enter the first name to update: ")   # ask for the first name to update
    with open("contact.csv", 'r') as file:
        reader = csv.reader(file)
        data = []
        for row in reader:
            if row[1].lower() == interrupt.lower():  # if first name matches then update the data
                print(f"Name: {row[1]} {row[2]}")
                print(f"Number: {row[3]}")
                print(f"Email: {row[4]}")
                print(f"Address: {row[5]}")
                print("\n")
                fname= input("First Name: ")
                lname= input("Last Name: ")
                cell = input("Number: ")
                email = input("Email: ")
                address = input("Address: ")
                data.append([row[0], fname, lname, cell, email, address])   # append the updated data
            else:
                data.append(row)    # append the data as it is
        
    with open("contact.csv", 'w', newline='') as file:  # open the file in write mode
        writer = csv.writer(file)
        writer.writerows(data)  # write the updated data into the file

    input("\nPress Enter to continue.")  # wait for the user to press enter

def delete_data():
    """
    Deletes a contact from the phone book.

    This function prompts the user to enter the first name of the contact to delete.
    If the contact is found, the user is asked for confirmation before deleting the contact.
    The contact is deleted from the 'contact.csv' file if the user confirms the deletion.

    Args:
        None

    Returns:
        None
    """
    clear_screen()

    entries = []
    if os.path.exists("contact.csv") and os.stat("contact.csv").st_size != 0:   # if file exists and not empty then read the data
        with open("contact.csv", 'r') as file:
            reader = csv.reader(file)
            for row in reader:  
                entries.append(row) # append the data into the list

    interrupt = input("Enter the first name to delete: ")   # ask for the first name to delete
    
    entries_to_keep = [entry for entry in entries if entry[1].lower() != interrupt.lower()] # keep the data which does not match the first name
    if len(entries) == len(entries_to_keep):    # if length of entries and entries to keep are same then data not found 
        print("Data not found.")
    else:
        interrupt = input("Do you want to delete the contact information? (y/n): ")  # ask for deleting the data
        if interrupt.lower() == 'y':    # if yes then write the data into the file
            for index, entry in enumerate(entries_to_keep, start = 0):  # enumerate the data and assign the serial number
                entry[0] = index + 1    
            with open("contact.csv", 'w', newline='') as file:  
                writer = csv.writer(file)
                writer.writerows(entries_to_keep)   # write the data into the file
            print("Data deleted successfully.")
        else:
            print("Data not deleted.")
    
    input("\nPress Enter to continue.") # wait for the user to press enter

def print_data():
    """
    Prints the contact list stored in a CSV file.

    Reads the data from the 'contact.csv' file and prints each contact's details,
    including serial number, name, number, email, and address. After printing the
    contact list, it waits for user input to continue.

    Args:
        None

    Returns:
        None
    """
    clear_screen()
    print("Contact List: \n")
    
    with open("contact.csv", 'r') as file:
        reader = csv.reader(file)
        serial = 1
        for row in reader:  # read the data from the file and print it
            print(f"Serial: {serial}")
            print(f"Name: {row[1]} {row[2]}")
            print(f"Number: {row[3]}")
            print(f"Email: {row[4]}")
            print(f"Address: {row[5]}")
            serial += 1
            print("\n")
    input("Press Enter to continue.")   # wait for the user to press enter

def main():
    """
    The main function of the Phone Book Manager program.
    Displays a menu of options and performs the selected action based on user input.
    """
    while True:
        clear_screen()
        print("Phone Book Manager \n")
    
        print("1. Add Data")
        print("2. Search data?")
        print("3. Update data?")
        print("4. Delete data?")
        print("5. View data?")
        print("\nPress 0 for exit.")
        
        interupt = input("What you want to do? ")
        match interupt:  # match the input with the cases and perform the action
            case '1':
                add_data()
            case '2':
                search_data()
            case '3':
                update_data()
            case '4':
                delete_data()
            case '5':
                print_data()
            case '0':
                sys.exit()
            case _:
                print("Wrong entry: Try again!") 

if __name__ == "__main__":
    main()