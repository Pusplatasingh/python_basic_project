# Add a student
def add_student(students, next_id):
    name = input("Enter student's name: ")
    try:
        marks = int(input("Enter marks: "))
    except ValueError:
        print("Invalid input for marks. Must be a number.")
        return next_id

    # Check for duplicate
    for student in students:
        if student['name'].lower() == name.lower() and student['marks'] == marks:
            print(f"\nA student with the same name and marks already exists (ID: {student['id']}).")
            confirm = input("Do you still want to add this student? (y/n): ").lower()
            if confirm != 'y':
                print("Student not added.")
                return next_id
            break  # If confirmed, skip checking other duplicates

    # Add student
    student = {"id": next_id, "name": name, "marks": marks}
    students.append(student)
    print("Student added.")
    return next_id + 1
    
# Display all students

def show_students(students):
    print("\n--- Student List ---")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, Marks: {student['marks']}")

# Save to file

def save_to_file(students):
    with open("students.txt", "w") as f:
        for student in students:
            f.write(f"{student['id']},{student['name']},{student['marks']}\n")
            
# Edit student details by ID
def edit_student(students):
    try:
        student_id = int(input("Enter student ID to edit: "))
        for student in students:
            if student['id'] == student_id:
                print(f"Current Name: {student['name']}, Marks: {student['marks']}")
                new_name = input("Enter new name (or press Enter to keep current): ")
                new_marks_input = input("Enter new marks (or press Enter to keep current): ")
                
                if new_name:
                    student['name'] = new_name
                if new_marks_input:
                    student['marks'] = int(new_marks_input)

                print("Student record updated.")
                return
        print("Student ID not found.")
    except ValueError:
        print("Invalid input.")
# Main program loop

students = []
next_id = 1  # Unique ID starts from 1

while True:
    print("\n1. Add Student")
    print("2. Show Students")
    print("3. Save to File")
    print("4. Edit Student")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        next_id = add_student(students, next_id)
    elif choice == "2":
        show_students(students)
    elif choice == "3":
        save_to_file(students)
        print("Saved to students.txt")
    elif choice == "4":
        edit_student(students)
    elif choice == "5":
        break
    else:
        print("Invalid option.")