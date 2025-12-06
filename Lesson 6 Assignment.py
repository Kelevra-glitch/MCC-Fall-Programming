
def main():

    students = {}

    students["Tony"] = {
        "id": "1",
        "gpa": 3.8,
        "credits": 45,
        "grades": ["A", "A-", "B+"]
    }

    students["Steve"] = {
        "id": "2",
        "gpa": 3.2,
        "credits": 36,
        "grades": ["B", "B-", "C+"]
    }

    students["Becky"] = {
        "id": "3",
        "gpa": 3.9,
        "credits": 60,
        "grades": ["A", "A", "A"]
    }

    print(students)
    print()

    print("List of students")
    for name in students:
        print(name)
    print()

    print("Student information")
    print("Name\tID\tGPA\tCredits\tGrades")

    for name, info in students.items():
        print(name + "\t" +
              info["id"] + "\t" +
              str(info["gpa"]) + "\t" +
              str(info["credits"]) + "\t" +
              str(info["grades"]))
    print()

    print("Steve has dropped out, removing from student info registry")
    removed_student = students.pop("Steve")
    print("Removed:", removed_student)
    print("Updated dictionary:")
    print(students)
    print()

    print("getting GPA information")

    for name in students:
        gpa = students.get(name).get("gpa")
        print(name + "'s GPA:", gpa)
    print()

    print("Students have graduated, clearing the registry now.")
    students.clear()
    print("Dictionary after clearing:", students)

if __name__ == "__main__":
    main()
print("Completed by, Jacob Harper")