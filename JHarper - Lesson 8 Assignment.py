
def create_csv_file(filename):

    file = open(filename, "w")
    file.write("Name,Phone,Email\n")
    file.close()
    print("Contact file created successfully.\n")


def add_contact(filename):

    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    file = open(filename, "a")
    file.write(name + "," + phone + "," + email + "\n")
    file.close()

    print("Contact added successfully.\n")


def view_contacts(filename):

    print("\n----- Contact List -----")

    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    for i in range(1, len(lines)):
        line = lines[i].strip()
        parts = line.split(",")
        if len(parts) == 3:
            print(str(i) + ". Name: " + parts[0] + 
                  " | Phone: " + parts[1] + 
                  " | Email: " + parts[2])
    print()


def edit_contact(filename):

    print("\nCurrent Contacts:")
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    contacts = []

    for i in range(1, len(lines)):
        line = lines[i].strip()
        parts = line.split(",")
        contacts.append(parts)

        print(str(i) + ". " + parts[0] + " | " + parts[1] + " | " + parts[2])

    print()


    choice = int(input("Enter the number of the contact to edit: "))

    if choice < 1 or choice > len(contacts):
        print("Error: Contact not found.\n")
        return

    new_phone = input("Enter new phone: ")
    new_email = input("Enter new email: ")

    contacts[choice - 1][1] = new_phone
    contacts[choice - 1][2] = new_email

    file = open(filename, "w")
    file.write("Name,Phone,Email\n")
    for c in contacts:
        file.write(c[0] + "," + c[1] + "," + c[2] + "\n")
    file.close()

    print("Contact updated successfully.\n")

def main():
    print("Welcome to the Contact Manager Program")
    filename = "contacts.csv"

    while True:
        print("Menu:")
        print("1 - Create new contact CSV file")
        print("2 - Add a new contact")
        print("3 - View all contacts")
        print("4 - Edit an existing contact")
        print("5 - Exit")
        
        option = input("Enter your choice: ")

        if option == "1":
            create_csv_file(filename)

        elif option == "2":
            add_contact(filename)

        elif option == "3":
            view_contacts(filename)

        elif option == "4":
            edit_contact(filename)

        elif option == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid option. Please try again.\n")

main()

print("Completed by, Jacob Harper")