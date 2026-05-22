studentnames = []
studentgrades = []

def addstudent():
    name = input("Enter student name: ")
    grade = input("Enter student grade: ")
    studentnames.append(name)
    studentgrades.append(grade)
    print("Student added!")

def viewstudents():
    if len(studentnames) == 0:
        print("No students added yet")
    else:
        print("Student List:")
        for i in range(len(studentnames)):
            print(i+1, ".", studentnames[i], "-", studentgrades[i])

def deletestudent():
    viewstudents()
    number = int(input("Enter student number to delete: "))
    if number < 1 or number > len(studentnames):
        print("Invalid number")
    else:
        print(studentnames[number-1], "deleted")
        studentnames.pop(number-1)
        studentgrades.pop(number-1)

def searchstudent():
    name = input("Enter name to search: ")
    found = False
    for i in range(len(studentnames)):
        if name.lower() == studentnames[i].lower():
            print("Found:", studentnames[i], "-", studentgrades[i])
            found = True
    if found == False:
        print("Student not found")

print("Welcome to Student Management System")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        addstudent()
    elif choice == "2":
        viewstudents()
    elif choice == "3":
        searchstudent()
    elif choice == "4":
        deletestudent()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Wrong choice, try again")
