import random

def main():
    print("===== Grade Calculator =====")
    grades = []

    while True:
        grade_input = input("Enter a grade (or -1 to stop): ")

        grade = int(grade_input)

        if grade == -1:
            break
        else:
            grades.append(grade)

    print("\nGrades entered:")
    print(grades)

    print("\n===== Removing Lowest Grade =====")
    lowest = min(grades)
    lowest_index = grades.index(lowest)
    grades.pop(lowest_index)

    print("Updated grades:")
    print(grades)

    print("\n===== Removing Random Grade =====")
    random_grade = random.choice(grades)
    grades.remove(random_grade)

    print("Updated grades:")
    print(grades)

    print("\n===== Edit a Grade =====")
    for i in range(len(grades)):
        print(str(i + 1) + ".", grades[i])

    while True:
        choice = int(input("Enter the number of the grade you want to edit: "))
        if choice < 1 or choice > len(grades):
            print("Invalid selection. Try again.")
        else:
            break

    new_grade = int(input("Enter the new grade: "))
    grades[choice - 1] = new_grade

    print("Updated grades:")
    print(grades)

    print("\n===== Sorting and Reversing Grades =====")
    grades.sort()
    grades.reverse()

    print("Updated grades:")
    print(grades)

    print("\n===== Grade Total and Average =====")
    total = sum(grades)
    average = total / len(grades)

    print("Total of grades:", total)
    print("Average grade:", average)

if __name__ == "__main__":
    main()
print("Completed by, Jacob Harper")