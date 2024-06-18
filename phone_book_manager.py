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
    else:
        print("Data not saved.")
    
    input("\nPress Enter to continue.")

def search_data():
    clear_screen()

    interrupt = input ("Enter the first name to search: ")
    with open("contact.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1].lower() == interrupt.lower():
                print(f"Name: {row[1]} {row[2]}")
                print(f"Number: {row[3]}")
                print(f"Email: {row[4]}")
                print(f"Address: {row[5]}")
                break
        else:
            print("Data not found.")

    input("\nPress Enter to continue.")

def update_data():
    clear_screen()

    interrupt = input("Enter the first name to update: ")
    with open("contact.csv", 'r') as file:
        reader = csv.reader(file)
        data = []
        for row in reader:
            if row[1].lower() == interrupt.lower():
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
                data.append([row[0], fname, lname, cell, email, address])
            else:
                data.append(row)
        
    with open("contact.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    input("\nPress Enter to continue.")

def delete_data():
    clear_screen()

    entries = []
    if os.path.exists("contact.csv") and os.stat("contact.csv").st_size != 0:
        with open("contact.csv", 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                entries.append(row)

    interrupt = input("Enter the first name to delete: ")
    
    entries_to_keep = [entry for entry in entries if entry[1].lower() != interrupt.lower()]
    if len(entries) == len(entries_to_keep):
        print("Data not found.")
    else:
        interrupt = input("Do you want to delete the contact information? (y/n): ")
        if interrupt.lower() == 'y':
            for index, entry in enumerate(entries_to_keep, start = 0):
                entry[0] = index + 1
            with open("contact.csv", 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(entries_to_keep)
            print("Data deleted successfully.")
        else:
            print("Data not deleted.")
    
    input("\nPress Enter to continue.")

def print_data():
    clear_screen()
    
    with open("contact.csv", 'r') as file:
        reader = csv.reader(file)
        serial = 1
        for row in reader:
            print(f"Serial: {serial}")
            print(f"Name: {row[1]} {row[2]}")
            print(f"Number: {row[3]}")
            print(f"Email: {row[4]}")
            print(f"Address: {row[5]}")
            serial += 1
            print("\n")
    input("Press Enter to continue.")

def main():
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
        match interupt:
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