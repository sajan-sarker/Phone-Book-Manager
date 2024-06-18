import csv
import sys
import os

def clear_screen():
    os.system('clear')

def get_serial_no(file_path):   # get the serial number
    if not os.path.exists(file_path) or os.stat(file_path).st_size == 0:   # check if file exists or not
        return 1    # if file does not exist or empty then return 1
    else:
        with open(file_path, 'r') as file:  
            reader = csv.reader(file)
            last_row = None
            for last_row in reader: # get the last row
                pass
            if last_row and last_row[0].isdigit():  # check if last row is not empty and first column is digit
                return int(last_row[0]) + 1 # return the next serial number
            return 1

def add_data():
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
    
    interrupt = input("Do you want to save the contact information? (y/n): ")
    if interrupt.lower() == 'y':
        with open(file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([serial_no, fname, lname, cell, email, address])
        
        print("Data added successfully.")
        input("\nPress any key to continue.")
    else:
        print("Data not saved.")
        input("\nPress any key to continue.")

def search_data():
    clear_screen()
    print("Execute add search function.")

def update_data():
    clear_screen()
    print("Execute add update function.")

def delete_data():
    clear_screen()
    print("Execute add delete function.")

def print_data():
    clear_screen()
    print("Execute add print function.")

def main_screen():
    while True:
        clear_screen()
        print("Phone Book Manager \n")
    
        print("1. Add Data")
        print("2. Search data?")
        print("3. Update data?")
        print("4. Delete data?")
        print("5. View data?")
        print("\nPress 0 for exit.")
        interupt = int(input("What you want to do? (1/2/3/4): "))
        match interupt:
            case 1:
                add_data()
            case 2:
                search_data()
            case 3:
                update_data()
            case 4:
                delete_data()
            case 5:
                print_data()
            case 0:
                sys.exit()
            case _:
                print("Wrong entry: Try again!")

def main():
    main_screen()


if __name__ == "__main__":
    main()