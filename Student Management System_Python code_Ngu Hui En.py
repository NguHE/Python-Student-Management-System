# NGU HUI EN
# TP073894

# define student list to store records
students = []


# function to add a student record
def add_student():
    print("\nAdd Student\n")
    print("Enter student details:")
    name = valid_name()
    id = student_id()
    if any(student['id'] == id for student in students):
        print("ID already exists. Please enter a different ID.")
        return add_student()
    else:
        pass
    age = valid_age()
    gender = valid_gender()
    course = valid_course()
    cgpa = valid_cgpa()
    grade = valid_grade(cgpa)

    student = {
        'name': name,
        'id': id,
        'age': age,
        'gender': gender,
        'course': course,
        'cgpa': cgpa,
        'grade': grade,
    }
    students.append(student)
    print("\nStudent {} with ID {} has been added successfully.\n".format(name, id))


# validation of name
def valid_name():
    while True:
        name = input("Name: ")
        if not all(char.isalpha() or char.isspace() for char in name):
            print("Name must contain only alphabetical characters.")
            continue
        return name


# validation of id
def student_id():
    while True:
        try:
            id = int(input("Student ID: "))
            if id <= 0:
                print("ID must be a positive integer.")
                continue
            return id
        except ValueError:
            print("ID must be a valid integer.")


# validation of age input
def valid_age():
    while True:
        try:
            age = int(input("Age: "))
            if age <= 0:
                print("Age must be a positive integer.")
                continue
            return age
        except ValueError:
            print("Age must be a valid integer.")


# validation of gender input
def valid_gender():
    while True:
        gender = input("Gender (M/F/O): ")
        if gender.lower() not in ['m', 'f', 'o']:
            print("Gender must be either M, F or O.")
            continue
        return gender.upper()


# validation of course
def valid_course():
    while True:
        course = input("Course name: ")
        if not all(char.isalpha() or char.isspace() for char in course):
            print("Course name must contain only alphabetical characters.")
            continue
        return course


# validation of CGPA input
def valid_cgpa():
    while True:
        try:
            cgpa = round(float(input("CGPA: ")), 2)
            if(cgpa < 0 or cgpa >= 4.0):
                print("CGPA must be within 0.00 - 4.00.")
                continue
            return cgpa
        except ValueError:
            print("CGPA must be a valid integer.")


# defining grade of cgpa
def valid_grade(cgpa):
    if (cgpa >= 3.70 and cgpa <= 4.00):
        return "First class"
    elif (cgpa >= 3.00 and cgpa < 3.70):
        return "Second class, first division"
    elif (cgpa >= 2.30 and cgpa < 3.00):
        return "Second class, second division"
    elif (cgpa >= 2.00 and cgpa < 2.30):
        return "Third division"
    else:
        return "Fail"


# function to delete a student record
def delete_student():
    print("\nDelete Student\n")
    id = int(input("Enter student ID: "))
    found = False
    for student in students:
        if student['id'] == id:
            students.remove(student)
            found = True
            print("\nStudent with ID {} has been deleted successfully!\n".format(id))
            break
    if not found:
        print("\nStudent with ID {} not found.\n".format(id))


# function to search a student record
def search_student():
    print("\nSearch Student\n")
    id = int(input("Enter student ID to search: "))
    found = False
    for student in students:
        if student['id'] == id:
            print("\nStudent found!")
            print("Name:", student['name'])
            print("Student ID:", student['id'])
            print("Age:", student['age'])
            print("Gender:", student['gender'])
            print("Course Name:",student['course'])
            print("CGPA:", student['cgpa'])
            print("Degree classification:", student['grade'], "\n")
            found = True
            break
    if not found:
        print("Student not found.")


# function to update a student record
def update_student():
    print("\nUpdate Student\n")
    id = int(input("Enter student ID to update: "))
    for student in students:
        if student["id"] == id:
            print(f"\nCurrent student information:")
            print(f"Student Name: {student['name']}")
            print(f"Student ID: {student['id']}")
            print(f"Student Age: {student['age']}")
            print(f"Student Gender: {student['gender']}")
            print(f"Student Course Name: {student['course']}")
            print(f"Student CGPA: {student['cgpa']}")
            print(f"Student Degree Classification: {student['grade']}\n")

            print("Please enter new student information: ")
            name = valid_name()
            age = valid_age()
            gender = valid_gender()
            course = valid_course()
            cgpa = valid_cgpa()
            grade = valid_grade(cgpa)

            student['name'] = name
            student['age'] = age
            student['gender'] = gender
            student['course'] = course
            student['cgpa'] = cgpa
            student['grade'] = grade

            print("\nStudent with ID {} has been updated successfully!\n".format(id))
            return
    print("\nStudent with ID {} does not exist in the system!\n".format(id))


# function to view all student records
def view_all_students():
    print("\nView All Students\n")
    if len(students) == 0:
        print("No student records found.")
    else:
        print("All student records:")
        for student in students:
            print("Name:", student['name'])
            print("Student ID: ", student['id'])
            print("Age:", student['age'])
            print("Gender:", student['gender'])
            print("Course name:", student['course'])
            print("CGPA:", student['cgpa'])
            print("Degree classification:", student['grade'])
            print("")


# main menu function
def main_menu():
    while True:
        print("*************************************")
        print("Welcome to Student Management System!")
        print("1. Add a student record")
        print("2. Delete a student record")
        print("3. Search for a student record")
        print("4. Update a student record")
        print("5. View all student records")
        print("6. Exit")
        print("*************************************")
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            add_student()
        elif choice == '2':
            delete_student()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            view_all_students()
        elif choice == '6':
            print("Thank you for using Student Management System!")
            break
        else:
            print("Invalid choice. Please try again.\n")


# call the main menu function to start the program
main_menu()
