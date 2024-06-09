import csv

def add_data():
    print("Execute add data function.")

def search_data():
    print("Execute add search function.")

def update_data():
    print("Execute add update function.")

def delete_data():
    print("Execute add delete function.")

def print_data():
    print("Execute add print function.")

def main():
    print("Phone Book Manager \n\n")
    
    print("1. Add Data")
    print("2. Search data?")
    print("3. Update data?")
    print("4. Delete data?")
    print("5. View data?")

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
        case _:
            print("Wrong entry: Try again!")



if __name__ == "__main__":
    main()