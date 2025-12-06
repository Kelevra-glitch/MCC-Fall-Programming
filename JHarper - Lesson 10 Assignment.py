
def get_input(prompt):

    user_value = input(prompt)
    return user_value


def find_substring(main_string, sub_string):

    index = main_string.find(sub_string)

    if index != -1:
        print(f"The substring was found at index {index}.")
        return index
    else:
        print("The substring was not found.")
        return -1


def get_yes_no(prompt):

    choice = input(prompt).lower()

    while choice != "y" and choice != "n":
        print("Invalid entry. Please type 'y' or 'n'.")
        choice = input(prompt).lower()

    return choice


def main():
    print("This program searches for a substring within a string and optionally replaces it.")

    main_string = get_input("Enter the main string: ")
    sub_string = get_input("Enter the substring to search for: ")

    index = find_substring(main_string, sub_string)

    if index != -1:
        choice = get_yes_no("Would you like to replace the substring? (y/n): ")

        if choice == "n":
            print("No replacement was made.")
        else:
            new_string = get_input("Enter the new substring: ")
            updated_string = main_string.replace(sub_string, new_string, 1)
            print("The updated string is:")
            print(updated_string)

    print("Thank you for using this program!")


main()

print("Completed by, Jacob Harper")