first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
current_year = int(input("Please enter the current year: "))
birth_year = int(input("Please enter your birth year: "))
age = current_year - birth_year
print("Hello, " + first_name + " " +last_name + "!\nYou are " +str(age) + " years old this year.")
age += 1
print(f"Next year you will be {age} years old.")
print("Completed by, Jacob Harper")